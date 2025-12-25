# =============================================================================
# DATASET CONFIGURATION - Add this cell to the top of notebooks 3-6
# =============================================================================

# Import the configuration system
import sys
from pathlib import Path
sys.path.insert(0, str(Path('../').resolve()))  # Add project root to path

from dataset_config import (
    DEFAULT_CONFIG, get_dataset_config, get_dataset_path, get_config_summary,
    load_dataset_frame,
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
    """Load the configured dataset subset via the shared loader."""
    df = load_dataset_frame(CURRENT_CONFIG, training=training, verbose=True)
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
