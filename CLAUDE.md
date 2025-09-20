# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a box office prediction and movie analysis project containing multiple movie datasets and a Jupyter notebook for exploration and modeling.

## Project Structure

```
box_office/
├── code/
│   └── box-office-prediction-exploration.ipynb  # Main analysis notebook
└── data/
    ├── boxoffice_data_2024.csv                  # Box office data 1984-2024
    ├── title.basics.tsv                         # IMDB movie basics (11.9M entries)
    ├── title.ratings.tsv                        # IMDB ratings (1.6M entries)
    ├── TMDB_all_movies.csv                      # TMDB comprehensive dataset
    └── TMDB_movie_dataset_v11.csv               # TMDB 930k movies dataset
```

## Data Sources

The project integrates multiple movie datasets:

1. **Box Office Data (1984-2024)**: Historical box office performance from BoxOfficeMojo
2. **IMDB Dataset**: Movie basics and ratings with 11.9M entries and 1.6M ratings
3. **TMDB Datasets**:
   - Comprehensive movie dataset with revenue, budget, cast, crew
   - 930k movies dataset with detailed metadata
   - API integration for fetching 2026 upcoming releases

## Development Environment

- **Primary Language**: Python
- **Main Tool**: Jupyter Notebook
- **Key Libraries**: pandas, numpy, requests, json
- **Data Format**: CSV and TSV files

## Setup and Installation

Install required dependencies:

```bash
# Install required Python packages
pip install -r requirements.txt

# Or install manually:
pip install pandas numpy requests jupyter matplotlib seaborn scikit-learn
```

## Running the Analysis

To run the main analysis notebook:

```bash
# Navigate to the code directory
cd code

# Start Jupyter notebook
jupyter notebook box-office-prediction-exploration.ipynb
```

## TMDB API Configuration

For fetching 2026 movie releases, set up TMDB API access:

1. Get API key from https://www.themoviedb.org/settings/api
2. Set environment variable: `export TMDB_API_KEY='your_key_here'`
3. Or create `config.json` in project root: `{"TMDB_API_KEY": "your_key_here"}`
4. Or create `.env` file: `TMDB_API_KEY=your_key_here`

## Data Processing Notes

- IMDB files use tab-separated format (.tsv)
- Box office data includes years 1984-2024 with gross revenue
- TMDB data includes revenue, budget, cast, crew, and metadata
- Memory usage for full dataset loading is approximately 6GB+
- The notebook includes data validation and linking between datasets

## Key Analysis Features

The main notebook demonstrates:
- Multi-dataset loading and integration
- Data exploration and validation
- Revenue and budget analysis capabilities
- IMDB ratings integration
- Future movie release fetching via TMDB API