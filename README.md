# Box Office Prediction & Movie Analysis

A data science project for predicting **US domestic box office** success using machine learning.

## 🎬 Project Overview

This project analyzes movie performance patterns and builds predictive models for **US domestic** box office success. The analysis focuses on English-speaking movies from 2015 onwards with complete domestic revenue and budget data.

**🎯 Key Feature: Uses actual US domestic box office revenue (not worldwide) for accurate US market predictions.**

## 📊 Current Dataset

- **820 movies** (2015-2024) with complete domestic revenue data
- **Enhanced box office data** from multiple sources with domestic + worldwide revenue
- **Comprehensive metadata** from TMDB (production companies, genres, cast, crew)
- **Verified accuracy**: Star Wars Force Awakens shows $858M domestic (not $2.07B worldwide)

### Top US Domestic Performers (2015-2024):
1. **Avengers: Endgame** - $858.4M domestic
2. **Spider-Man: No Way Home** - $804.8M domestic
3. **Top Gun: Maverick** - $718.7M domestic
4. **Black Panther** - $700.1M domestic
5. **Avatar: The Way of Water** - $684.1M domestic

## 🛠 Features

### Data Processing & Feature Engineering
- **Studio Detection**: Hierarchical classification (major vs mid-tier studios)
- **Genre Analysis**: One-hot encoding of all movie genres
- **Country/Language Flags**: Production origin and language features
- **Franchise Detection**: Marvel, Star Wars, DC, Fast & Furious identification
- **Sequel Indicators**: Pattern matching for franchise films

### Data Quality & Filtering
- ✅ **Domestic revenue focus**: US theatrical box office only
- ✅ **Content filtering**: Removes TV shows, TV movies, streaming-first releases
- ✅ **English language**: Focus on US market-relevant films
- ✅ **Quality threshold**: Movies with meaningful budget and revenue data

## 📁 Project Structure

```
box_office/
├── code/
│   ├── domestic-data-integration.ipynb    # Creates domestic dataset
│   └── feature-engineering.ipynb         # Analysis & feature creation
├── data/
│   ├── enhanced_box_office_data(2000-2024)u.csv  # Source domestic data
│   ├── TMDB_movie_dataset_v11.csv               # Movie metadata
│   ├── dataset_domestic.csv                     # Clean domestic dataset
│   └── title.*.tsv                              # IMDB ratings/info
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Kaggle API (for data updates)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jasmineplows/box_office.git
   cd box_office
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start analysis:**
   ```bash
   jupyter notebook code/feature-engineering.ipynb
   ```

### Data Pipeline

1. **Source**: Enhanced box office dataset with verified domestic revenue
2. **Integration**: Merge with TMDB metadata via `domestic-data-integration.ipynb`
3. **Analysis**: Feature engineering and modeling via `feature-engineering.ipynb`

## 📈 Analysis Highlights

- **820 movies** with complete domestic revenue data (2015-2024)
- **Comprehensive studio analysis** with major + mid-tier classification
- **Genre analysis** with one-hot encoding for all unique genres
- **Franchise identification** for Marvel, Star Wars, DC, and major series
- **Revenue analysis** focused on US domestic market performance

### Studio Performance (Average Domestic Revenue):
- **Disney**: Highest average domestic revenue
- **Warner Bros**: Strong consistent performance
- **Universal**: Major franchise success
- **Sony**: Solid mid-tier performance

## 🎯 Why Domestic Revenue Matters

Using **US domestic box office** instead of worldwide revenue provides:

- ✅ **Accurate US predictions**: Relevant for US theatrical decisions
- ✅ **Market-specific insights**: US audience preferences and behavior
- ✅ **Comparable metrics**: Consistent currency and market conditions
- ✅ **Strategic relevance**: US is the primary theatrical market for most studios

## 🔄 Data Updates

The project uses Kaggle API for dataset updates:

```bash
# Update domestic box office data
kaggle datasets download -d aditya126/movies-box-office-dataset-2000-2024

# Re-run integration
jupyter notebook code/domestic-data-integration.ipynb
```

## 📊 Key Insights

- **Franchise films** dominate top domestic revenue
- **Disney/Marvel** leads in average revenue per film
- **Domestic vs Worldwide**: US typically represents 30-45% of global revenue
- **Genre trends**: Action/Adventure and Sci-Fi perform best domestically

---

**Built for accurate US domestic box office prediction** 🎬📊