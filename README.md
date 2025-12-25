# Box Office Prediction & Movie Analysis

This project predicts **US 2026 domestic box office** success using machine learning models trained on comprehensive movie data from 2010-2025.

## 🎬 Project Overview

The analysis combines **Box Office Mojo** lifetime domestic grosses with **TMDb metadata** to create a comprehensive dataset for predicting theatrical success. The project includes multiple machine learning models with the best achieving **80% recall** for identifying top-performing movies.

## 📊 Current Status

### 🏆 Best Model Performance
- **Model**: LightGBM Regressor (No Pandemic Era)
- **Dataset**: English-only movies (2015-2026)
- **Performance**: 80% Recall@10, RMSE $78.9M, R² 0.472
- **Training**: 1,003 movies (2015-2023), Testing: 145 movies (2024)

### 📈 Datasets Available
- **2,339 total movies** across multiple dataset configurations
- **Training datasets**: 2015-2023 (prevents data leakage)
- **Test set**: 169 movies from 2024
- **Evaluation set**: 128 movies from 2025
- **Prediction target**: 48 movies for 2026

## 🛠 Features & Model Architecture

### 68 Engineered Features Across 8 Categories:

#### **Studio Features (9 features)**
- Major studio classification: Disney, Warner Bros, Universal, Sony, Paramount, Fox, MGM, Lionsgate
- `is_major_studio` aggregate flag

#### **Genre Features (18 features)**
- Individual genre flags: Action, Adventure, Animation, Comedy, Crime, Drama, Family, Fantasy, History, Horror, Music, Mystery, Romance, Sci-Fi, Thriller, War, Western
- `genre_count` - number of genres per movie

#### **IP & Franchise Features (12 features)**
- Franchise detection: Marvel MCU, DC, Star Wars, Fast & Furious, Harry Potter
- Content type flags: Sequels, live-action remakes, media adaptations, superhero films
- `is_ip_movie` comprehensive IP indicator

#### **Release Timing Features (10 features)**
- Seasonal indicators: Summer blockbuster, holiday release, Oscar season
- Holiday proximity: Christmas, Thanksgiving, Independence Day, Memorial/Labor Day
- `release_month` and `days_to_holiday`

#### **Competition Features (5 features)**
- Nearby major releases within ±14 days
- Blockbuster competition ($200M+ movies)
- Competition intensity and immediate competition flags

#### **Origin & Language Features (5 features)**
- Production country indicators: US, UK/Ireland, Canada
- English language classification

#### **Time & Era Features (5 features)**
- `years_since_baseline` (2010 baseline)
- Era classification: Pre-streaming, streaming transition, pandemic, post-pandemic

#### **Other Features (1 feature)**
- Remake indicator patterns in titles

## 📁 Project Structure

```
box_office/
├── code/
│   ├── 1_get_data.ipynb                         # Data collection & merging
│   ├── 2_feature_engineering.ipynb             # 68-feature engineering pipeline
│   ├── 3_llm_feature_validation.ipynb          # LLM-assisted feature validation
│   ├── 4_train_models.ipynb                    # Model training & evaluation
│   ├── 5_try_different_modeling_approaches.ipynb # Alternative modeling experiments
│   ├── 6_final_model_comparison.ipynb          # Model comparison & validation
│   ├── 7_2026_predictions.ipynb                # 2026 box office predictions
│   ├── 8_2025_predictions.ipynb                # 2025 box office predictions
│   ├── movie_lists.py                          # Curated IP detection lists
│   ├── model_utils.py                          # Shared modeling utilities
│   └── dataset_config.py                       # Dataset configuration system
├── data/
│   ├── boxoffice_alltime_domestic.csv           # Box Office Mojo scraped data
│   ├── tmdb_filtered.csv                       # TMDb API movie metadata
│   ├── dataset_domestic_processed.csv          # Full dataset (2010-2026)
│   ├── dataset_domestic_processed_english_2015_2026.csv # Best model training set
│   ├── dataset_domestic_processed_english_2010_2026.csv # Alternative English set
│   ├── dataset_domestic_processed_major_*.csv   # Major studio subsets
│   └── matched_2026_movies.csv                 # 2026 prediction targets
├── mlruns/                                     # MLflow experiment tracking
├── backfill_mlflow_start_year.py              # MLflow metadata backfill utility
├── CLAUDE.md                                   # Technical implementation guidelines
└── README.md                                   # This documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- MLflow for experiment tracking
- TMDb API key (for data updates)

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

3. **Set up TMDb API (for data updates):**
   ```bash
   # Create config.json with your TMDb API key
   {
     "TMDB_API_KEY": "your_api_key_here"
   }
   ```

### Running the Analysis

1. **Feature Engineering**: `2_feature_engineering.ipynb` - Creates the 68-feature dataset
2. **Model Training**: `4_train_models.ipynb` - Trains and evaluates multiple models
3. **Model Comparison**: `6_final_model_comparison.ipynb` - Validates best model on 2024 data
4. **Predictions**: `7_2026_predictions.ipynb` - Generates 2026 box office predictions

### Data Pipeline

1. **Collection**: Box Office Mojo scraping + TMDb API integration
2. **Feature Engineering**: 68 features across 8 categories with comprehensive IP detection
3. **Model Training**: Multiple algorithms (LightGBM, XGBoost, Random Forest) with MLflow tracking
4. **Validation**: Time-based splits (train: 2015-2023, test: 2024, eval: 2025, predict: 2026)
5. **Deployment**: MLflow model serving for predictions

## 📈 Key Performance Insights

### Model Performance
- **Best Model**: LightGBM with 80% Recall@10 (identifies 8/10 top movies correctly)
- **RMSE**: $78.9M average prediction error
- **R²**: 0.472 (explains 47% of revenue variance)
- **Training Strategy**: No pandemic era data (excludes 2020-2021 anomalies)

### IP vs Original Content Analysis
- **IP movies**: 9.5% of releases, 466% revenue advantage over originals
- **Marvel dominance**: 36 MCU films with highest average revenue
- **Superhero advantage**: 80 superhero movies show consistent outperformance
- **Live-action remakes**: 23 Disney/DreamWorks remakes with strong box office results

### Market Trends (2015-2026)
- **Studio Competition**: Disney leads average revenue, major studios account for 54.5% of releases
- **Genre Evolution**: Action-adventure maintains dominance, streaming era affects mid-budget films
- **Seasonal Patterns**: Summer blockbusters (32.7% of releases), holiday concentration
- **Competition Effects**: 95.9% of movies face nearby major release competition

### Dataset Configurations
- **English-only (2015-2026)**: 1,307 movies - Best model performance
- **English-only (2010-2026)**: 2,009 movies - Broader historical scope
- **Major studios only**: 1,274 movies - Studio-focused analysis
- **Full dataset**: 2,339 movies - Complete market view

## 🔄 Data Updates & Maintenance

The project includes automated data refresh capabilities:

```bash
# Update Box Office Mojo + TMDb data
jupyter notebook code/1_get_data.ipynb

# Set FORCE_REFRESH = True to bypass cache
# Re-run feature engineering after data updates
jupyter notebook code/2_feature_engineering.ipynb
```

### MLflow Experiment Tracking
- **24 trained models** across multiple configurations
- **Comprehensive metrics**: RMSE, MAE, MAPE, R², Recall@10, Precision@10, NDCG@10
- **Dataset versioning**: Automatic tracking of training data subsets
- **Model comparison**: Built-in performance ranking and validation

## 🎯 2026 Predictions

The trained model provides predictions for 48 upcoming 2026 releases including:
- Revenue forecasts with confidence intervals
- Top 10 predicted performers
- Risk assessment based on feature analysis
- Comparison with historical similar releases

## 🔧 Technical Implementation

- **Feature Engineering**: Comprehensive 68-feature pipeline with IP detection
- **Model Architecture**: Ensemble methods with time-aware validation
- **Data Quality**: Automated title normalization, duplicate detection, outlier analysis
- **Reproducibility**: MLflow tracking, dataset versioning, configuration management
- **Scalability**: Modular design supporting multiple dataset configurations

## 📊 Future Enhancements

- **Real-time data integration**: Automated Box Office Mojo scraping
- **Extended feature set**: Social media sentiment, marketing spend, cast popularity
- **International markets**: Expansion beyond US domestic predictions
- **Streaming integration**: Hybrid theatrical/streaming performance modeling