# model_loader.py
import pandas as pd
import pickle

def load_model_and_data(disease):
    if disease == "Dengue":
        model = pickle.load(open("models/dengue_xgb.pkl", "rb"))
        df = pd.read_csv("data/cleaned_dengue.csv")
    elif disease == "Influenza":
        model = pickle.load(open("models/flu_xgb.pkl", "rb"))
        df = pd.read_csv("data/cleaned_influenza.csv")
    else:
        model = pickle.load(open("models/covid_xgb.pkl", "rb"))
        df = pd.read_csv("data/covid_weekly_deaths.csv")

        # Rename for consistency (only for COVID dataset)
        df.rename(columns={
            'week_start': 'date',
            'deaths': 'total_cases'
        }, inplace=True)

    # Ensure 'date' column is datetime
    df['date'] = pd.to_datetime(df['date'])

    # Get model expected input size
    num_features = model.n_features_in_
    latest_input = df['total_cases'].tail(num_features).tolist()
    return model, latest_input, df