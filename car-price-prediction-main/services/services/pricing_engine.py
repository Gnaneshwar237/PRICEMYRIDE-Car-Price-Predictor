# services/pricing_engine.py
import joblib
import pandas as pd
import numpy as np
import os

class ValuationEngine:
    def __init__(self, model_path: str = 'car_prediction_model.pkl'):
        self.model = None
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
            
    def predict_valuation(self, payload: dict) -> dict:
        """
        Executes model inference, applies condition scoring & computes price spreads.
        """
        if self.model is None:
            raise FileNotFoundError("Model file not found.")
            
        fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
        seller_map = {'Dealer': 0, 'Individual': 1}
        trans_map = {'Manual': 0, 'Automatic': 1}
        
        # Prepare 7-feature input dataframe for the Random Forest model
        X = pd.DataFrame([{
            'Year': payload.get('year', 2016),
            'Present_Price': payload.get('present_price', 7.5),
            'Kms_Driven': payload.get('kms_driven', 40000),
            'Fuel_Type': fuel_map.get(payload.get('fuel_type', 'Petrol'), 0),
            'Seller_Type': seller_map.get(payload.get('seller_type', 'Dealer'), 0),
            'Transmission': trans_map.get(payload.get('transmission', 'Manual'), 0),
            'Owner': payload.get('owner', 0)
        }])
        
        base_estimate = float(self.model.predict(X)[0])
        
        # Multiplier adjustments
        cond_multiplier = payload.get('condition_factor', 1.0)
        final_estimate = max(0.20, base_estimate * cond_multiplier)
        
        showroom_price = payload.get('present_price', 7.5)
        depreciation = max(0.0, showroom_price - final_estimate)
        deprec_pct = (depreciation / showroom_price) * 100 if showroom_price > 0 else 0
        
        # Liquidity and spreads
        dealer_buyout = round(final_estimate * 0.90, 2)
        private_sale = round(final_estimate * 1.05, 2)
        cpo_retail = round(final_estimate * 1.12, 2)
        range_low = round(final_estimate * 0.94, 2)
        range_high = round(final_estimate * 1.06, 2)
        
        return {
            'final_estimate': round(final_estimate, 2),
            'base_estimate': round(base_estimate, 2),
            'showroom_price': round(showroom_price, 2),
            'depreciation': round(depreciation, 2),
            'depreciation_pct': round(deprec_pct, 1),
            'range_low': range_low,
            'range_high': range_high,
            'dealer_buyout': dealer_buyout,
            'private_sale': private_sale,
            'cpo_retail': cpo_retail
        }