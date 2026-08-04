
# Heart Disease Prediction — CI Assignment

Kaggle Playground Series S6E2 competition submission.

## Files
- Training script/notebook — EDA, model training (Random Forest, XGBoost)
- `app.py` — Streamlit prediction app
- `heart_disease_model.pkl` — trained XGBoost model

## Setup
1. Download `train.csv`/`test.csv` from [the competition page](https://www.kaggle.com/competitions/playground-series-s6e2)
2. `pip install -r requirements.txt`
3. `streamlit run app.py`

## Results
- XGBoost validation AUC: 0.956
- Kaggle leaderboard: 0.953 (public) / 0.955 (private)
