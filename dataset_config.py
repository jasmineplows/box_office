"""
Dataset Configuration System for Box Office Prediction Project

This module provides easy configuration for switching between different dataset subsets
across all notebooks (3-6). Simply change the DEFAULT_CONFIG to use different scopes.

Available Dataset Subsets:
- Full dataset: All studios, all languages (2010-2026)
- English-only: English movies only (2010-2026 or 2015-2026)
- Major studios: Only major studios (2010-2026 or 2015-2026)
- Combined: English + Major studios (2010-2026 or 2015-2026)
"""

from pathlib import Path
import json
from typing import Optional, Dict

import pandas as pd

try:
    from movie_lists import normalize_domestic_titles
except ImportError:  # pragma: no cover
    normalize_domestic_titles = None

# =============================================================================
# MAIN CONFIGURATION - Change this to switch dataset scope for all notebooks
# =============================================================================

DEFAULT_CONFIG = {
    # Dataset scope settings
    'scope': 'full',          # Options: 'full', 'english', 'major', 'english_major'
    'year_start': 2010,       # Options: 2010, 2015

    # Advanced settings (usually don't need to change)
    'data_dir': '../data',
    'force_full_validation': False,  # Use full dataset for validation even if scope is limited
}

# =============================================================================
# Dataset Subset Definitions
# =============================================================================

DATASET_CONFIGS = {
    'full': {
        'name': 'Full Dataset',
        'description': 'All studios, all languages',
        'filename_pattern': 'dataset_domestic_processed.csv',
        'training_filename_pattern': 'dataset_domestic_processed_modeling.csv',
        'filter_english': False,
        'filter_major': False,
    },

    'english': {
        'name': 'English Only',
        'description': 'English movies only',
        'filename_pattern': 'dataset_domestic_processed_english_{year_start}_2026.csv',
        'training_filename_pattern': 'dataset_domestic_processed_english_{year_start}_2026.csv',
        'filter_english': True,
        'filter_major': False,
    },

    'major': {
        'name': 'Major Studios',
        'description': 'Major studios only',
        'filename_pattern': 'dataset_domestic_processed_major_{year_start}_2026.csv',
        'training_filename_pattern': 'dataset_domestic_processed_major_{year_start}_2026.csv',
        'filter_english': False,
        'filter_major': True,
    },

    'english_major': {
        'name': 'English + Major Studios',
        'description': 'English movies from major studios only',
        'filename_pattern': 'dataset_domestic_processed_english_{year_start}_2026.csv',  # Use English subset
        'training_filename_pattern': 'dataset_domestic_processed_english_{year_start}_2026.csv',
        'filter_english': True,
        'filter_major': True,  # Apply major studio filter on top
    }
}

# =============================================================================
# Helper Functions
# =============================================================================

def get_dataset_config(config=None):
    """Get the current dataset configuration."""
    if config is None:
        config = DEFAULT_CONFIG.copy()

    scope = config['scope']
    year_start = config['year_start']

    if scope not in DATASET_CONFIGS:
        raise ValueError(f"Unknown scope '{scope}'. Available: {list(DATASET_CONFIGS.keys())}")

    dataset_config = DATASET_CONFIGS[scope].copy()

    # Format filename patterns with year_start
    if '{year_start}' in dataset_config['filename_pattern']:
        dataset_config['filename_pattern'] = dataset_config['filename_pattern'].format(year_start=year_start)

    if '{year_start}' in dataset_config['training_filename_pattern']:
        dataset_config['training_filename_pattern'] = dataset_config['training_filename_pattern'].format(year_start=year_start)

    # Add computed fields
    dataset_config['scope'] = scope
    dataset_config['year_start'] = year_start
    dataset_config['data_dir'] = config['data_dir']
    dataset_config['force_full_validation'] = config.get('force_full_validation', False)

    return dataset_config

def get_dataset_path(training=False, config=None):
    """Get the path to the dataset file based on current configuration."""
    dataset_config = get_dataset_config(config)
    data_dir = Path(dataset_config['data_dir'])

    if training:
        filename = dataset_config['training_filename_pattern']
    else:
        # For validation/testing, use full dataset if force_full_validation is True
        if dataset_config['force_full_validation'] and dataset_config['scope'] != 'full':
            filename = 'dataset_domestic_processed.csv'
        else:
            filename = dataset_config['filename_pattern']

    return data_dir / filename

def get_config_summary(config=None):
    """Get a human-readable summary of the current configuration."""
    dataset_config = get_dataset_config(config)

    summary = f"📊 Dataset Configuration: {dataset_config['name']}\n"
    summary += f"   Description: {dataset_config['description']}\n"
    summary += f"   Year range: {dataset_config['year_start']}-2026\n"
    summary += f"   Training file: {dataset_config['training_filename_pattern']}\n"
    summary += f"   Full file: {dataset_config['filename_pattern']}\n"

    if dataset_config['force_full_validation']:
        summary += f"   ⚠️ Using full dataset for validation (force_full_validation=True)\n"

    return summary


def build_scope_config(language_scope: str, studio_scope: str, year_start: int, data_dir: str = '../data') -> Dict[str, any]:
    """Derive a dataset configuration dict from scope strings."""
    language_scope = (language_scope or 'all_languages').lower()
    studio_scope = (studio_scope or 'all_studios').lower()

    if studio_scope == 'all_studios' and language_scope == 'all_languages':
        scope_key = 'full'
    elif studio_scope == 'all_studios' and language_scope.startswith('english'):
        scope_key = 'english'
    elif studio_scope == 'major_only' and language_scope == 'all_languages':
        scope_key = 'major'
    else:
        scope_key = 'english_major'

    return {
        'scope': scope_key,
        'year_start': int(year_start or 2010),
        'data_dir': data_dir,
    }


def load_dataset_frame(config: Optional[Dict[str, any]] = None, *, training: bool = False, verbose: bool = True) -> pd.DataFrame:
    """Load the unified dataset and apply filters based on ``config``."""

    dataset_config = get_dataset_config(config)
    data_dir = Path(dataset_config['data_dir'])
    base_path = data_dir / 'dataset_domestic_processed.csv'
    if not base_path.exists():
        raise FileNotFoundError(f"Base dataset not found: {base_path}")

    df = pd.read_csv(base_path)
    if normalize_domestic_titles is not None:
        df = normalize_domestic_titles(df)

    start_year = dataset_config['year_start']
    if 'release_year' in df.columns:
        df = df[df['release_year'].between(start_year, 2026, inclusive='both')]

    if training and 'release_year' in df.columns:
        df = df[df['release_year'] <= 2023]

    if dataset_config.get('filter_english') and 'original_language' in df.columns:
        df = df[df['original_language'].fillna('').str.lower() == 'en']

    if dataset_config.get('filter_major') and 'is_major_studio' in df.columns:
        df = df[df['is_major_studio'] == 1]

    if verbose:
        total = len(df)
        year_min = df['release_year'].min() if 'release_year' in df.columns else 'n/a'
        year_max = df['release_year'].max() if 'release_year' in df.columns else 'n/a'
        print(f"📁 Loaded dataset ({dataset_config['name']}): {total:,} rows | Years {year_min}-{year_max}")

    return df

def save_config_to_file(config=None, filepath=None):
    """Save current configuration to a JSON file for sharing across notebooks."""
    if config is None:
        config = DEFAULT_CONFIG.copy()

    if filepath is None:
        filepath = Path('../data/current_dataset_config.json')

    with open(filepath, 'w') as f:
        json.dump(config, f, indent=2)

    return filepath

def load_config_from_file(filepath=None):
    """Load configuration from a JSON file."""
    if filepath is None:
        filepath = Path('../data/current_dataset_config.json')

    if not Path(filepath).exists():
        return DEFAULT_CONFIG.copy()

    with open(filepath, 'r') as f:
        config = json.load(f)

    # Merge with defaults to ensure all keys exist
    full_config = DEFAULT_CONFIG.copy()
    full_config.update(config)

    return full_config

# =============================================================================
# Quick Configuration Examples
# =============================================================================

def use_full_dataset():
    """Quick function to switch to full dataset."""
    return {'scope': 'full', 'year_start': 2010, 'data_dir': '../data'}

def use_english_only(year_start=2010):
    """Quick function to switch to English-only dataset."""
    return {'scope': 'english', 'year_start': year_start, 'data_dir': '../data'}

def use_major_studios(year_start=2010):
    """Quick function to switch to major studios dataset."""
    return {'scope': 'major', 'year_start': year_start, 'data_dir': '../data'}

def use_english_major(year_start=2010):
    """Quick function to switch to English + major studios dataset."""
    return {'scope': 'english_major', 'year_start': year_start, 'data_dir': '../data'}

# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    # Print current configuration
    print(get_config_summary())

    # Example: Switch to English-only from 2015
    english_config = use_english_only(2015)
    print("\nSwitching to English-only (2015-2026):")
    print(get_config_summary(english_config))

    # Example: Get dataset paths
    training_path = get_dataset_path(training=True)
    full_path = get_dataset_path(training=False)
    print(f"\nDataset paths:")
    print(f"Training: {training_path}")
    print(f"Full: {full_path}")
