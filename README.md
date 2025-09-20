# Box Office Prediction & Movie Analysis

A comprehensive data science project for analyzing movie performance and predicting box office success using multiple film industry datasets.

## 🎬 Project Overview

This project combines data from multiple sources to analyze movie performance patterns and build predictive models for box office success. The analysis focuses on movies from 2015 onwards with complete revenue and budget data.

## 📊 Datasets

The project integrates several major movie databases:

- **Box Office Data (1984-2024)**: Historical performance from BoxOfficeMojo
- **TMDB Dataset**: 930k+ movies with revenue, budget, cast, and crew data
- **IMDB Dataset**: Movie basics and ratings (11.9M entries, 1.6M ratings)

*Note: Large data files (>100MB) are stored locally and excluded from version control.*

## 🛠 Features

### Data Processing & Feature Engineering
- **Studio Detection**: Comprehensive mapping of major film studios and subsidiaries
- **Genre Analysis**: One-hot encoding of all unique genres in the dataset
- **Country/Language Flags**: Binary features for production countries and spoken languages
- **Franchise Detection**: Identification of major film franchises (Marvel, Star Wars, DC, etc.)
- **Sequel Indicators**: Pattern matching for sequels and series films

### Data Quality
- Filtered to movies with revenue > 0 and budget > 0
- Excluded adult films and documentaries from franchise analysis
- US/UK production focus for major franchise identification

## 📁 Project Structure

```
box_office/
├── code/
│   ├── dataset-exploration.ipynb    # Initial data exploration
│   └── feature-engineering.ipynb   # Feature engineering & analysis
├── data/                           # Large datasets (local only)
│   ├── *.csv                      # TMDB and box office data
│   └── *.tsv                      # IMDB data files
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- ~6GB disk space for datasets

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

3. **Download datasets** (not included in repo due to size):
   - TMDB movie datasets
   - IMDB title files
   - Box office data

4. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

## 📈 Analysis Highlights

- **371,040 movies** after filtering (adult films and zero revenue/budget removed)
- **Comprehensive genre analysis** with one-hot encoding for all unique genres
- **Major studio detection** for Disney, Warner Bros, Universal, Sony, Paramount, Fox, MGM, Lionsgate
- **Franchise identification** for Marvel, Star Wars, DC, Fast & Furious, Harry Potter
- **Revenue analysis** by studio, genre, country, and franchise status

## 🔧 Key Technologies

- **Python**: pandas, numpy, matplotlib, seaborn
- **Jupyter Notebooks**: Interactive analysis and visualization
- **Data Sources**: TMDB API, IMDB datasets, BoxOfficeMojo

## 📝 Notes

- Large data files are excluded from version control due to GitHub's 100MB limit
- The project focuses on theatrical releases with complete financial data
- Franchise detection is limited to US/UK productions to avoid false positives

## 🤝 Contributing

This is a personal data science project, but suggestions and improvements are welcome!

## 📄 License

This project is for educational and analysis purposes.