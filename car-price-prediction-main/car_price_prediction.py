import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
df = pd.read_csv('car_data.csv')

# Encode categorical variables
df.replace({'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2}}, inplace=True)
df.replace({'Seller_Type': {'Dealer': 0, 'Individual': 1}}, inplace=True)
df.replace({'Transmission': {'Manual': 0, 'Automatic': 1}}, inplace=True)

# Features and Target
X = df[['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
y = df['Selling_Price']

# Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'car_prediction_model.pkl')
print("Model trained and saved as car_prediction_model.pkl successfully!")