# Disease Forecasting Dashboard

## Project Overview
This project focuses on predicting the future spread of diseases such as COVID-19, Dengue, Cholera, and Influenza. Using historical datasets and machine learning techniques, the app forecasts disease trends and provides geospatial visualizations to help better understand regional disease outbreaks. The models used include Random Forest and XGBoost, which have been trained and optimized for accurate forecasting. 

### Key Features:
- **Forecasting with Random Forest and XGBoost**: Accurate predictions for the future spread of diseases.
- **Geospatial Visualization**: Interactive maps showing disease predictions based on location.
- **Historical Data Analysis**: Time-series forecasting for trend analysis and future predictions.
- **User Interaction**: Allows users to select different diseases and forecast horizons, making the dashboard flexible for a variety of users.

## Dataset and Data Sources

### Datasets Used:
1. **COVID-19 Data** (Mexico)
   - This dataset contains daily COVID-19 infection counts, patient demographics, comorbidities, and other relevant features. It is used to forecast the spread of COVID-19 in various regions of Mexico.
   - **Source**: [Kaggle - COVID-19 Data from Mexican Government](https://www.kaggle.com/datasets)
   
2. **Cholera Data** (WHO)
   - A dataset that provides historical data on cholera outbreaks worldwide.
   - **Source**: [World Health Organization (WHO)](https://www.who.int)

3. **Dengue Data** (Kaggle)
   - A dataset containing daily records of Dengue fever outbreaks in different regions.
   - **Source**: [Kaggle - Dengue Fever Data](https://www.kaggle.com/datasets)

4. **Influenza Data** (CDC)
   - This dataset tracks the seasonal flu and its patterns, provided by the CDC.
   - **Source**: [CDC - Influenza Data](https://www.cdc.gov)

### Dataset Issues and Challenges:
- **Missing Data**: Some datasets had missing values or incomplete records, particularly in the COVID-19 and Dengue datasets. These gaps were handled through imputation and removal of certain rows.
- **Data Quality**: Inconsistent reporting intervals in some regions of the datasets required extra preprocessing to normalize data for time-series forecasting.
- **Geospatial Data Challenges**: Geospatial data was sparse in some areas, making it difficult to generate accurate predictions for certain regions. We handled this by focusing on regions with more complete data and using interpolation techniques for others.

### Preprocessing:
- **Data Cleaning**: Missing data were handled using imputation techniques. Unnecessary columns were dropped, and dates were normalized.
- **Feature Engineering**: Lag features were added to assist with time-series forecasting, especially for models like XGBoost and Random Forest.
- **Scaling and Encoding**: Necessary categorical variables were one-hot encoded, and numerical features were scaled to improve model performance.

## Technologies Used:
- **Python**: Main programming language.
- **Streamlit**: For the frontend dashboard and visualizations.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: For machine learning models (Random Forest, XGBoost).
- **Geopandas**: For geospatial data visualizations.
- **Matplotlib/Plotly**: For interactive charts and graphs.




