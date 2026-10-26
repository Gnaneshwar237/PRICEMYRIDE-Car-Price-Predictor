# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv('car_data.csv')

# Encode categorical values
df.replace({'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2}}, inplace=True)
df.replace({'Seller_Type': {'Dealer': 0, 'Individual': 1}}, inplace=True)
df.replace({'Transmission': {'Manual': 0, 'Automatic': 1}}, inplace=True)

X = df[['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
y = df['Selling_Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'car_prediction_model.pkl')
print("✅ Trained Random Forest Regressor saved as car_prediction_model.pkl successfully!")