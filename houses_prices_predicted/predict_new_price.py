#!/usr/bin/env python3
import joblib
import pandas as pd

new_data = pd.DataFrame({
    'MedInc': [3.5, 8.0, 2.1],
    'HouseAge': [25, 30, 15],
    'AveRooms': [4.5, 7.2, 3.9],
    'AveBedrms': [1.0, 1.1, 0.9],
    'Population': [900, 500, 1200],
    'AveOccup': [2.4, 3.0, 2.8],
    'Latitude': [36.8, 37.5, 35.2],
    'Longitude': [-121.9, -122.1, -120.9]
})

loaded_model = joblib.load('house_price_model.pkl')

predicted_price = loaded_model.predict(new_data)

for i, price in enumerate(predicted_price, start=1):
    real_price = price * 100000
    print(f"Predicted price for house {i}: ${real_price:,.2f}")


