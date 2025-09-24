"""Shared utilities for box office modeling notebooks.

This module consolidates common feature-preparation, evaluation, and
reporting helpers so that the notebooks stay focused on exploratory
work without duplicating logic.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Columns that should not be used as model inputs.
DEFAULT_EXCLUDE_COLS: Tuple[str, ...] = (
    # Metadata columns
    'adult', 'backdrop_path', 'genre_ids', 'id', 'original_language',
    'original_title', 'overview', 'poster_path', 'release_date', 'title',
    'video', 'genres', 'title_normalized', 'rank', 'distributor',
    'genre_names', 'release_month_name', 'nearest_holiday',
    'nearby_major_releases_max_revenue', 'days_to_nearest_major_release',
    # Target columns
    'domestic_revenue', 'revenue_domestic', 'revenue',
    # String / categorical columns that would need separate encoding
    'primary_genre', 'release_season', 'competition_intensity',
    # Post-release TMDb signals that leak future information
    'popularity', 'vote_average', 'vote_count',
    # Raw year (replaced by engineered time features)
    'release_year',
)

# Helpful flags that are useful to surface when presenting results.
DEFAULT_FEATURE_FLAGS: Tuple[str, ...] = (
    'is_marvel', 'is_dc', 'is_star_wars', 'is_superhero', 'is_sequel',
    'is_live_action_remake', 'is_major_studio', 'is_disney'
)


def prepare_features(
    df: pd.DataFrame,
    *,
    target: str = 'revenue_domestic',
    exclude_cols: Optional[Sequence[str]] = None,
    filter_major_only: bool = False,
    drop_major_flag_from_features: bool = True,
    verbose: bool = True,
) -> Tuple[pd.DataFrame, List[str], str]:
    """Return a copy of ``df`` prepared for modeling and the feature list.

    Parameters
    ----------
    df:
        Input dataframe produced by the feature-engineering notebook.
    target:
        Name of the target column. Returned unchanged for convenience.
    exclude_cols:
        Optional iterable with extra columns to exclude. When ``None`` the
        :data:`DEFAULT_EXCLUDE_COLS` list is used.
    filter_major_only:
        If ``True`` the dataframe is filtered down to major studios
        (``is_major_studio == 1``).
    drop_major_flag_from_features:
        If ``True`` the ``is_major_studio`` column will not be included in
        the returned feature list (helpful when it is constant).
    verbose:
        When ``True`` the function prints a short summary mirroring what the
        notebooks previously reported.
    """
    df_prepared = df.copy()
    if filter_major_only and 'is_major_studio' in df_prepared.columns:
        df_prepared = df_prepared[df_prepared['is_major_studio'] == 1].copy()

    if exclude_cols is None:
        exclude_cols = list(DEFAULT_EXCLUDE_COLS)
    else:
        exclude_cols = list(exclude_cols)

    if drop_major_flag_from_features:
        exclude_cols.append('is_major_studio')

    potential_features = [
        col for col in df_prepared.columns if col not in set(exclude_cols)
    ]

    feature_cols: List[str] = []
    excluded_strings: Dict[str, Sequence[str]] = {}

    for col in potential_features:
        series = df_prepared[col]
        if pd.api.types.is_numeric_dtype(series):
            feature_cols.append(col)
            continue
        if pd.api.types.is_bool_dtype(series):
            feature_cols.append(col)
            continue
        # Allow binary-like object columns
        distinct = series.dropna().unique()
        if len(distinct) <= 2:
            feature_cols.append(col)
        else:
            excluded_strings[col] = distinct[:5]

    if verbose:
        print("\n🔧 Feature preparation summary:")
        if filter_major_only:
            print(f"   • Rows after major-studio filter: {len(df_prepared):,}")
        print(f"   • Candidate features: {len(feature_cols)}")
        if excluded_strings:
            print("   • Excluded non-numeric columns:")
            for col, sample in excluded_strings.items():
                print(f"     – {col}: sample values {list(sample)}")
        missing = df_prepared[feature_cols].isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            print("   • Columns with missing values:")
            for name, count in missing.items():
                print(f"     – {name}: {int(count)} nulls")
        else:
            print("   • No missing values in selected features ✅")

    return df_prepared, feature_cols, target


def create_sample_weights(
    df: pd.DataFrame,
    *,
    pandemic_flag: str = 'is_pandemic_year',
    pandemic_weight: float = 0.3,
) -> np.ndarray:
    """Return sample weights that down-weight pandemic-era rows."""
    weights = np.ones(len(df), dtype=float)
    if pandemic_flag in df.columns:
        mask = df[pandemic_flag].astype(bool).to_numpy()
        weights[mask] = pandemic_weight
    return weights


def evaluate_model(
    model,
    X_val: pd.DataFrame,
    y_val_log: Optional[pd.Series],
    y_val_actual: pd.Series,
    model_name: str,
) -> Dict[str, object]:
    """Evaluate ``model`` on validation data and return metric summary."""
    y_pred_log = model.predict(X_val)
    y_pred = np.expm1(y_pred_log)

    mse = mean_squared_error(y_val_actual, y_pred)
    rmse = float(np.sqrt(mse))
    mae = float(mean_absolute_error(y_val_actual, y_pred))
    r2 = float(r2_score(y_val_actual, y_pred))
    mape = float(np.mean(np.abs((y_val_actual - y_pred) / y_val_actual)) * 100)

    print(f"\n{model_name} Performance:")
    print(f"  RMSE: ${rmse:,.0f}")
    print(f"  MAE:  ${mae:,.0f}")
    print(f"  MAPE: {mape:.1f}%")
    print(f"  R²:   {r2:.3f}")

    return {
        'model': model_name,
        'model_name': model_name,
        'rmse': rmse,
        'mae': mae,
        'mape': mape,
        'r2': r2,
        'predictions': y_pred,
        'model_object': model,
    }


def get_top10_predictions(
    model,
    data: pd.DataFrame,
    year: int,
    feature_cols: Sequence[str],
    *,
    target_col: str = 'revenue_domestic',
    feature_flags: Sequence[str] = DEFAULT_FEATURE_FLAGS,
) -> Optional[pd.DataFrame]:
    """Return the top 10 predicted titles for ``year`` using ``model``."""
    year_data = data[data['release_year'] == year].copy()
    if year_data.empty:
        print(f"No data found for year {year}")
        return None

    X_year = year_data[feature_cols]
    y_pred = np.expm1(model.predict(X_year))

    year_data['predicted_revenue'] = y_pred
    if target_col in year_data.columns:
        year_data['actual_revenue'] = year_data[target_col]
        year_data['prediction_error'] = year_data['actual_revenue'] - year_data['predicted_revenue']
        year_data['prediction_error_pct'] = (
            year_data['prediction_error'] / year_data['actual_revenue']
        ) * 100

    top10 = year_data.nlargest(10, 'predicted_revenue')

    display_cols = ['title', 'predicted_revenue']
    if target_col in year_data.columns:
        display_cols.extend(['actual_revenue', 'prediction_error_pct'])

    additional_flags = [flag for flag in feature_flags if flag in top10.columns]
    display_cols.extend(additional_flags)

    return top10[display_cols].reset_index(drop=True)

