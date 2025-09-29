# =============================================================================
# DATASET CONFIGURATION - Add this cell to the top of notebooks 3-6
# =============================================================================

# Import the configuration system
import sys
from pathlib import Path
sys.path.insert(0, str(Path('../').resolve()))  # Add project root to path

from dataset_config import (
    DEFAULT_CONFIG, get_dataset_config, get_dataset_path, get_config_summary,
    use_full_dataset, use_english_only, use_major_studios, use_english_major
)

# =============================================================================
# EASY CONFIGURATION SWITCHING - Uncomment one of these to change scope
# =============================================================================

# CURRENT_CONFIG = use_full_dataset()                    # All studios, all languages (2010-2026)
# CURRENT_CONFIG = use_english_only(2010)                # English only (2010-2026)
# CURRENT_CONFIG = use_english_only(2015)                # English only (2015-2026)
# CURRENT_CONFIG = use_major_studios(2010)               # Major studios only (2010-2026)
# CURRENT_CONFIG = use_major_studios(2015)               # Major studios only (2015-2026)
# CURRENT_CONFIG = use_english_major(2010)               # English + Major studios (2010-2026)
# CURRENT_CONFIG = use_english_major(2015)               # English + Major studios (2015-2026)

# Use default if none specified above
CURRENT_CONFIG = DEFAULT_CONFIG

# =============================================================================
# DATASET LOADING FUNCTIONS - Use these in your notebook
# =============================================================================

def load_dataset(training=False):
    """Load the configured dataset subset."""
    import pandas as pd
    from movie_lists import normalize_domestic_titles

    dataset_path = get_dataset_path(training=training, config=CURRENT_CONFIG)
    dataset_config = get_dataset_config(CURRENT_CONFIG)

    print(f"📁 Loading dataset: {dataset_path}")
    print(get_config_summary(CURRENT_CONFIG))

    # Load data
    df = pd.read_csv(dataset_path)

    # Apply additional filtering if needed (for english_major scope)
    if dataset_config['scope'] == 'english_major':
        if 'is_major_studio' in df.columns:
            original_len = len(df)
            df = df[df['is_major_studio'] == 1].copy()
            print(f"   Filtered to major studios: {len(df):,} movies (removed {original_len - len(df):,})")

    # Normalize titles
    df = normalize_domestic_titles(df)

    print(f"   ✅ Loaded {len(df):,} movies")
    if 'release_year' in df.columns:
        print(f"   Year range: {df['release_year'].min()}-{df['release_year'].max()}")

        # Show breakdown by time period
        training_count = len(df[df['release_year'] <= 2023])
        test_2024_count = len(df[df['release_year'] == 2024])
        eval_2025_count = len(df[df['release_year'] == 2025])
        pred_2026_count = len(df[df['release_year'] == 2026])

        print(f"   Training (≤2023): {training_count:,} movies")
        if test_2024_count > 0:
            print(f"   Testing (2024): {test_2024_count:,} movies")
        if eval_2025_count > 0:
            print(f"   Evaluation (2025): {eval_2025_count:,} movies")
        if pred_2026_count > 0:
            print(f"   Prediction (2026): {pred_2026_count:,} movies")

    return df

def get_current_scope_info():
    """Get information about the current dataset scope."""
    return get_config_summary(CURRENT_CONFIG)

# =============================================================================
# SHOW CURRENT CONFIGURATION
# =============================================================================

print("🎯 CURRENT DATASET CONFIGURATION:")
print("=" * 50)
print(get_config_summary(CURRENT_CONFIG))
print("\n💡 To change scope, uncomment one of the CURRENT_CONFIG lines above")
print("   and restart the notebook kernel.\n")

# Quick scope switching examples
print("📝 QUICK SCOPE SWITCHING EXAMPLES:")
print("   CURRENT_CONFIG = use_full_dataset()          # All data")
print("   CURRENT_CONFIG = use_english_only(2015)      # English 2015-2026")
print("   CURRENT_CONFIG = use_major_studios(2010)     # Major studios 2010-2026")
print("   CURRENT_CONFIG = use_english_major(2015)     # English + Major 2015-2026")