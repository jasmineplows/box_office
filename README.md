# Box Office Prediction & Movie Analysis

This project aims to predict **US 2026 domestic box office** success.

## 🎬 Project Overview

The analysis combines **Box Office Mojo** lifetime domestic grosses with **TMDb metadata** to create a comprehensive dataset of English-language theatrical releases from 2015-2025.

## 📊 Current Datasets
- **Box Office Mojo**: All-time domestic grosses + distributor information
- **TMDb Integration**: Rich metadata (genres, cast, runtime, vote metrics)

## 🛠 Features

### Data Processing & Feature Engineering
- **Distributor Analysis**: Major studio classification based on Box Office Mojo distributors
- **Genre Processing**: TMDb genre ID to name mapping with one-hot encoding
- **Franchise Detection**: Marvel, Star Wars, DC, Fast & Furious identification with flexible pattern matching
- **Sequel Indicators**: Comprehensive pattern matching for franchise films
- **Remake Detection**: Disney live-action remakes, media adaptations, and reboot identification
- **Language Features**: English-language focus for domestic market relevance

### Data Quality & Filtering
- ✅ **Lifetime domestic focus**: Box Office Mojo all-time domestic grosses
- ✅ **Content filtering**: Removes TV shows, documentaries, non-English films
- ✅ **Theatrical releases**: Focus on movies with significant domestic box office
- ✅ **Distributor integration**: Enhanced with year-by-year distributor data

## 📁 Project Structure

```
box_office/
├── code/
│   ├── 1.get-data.ipynb                     # Data collection & merging
│   ├── 2.feature-engineering.ipynb         # Advanced feature engineering & visualization
│   └── movie_lists.py                      # Curated movie lists for IP detection
├── data/
│   ├── boxoffice_alltime_domestic.csv       # Box Office Mojo domestic data
│   ├── tmdb_filtered.csv                    # TMDb movie metadata
│   ├── dataset_domestic_lifetime_merged.csv # Merged raw dataset
│   └── dataset_domestic_processed.csv       # Final processed dataset (67 features)
├── config.json                             # TMDb API configuration
└── README.md                              # This documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- TMDb API key (v3 or v4 token)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jasmineplows/box_office.git
   cd box_office
   ```

2. **Set up TMDb API:**
   ```bash
   # Create config.json with your TMDb API key
   {
     "TMDB_API_KEY": "your_api_key_here"
   }
   ```

3. **Run the analysis:**
   ```bash
   jupyter notebook code/1.get-data.ipynb      # Data collection
   jupyter notebook code/2.feature-engineering.ipynb  # Feature creation
   ```

### Data Pipeline

1. **Collection**: `1.get-data.ipynb` scrapes Box Office Mojo + fetches TMDb data
2. **Merging**: Intelligent exact + fuzzy matching with distributor integration
3. **Feature Engineering**: `2.feature-engineering.ipynb` creates 67 features with advanced IP detection
4. **Visualization**: Interactive charts showing studio, genre, and IP performance trends by year

## 📈 Analysis Highlights

- **1,532 movies** with complete lifetime domestic revenue data (2015-2025)
- **67 engineered features** including studio flags, genre encoding, and IP detection
- **Comprehensive IP analysis** covering franchises, remakes, adaptations, and superhero films
- **Interactive visualizations** showing performance trends by year across studios, genres, and IP categories
- **Advanced pattern matching** for flexible franchise and remake identification
- **Revenue analysis** focused on lifetime US domestic market performance


## 🔄 Data Updates

The project automatically scrapes fresh data:

```bash
# Re-run data collection (updates Box Office Mojo + TMDb data)
jupyter notebook code/1.get-data.ipynb

# Set FORCE_REFRESH = True in notebook to bypass cache
```

## 📊 Key Performance Insights

### IP vs Original Content
- **IP movies** represent ~9% of releases but generate disproportionate revenue
- **IP advantage**: IP movies earn significantly more on average than original content
- **Superhero dominance**: 63 superhero movies show 400%+ revenue advantage over non-superhero films
- **Live-action remake success**: Disney/DreamWorks remakes show 360%+ advantage over non-remakes

### Studio & Genre Trends
- **Disney dominance**: Walt Disney Studios leads in average revenue per movie
- **Action/Adventure**: Consistently highest-grossing primary genres
- **Franchise concentration**: Marvel (26 films), DC (13 films), and Star Wars (5 films) drive major revenue
- **Year-over-year evolution**: Clear trends in studio market share and genre preferences (2015-2025)

### Market Evolution
- **IP percentage trends**: Analysis shows changing reliance on established intellectual properties
- **Studio competition**: Visualization reveals shifting dominance between major distributors
- **Genre performance**: Clear patterns in which genres dominate domestic box office by year