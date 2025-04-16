# visualization.py
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def plot_forecast(forecast_df, historical_df):
    fig = go.Figure()

    if 'date' not in historical_df.columns:
        raise ValueError("❌ 'date' column missing in historical data!")

    # Plot historical
    fig.add_scatter(x=historical_df['date'], y=historical_df['total_cases'], name='Historical')

    # Plot forecast
    fig.add_scatter(x=forecast_df['Date'], y=forecast_df['Forecasted Cases'], name='Forecast')

    fig.update_layout(title="Disease Forecast", xaxis_title="Date", yaxis_title="Total Cases")
    st.plotly_chart(fig)

def show_map():
    df = pd.read_csv("data/covid_weekly_deaths_by_region.csv")
    df['date'] = pd.to_datetime(df['date'])
    latest = df.sort_values('date').groupby("region").last().reset_index()

    fig = px.choropleth(latest,
                        locations="region",
                        locationmode="country names",
                        color="total_cases",
                        hover_name="region",
                        title="Latest COVID-19 Deaths by Region",
                        color_continuous_scale="Reds")
    st.plotly_chart(fig, use_container_width=True)

def show_region_trend():
    df = pd.read_csv("data/covid_weekly_deaths_by_region.csv")
    df['date'] = pd.to_datetime(df['date'])

    regions = df['region'].unique()
    region = st.selectbox("Choose a region", regions)
    region_df = df[df['region'] == region]

    fig = px.line(region_df, x="date", y="total_cases", title=f"{region} - Weekly COVID-19 Deaths")
    st.plotly_chart(fig, use_container_width=True)