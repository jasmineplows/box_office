# Dataset Configuration System

This system makes it easy to switch between different dataset subsets across all notebooks (3-6) without manually changing file paths.

## Quick Start

### 1. In any notebook (3-6), add the configuration cell at the top:

```python
# =============================================================================
# DATASET CONFIGURATION - Easy switching between dataset subsets
# =============================================================================

import sys
from pathlib import Path
sys.path.insert(0, str(Path('../').resolve()))

from dataset_config import (
    DEFAULT_CONFIG, get_dataset_config, get_dataset_path, get_config_summary,
    use_full_dataset, use_english_only, use_major_studios, use_english_major
)

# =============================================================================
# CHOOSE YOUR DATASET SCOPE - Uncomment one line to switch
# =============================================================================

# CURRENT_CONFIG = use_full_dataset()                    # All studios, all languages (2010-2026)
# CURRENT_CONFIG = use_english_only(2010)                # English only (2010-2026)
# CURRENT_CONFIG = use_english_only(2015)                # English only (2015-2026)
# CURRENT_CONFIG = use_major_studios(2010)               # Major studios only (2010-2026)
# CURRENT_CONFIG = use_major_studios(2015)               # Major studios only (2015-2026)
# CURRENT_CONFIG = use_english_major(2010)               # English + Major studios (2010-2026)
# CURRENT_CONFIG = use_english_major(2015)               # English + Major studios (2015-2026)

CURRENT_CONFIG = DEFAULT_CONFIG  # Use default (full dataset)

print("🎯 DATASET CONFIGURATION:")
print("=" * 50)
print(get_config_summary(CURRENT_CONFIG))
```

### 2. Replace your data loading code with:

```python
# Load dataset using configuration system
def load_dataset(training=False):
    """Load the configured dataset subset."""
    import pandas as pd
    from movie_lists import normalize_domestic_titles

    dataset_path = get_dataset_path(training=training, config=CURRENT_CONFIG)
    dataset_config = get_dataset_config(CURRENT_CONFIG)

    print(f"📁 Loading dataset: {dataset_path}")

    df = pd.read_csv(dataset_path)

    # Apply additional filtering if needed (for english_major scope)
    if dataset_config['scope'] == 'english_major':
        if 'is_major_studio' in df.columns:
            original_len = len(df)
            df = df[df['is_major_studio'] == 1].copy()
            print(f"   Filtered to major studios: {len(df):,} movies")

    df = normalize_domestic_titles(df)
    print(f"   ✅ Loaded {len(df):,} movies")

    return df

# Load the dataset
df = load_dataset(training=False)  # Use training=True for training data only
```

## Available Dataset Subsets

| Scope | Description | Files | Training Movies | Total Movies |
|-------|-------------|-------|----------------|--------------|
| `full` | All studios, all languages | `dataset_domestic_processed.csv` | 1,994 | 2,339 |
| `english` | English movies only | `dataset_domestic_processed_english_{year}_2026.csv` | 1,646 (2010) / 1,003 (2015) | 2,009 (2010) / 1,307 (2015) |
| `major` | Major studios only | `dataset_domestic_processed_major_{year}_2026.csv` | 1,053 (2010) / 643 (2015) | 1,274 (2010) / 802 (2015) |
| `english_major` | English + Major studios | Uses English subset + filtering | ~800-1,000 | ~1,000-1,600 |

## How to Switch Datasets

### Option 1: Quick Switch
Just uncomment one of the `CURRENT_CONFIG` lines in the configuration cell:

```python
# CURRENT_CONFIG = use_english_only(2015)     # Switch to English 2015-2026
CURRENT_CONFIG = use_major_studios(2010)      # Switch to Major studios 2010-2026
```

### Option 2: Custom Configuration
```python
CURRENT_CONFIG = {
    'scope': 'english',
    'year_start': 2015,
    'data_dir': '../data',
    'force_full_validation': True  # Use full dataset for validation even if scope is limited
}
```

## Effects on Different Notebooks

- **Notebook 3 (LLM Validation)**: Validates only the specified subset
- **Notebook 5 (Model Training)**: Trains on the specified subset
- **Notebook 6 (Model Comparison)**: Loads models trained on the specified subset

## Benefits

1. **Consistency**: All notebooks use the same dataset subset automatically
2. **Easy Switching**: Change one line to switch scope across all notebooks
3. **Clear Documentation**: Always shows which subset is being used
4. **Experimentation**: Easy to test different scopes and year ranges
5. **No Manual Path Changes**: Automatically handles file paths and filtering

## Example Workflow

1. **Development**: Use `english_only(2015)` for faster iteration
2. **Full Training**: Switch to `full` dataset for final models
3. **Major Studio Analysis**: Use `major` scope for studio-specific insights
4. **English Market Focus**: Use `english_major(2010)` for English-speaking market analysis

## Files Created

- `dataset_config.py`: Main configuration system
- `dataset_config_cell.py`: Template cell for notebooks
- `DATASET_CONFIG_README.md`: This documentation

The system automatically saves configuration to `data/current_dataset_config.json` for sharing across notebooks.