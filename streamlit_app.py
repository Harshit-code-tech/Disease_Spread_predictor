# streamlit_app.py
import streamlit as st

from utils.forecasting import recursive_forecast
from utils.model_loader import load_model_and_data
from utils.visualization import plot_forecast, show_map, show_region_trend

st.set_page_config(page_title="Disease Forecast Dashboard", layout="wide")

st.sidebar.title("Disease Forecast Dashboard")
selected_tab = st.sidebar.radio("Choose Task", [
    "Home",
    "Forecasting Overview",
    "Predict Cases",
    "Region-wise Visualization",
    "About Project"
])

# --- Home Tab ---
if selected_tab == "Home":
    st.title("Welcome to the Disease Forecast Dashboard")
    st.markdown("""
    This dashboard forecasts disease spread using historical data for:
    - 🦟 Dengue
    - 🦠 Influenza
    - 🧍‍♂️ COVID-19

    Built with XGBoost, Random Forest, and time series modeling. View national and regional trends.
    """)

# --- Forecasting Overview Tab ---
elif selected_tab == "Forecasting Overview":
    st.title("Forecasting Overview")
    disease = st.selectbox("Choose a disease to forecast", ["Dengue", "Influenza", "COVID-19"])
    model, latest_input, df = load_model_and_data(disease)
    forecast = recursive_forecast(model, latest_input, 8)
    plot_forecast(forecast, df)

# --- Predict Next Week's Cases Tab ---
elif selected_tab == "Predict Cases":
    st.title("Predict Next Week's Cases")
    disease = st.selectbox("Select Disease", ["Dengue", "Influenza", "COVID-19"])
    model, latest_input, _ = load_model_and_data(disease)

    st.write("Provide recent weekly case values (used as lag features):")
    lags = []
    for i in range(len(latest_input)):
        val = st.number_input(f"Week -{len(latest_input) - i}", value=float(latest_input[i]))
        lags.append(val)

    if st.button("Predict"):
        prediction = model.predict([lags])[0]
        st.success(f"🧮 Predicted next week cases: **{round(prediction)}**")

# --- Region-wise Visualization Tab ---
elif selected_tab == "Region-wise Visualization":
    st.title("Regional View")

    # Currently only COVID-19 has regional data
    disease = st.selectbox("Select Disease for Region-wise View", ["COVID-19"])
    region_view = st.radio("Select view", ["Map", "Time Series by Region"])

    if disease == "COVID-19":
        if region_view == "Map":
            show_map()
        else:
            show_region_trend()
    else:
        st.warning(f"⚠️ Regional data not available for {disease}.")

# --- About Tab ---
elif selected_tab == "About Project":
    st.title("About the Project")
    st.markdown("""
    This system forecasts disease spread using historical data from:
    - Kaggle
    - WHO
    - CDC
    - Mexican Government Datasets

    Models Used:
    - Time Series Models with Lag Features
    - Random Forest & XGBoost
    - Recursive Multi-step Forecasting

    Regional views are available for COVID-19, with visualizations on maps and time series by region.
    """)
