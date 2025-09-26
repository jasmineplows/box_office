"""Shared utilities for box office modeling notebooks.

This module consolidates common feature-preparation, evaluation, and
reporting helpers so that the notebooks stay focused on exploratory
work without duplicating logic.
"""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
import pandas as pd
from scipy.stats import kendalltau, spearmanr
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
    'is_live_action_remake', 'is_major_studio', 'is_disney',
    'is_english', 'is_origin_usa', 'is_origin_uk_ie', 'is_origin_canada', 'is_origin_us_uk_ca'
)


def prepare_features(
    df: pd.DataFrame,
    *,
    target: str = 'revenue_domestic',
    exclude_cols: Optional[Sequence[str]] = None,
    filter_major_only: bool = False,
    drop_major_flag_from_features: bool = False,
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
        the returned feature list (useful when you manually filter majors elsewhere).
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


def log_results_to_mlflow(
    results: Dict[str, Any],
    *,
    run_name: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    tags: Optional[Dict[str, Any]] = None,
    model: Optional[Any] = None,
    model_type: str = 'sklearn',
    validation_frame: Optional[pd.DataFrame] = None,
    prediction_artifact_name: str = 'validation_predictions.csv',
    artifacts: Optional[Dict[str, Union[str, Path]]] = None,
    extra_metrics: Optional[Dict[str, float]] = None,
    feature_frame: Optional[pd.DataFrame] = None,
    input_example_rows: int = 10,
    dataset_major_only: Optional[bool] = None,
    dataset_english_only: Optional[bool] = None,
) -> None:
    """Log ``results`` from :func:`evaluate_model` to MLflow."""

    try:
        import mlflow
        from mlflow import sklearn as mlflow_sklearn
        from mlflow.models import infer_signature
    except ImportError as exc:  # pragma: no cover - only triggered when mlflow missing
        raise RuntimeError(
            "mlflow is not installed. Add it to requirements.txt and pip install mlflow."
        ) from exc

    resolved_run_name = run_name or results.get('model_name') or 'model-run'

    with mlflow.start_run(run_name=resolved_run_name):
        derived_params: Dict[str, Any] = {}
        if dataset_major_only is not None:
            derived_params['data_scope_studios'] = 'major_only' if dataset_major_only else 'all_studios'
        if dataset_english_only is not None:
            derived_params['data_scope_language'] = 'english_only' if dataset_english_only else 'all_languages'

        if params or derived_params:
            sanitized_params: Dict[str, Any] = {}
            for key, value in {**derived_params, **(params or {})}.items():
                if isinstance(value, (str, int, float, bool)) or value is None:
                    sanitized_params[key] = value
                else:
                    sanitized_params[key] = str(value)
            if sanitized_params:
                mlflow.log_params(sanitized_params)

        derived_tags: Dict[str, str] = {}
        if dataset_major_only is not None:
            derived_tags['dataset.studio_scope'] = 'major_only' if dataset_major_only else 'all_studios'
        if dataset_english_only is not None:
            derived_tags['dataset.language_scope'] = 'english_only' if dataset_english_only else 'all_languages'

        if tags or derived_tags:
            sanitized_tags = {key: (str(value) if value is not None else '') for key, value in {**derived_tags, **(tags or {})}.items()}
            mlflow.set_tags(sanitized_tags)

        core_metrics = {
            key: float(results[key])
            for key in ('rmse', 'mae', 'mape', 'r2')
            if key in results and results[key] is not None
        }
        if extra_metrics:
            core_metrics.update({key: float(value) for key, value in extra_metrics.items()})
        if core_metrics:
            mlflow.log_metrics(core_metrics)

        model_to_log = model or results.get('model_object')
        signature = None
        input_example_df = None
        feature_sample = None
        if feature_frame is not None:
            feature_frame = feature_frame.reset_index(drop=True).copy()
            if input_example_rows > 0:
                input_example_df = feature_frame.head(input_example_rows).reset_index(drop=True)
            # Use at most 500 rows for signature inference to balance fidelity and size.
            sample_rows = min(len(feature_frame), max(input_example_rows, 500))
            if sample_rows > 0:
                feature_sample = feature_frame.head(sample_rows)

        if feature_sample is not None and model_to_log is not None:
            try:
                preds_for_signature = model_to_log.predict(feature_sample)
                signature = infer_signature(feature_sample, preds_for_signature)
            except Exception:
                signature = None

        if model_to_log is not None:
            # ``artifact_path`` was renamed to ``name`` in newer MLflow versions.
            sklearn_params = mlflow_sklearn.log_model.__code__.co_varnames
            sklearn_path_kw = 'name' if 'name' in sklearn_params else 'artifact_path'
            pyfunc_params = mlflow.pyfunc.log_model.__code__.co_varnames
            pyfunc_path_kw = 'name' if 'name' in pyfunc_params else 'artifact_path'

            if model_type == 'sklearn':
                mlflow_sklearn.log_model(
                    model_to_log,
                    **{sklearn_path_kw: 'model'},
                    signature=signature,
                    input_example=input_example_df,
                )
            else:
                mlflow.pyfunc.log_model(
                    python_model=model_to_log,
                    **{pyfunc_path_kw: 'model'},
                    signature=signature,
                    input_example=input_example_df,
                )

        if validation_frame is not None and 'predictions' in results:
            predictions = np.asarray(results['predictions'])
            if len(predictions) == len(validation_frame):
                temp_df = validation_frame.copy()
                temp_df['predicted'] = predictions
                with tempfile.TemporaryDirectory() as tmpdir:
                    temp_path = Path(tmpdir) / prediction_artifact_name
                    temp_df.to_csv(temp_path, index=False)
                    mlflow.log_artifact(str(temp_path), artifact_path='predictions')

    if artifacts:
        for name, location in artifacts.items():
            path_obj = Path(location)
            if path_obj.exists():
                mlflow.log_artifact(str(path_obj), artifact_path=str(name))


def calculate_top_k_overlap(
    validation_frame: Optional[pd.DataFrame],
    predictions: Optional[Sequence[float]],
    *,
    target_col: str,
    title_col: str = 'title',
    k: int = 10,
) -> Optional[int]:
    """Return the overlap count between actual and predicted top ``k`` titles."""

    metrics = compute_ranking_metrics(
        validation_frame,
        predictions,
        target_col=target_col,
        title_col=title_col,
        k=k,
    )
    if not metrics:
        return None
    return int(metrics.get('top10_overlap')) if metrics.get('top10_overlap') is not None else None


def _dcg(scores: np.ndarray) -> float:
    if scores.size == 0:
        return 0.0
    discounts = np.log2(np.arange(2, scores.size + 2))
    return float(np.sum(scores / discounts))


def compute_ranking_metrics(
    validation_frame: Optional[pd.DataFrame],
    predictions: Optional[Sequence[float]],
    *,
    target_col: str,
    title_col: str = 'title',
    k: int = 10,
) -> Dict[str, float]:
    """Return ranking-quality metrics comparing predictions to ``target_col``."""

    if validation_frame is None or predictions is None:
        return {}
    if title_col not in validation_frame.columns or target_col not in validation_frame.columns:
        return {}

    preds = np.asarray(predictions, dtype=float)
    if len(preds) != len(validation_frame):
        return {}

    working = validation_frame[[title_col, target_col]].copy()
    working['predicted'] = preds
    working = working.dropna(subset=[title_col, target_col])
    if working.empty:
        return {}

    actual_sorted = working.sort_values(target_col, ascending=False)
    predicted_sorted = working.sort_values('predicted', ascending=False)

    k_actual = min(k, len(actual_sorted))
    k_pred = min(k, len(predicted_sorted))
    actual_top_titles = actual_sorted.head(k_actual)[title_col].astype(str).tolist()
    predicted_top_titles = predicted_sorted.head(k_pred)[title_col].astype(str).tolist()
    overlap = len(set(actual_top_titles) & set(predicted_top_titles))
    recall = overlap / k_actual if k_actual > 0 else np.nan

    # Normalised DCG@k (using scaled actual revenue as gain)
    actual_gains = actual_sorted[target_col].to_numpy(dtype=float)
    max_gain = float(np.nanmax(actual_gains)) if actual_gains.size else 0.0
    if not np.isfinite(max_gain) or max_gain <= 0:
        max_gain = 1.0
    pred_gains = predicted_sorted.head(k_pred)[target_col].to_numpy(dtype=float) / max_gain
    ideal_gains = actual_sorted.head(k_actual)[target_col].to_numpy(dtype=float) / max_gain
    dcg_pred = _dcg(pred_gains)
    dcg_ideal = _dcg(ideal_gains)
    ndcg = dcg_pred / dcg_ideal if dcg_ideal > 0 else np.nan

    # Rank correlations on full validation set
    if working[target_col].nunique() <= 1 or working['predicted'].nunique() <= 1:
        spearman = np.nan
        kendall = np.nan
    else:
        spearman_res = spearmanr(working[target_col], working['predicted'])
        kendall_res = kendalltau(working[target_col], working['predicted'])
        spearman = getattr(spearman_res, 'statistic', None)
        if spearman is None:
            spearman = spearman_res[0] if isinstance(spearman_res, (tuple, list)) else spearman_res
        kendall = getattr(kendall_res, 'statistic', None)
        if kendall is None:
            kendall = kendall_res[0] if isinstance(kendall_res, (tuple, list)) else kendall_res

    precision = overlap / k_pred if k_pred > 0 else np.nan

    metrics = {
        'top10_overlap': float(overlap),
        'recall_at_10': float(recall) if np.isfinite(recall) else None,
        'precision_at_10': float(precision) if np.isfinite(precision) else None,
        'ndcg_at_10': float(ndcg) if np.isfinite(ndcg) else None,
        'spearman_corr': float(spearman) if np.isfinite(spearman) else None,
        'kendall_corr': float(kendall) if np.isfinite(kendall) else None,
    }

    return {key: value for key, value in metrics.items() if value is not None}
