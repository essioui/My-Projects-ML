#!/usr/bin/env python3
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics
import joblib

# loading the dataset
data = fetch_california_housing(as_frame=True)
print(data)

house_price_dataframe = pd.DataFrame(data=data.data, columns=data.feature_names)

# print the first 5 rows of the dataframe
print(house_price_dataframe.head())

# adding the target column to the dataframe
house_price_dataframe['Prices'] = data.target
print(house_price_dataframe.head())

# checking the number of rows and columns in the dataframe
print(house_price_dataframe.shape)

# check for messing values
print(house_price_dataframe.isnull().sum())

# statistical measures about the data
print(house_price_dataframe.describe())

# understanding the correlation between various features in the dataset
correlation = house_price_dataframe.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='Blues')
plt.show()

# splitting the data into features and target
X = house_price_dataframe.drop(columns='Prices', axis=1)
Y = house_price_dataframe['Prices']
print("the X", X)
print("the Y", Y)

# splitting the data into training data and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print("the X_train", X_train.shape)
print("the X_test", X_test.shape)
print("the Y_train", Y_train.shape)
print("the Y_test", Y_test.shape)

# Model Training

# loading the model (XGBoost Regressor)
model = XGBRegressor(n_estimators=500, learning_rate=0.05, max_depth=6)

# training the model with X_train
model.fit(X_train, Y_train)

# evaluation

# prediction on training data
# accuarcy for prediction on train data
training_data_prediction = model.predict(X_train)
print(training_data_prediction)

# Squared error
score1 = metrics.r2_score(Y_train, training_data_prediction)
print("R squared error : ", score1)

# Mean Absolute Error
score2 = metrics.mean_absolute_error(Y_train, training_data_prediction)
print("Mean Absolute Error : ", score2)


# accuracy for prediction on test data
test_data_prediction = model.predict(X_test)

# Squared error
score3 = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error : ", score3)

# Mean Absolute Error
score4 = metrics.mean_absolute_error(Y_test, test_data_prediction)
print("Mean Absolute Error : ", score4)

# plotting the actual prices and predicted prices
plt.scatter(Y_test, test_data_prediction, color='blue', alpha=0.5)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

# saving the trained model
joblib.dump(model, 'house_price_model.pkl')
print("Model saved successfully!")
