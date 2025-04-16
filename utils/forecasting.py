# forecasting.py
import pandas as pd
import numpy as np

def recursive_forecast(model, recent_data, steps):
    predictions = []
    input_data = list(recent_data)
    for _ in range(steps):
        pred = model.predict([input_data])[0]
        predictions.append(pred)
        input_data = input_data[1:] + [pred]

    dates = pd.date_range(start=pd.Timestamp.today(), periods=steps, freq='W')
    return pd.DataFrame({"Date": dates, "Forecasted Cases": predictions})
