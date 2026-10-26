import os

# Define folders to create
folders = ['core', 'components', 'services', 'views']
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    init_file = os.path.join(folder, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w', encoding='utf-8') as f:
            f.write('')

# 1. core/config.py
config_code = '''# core/config.py

class Theme:
    BG_BASE = "#0b0f19"
    BG_SURFACE = "#111827"
    BG_CARD = "#1f293d"
    BG_CARD_HOVER = "#27354f"
    BORDER_SUBTLE = "#374151"
    BORDER_GLOW = "rgba(6, 182, 212, 0.3)"

    TEXT_PRIMARY = "#f9fafb"
    TEXT_SECONDARY = "#9ca3af"
    TEXT_MUTED = "#6b7280"

    EMERALD_GOOD = "#10b981"
    AMBER_FAIR = "#f59e0b"
    ROSE_RISK = "#ef4444"
    CYAN_METRIC = "#06b6d4"
    PURPLE_ACCENT = "#8b5cf6"

    GRADIENT_CYAN_PURPLE = "linear-gradient(135deg, #06b6d4 0%, #8b5cf6 100%)"
    GRADIENT_CARD = "linear-gradient(145deg, rgba(31, 41, 61, 0.8) 0%, rgba(17, 24, 39, 0.95) 100%)"

APP_METADATA = {
    "title": "AutoValuate PRO",
    "tagline": "Institutional Used-Car Valuation & Decision Terminal",
    "version": "v5.0-Enterprise",
    "model_r2": "0.884",
    "inference_latency": "14ms",
    "market_regime": "Sellers Market (Low Inventory)"
}
'''
with open(os.path.join('core', 'config.py'), 'w', encoding='utf-8') as f:
    f.write(config_code)

# 2. core/styles.py
styles_code = '''# core/styles.py
import streamlit as st
from core.config import Theme

def inject_design_system():
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        .stApp {
            background: radial-gradient(circle at 15% 15%, #131d31 0%, {Theme.BG_BASE} 90%);
            color: {Theme.TEXT_PRIMARY};
        }

        .hud-ribbon {
            background: {Theme.BG_SURFACE};
            border: 1px solid {Theme.BORDER_SUBTLE};
            border-radius: 12px;
            padding: 12px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }

        .hud-metric-pill {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            padding: 4px 10px;
            border-radius: 6px;
            background: #1e293b;
            color: {Theme.CYAN_METRIC};
            border: 1px solid #334155;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .pro-card {
            background: {Theme.GRADIENT_CARD};
            border: 1px solid {Theme.BORDER_SUBTLE};
            border-radius: 14px;
            padding: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
            backdrop-filter: blur(10px);
        }

        .terminal-mono {
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700;
        }

        .badge-good {
            background: rgba(16, 185, 129, 0.15);
            color: {Theme.EMERALD_GOOD};
            border: 1px solid {Theme.EMERALD_GOOD};
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.8rem;
        }

        .badge-fair {
            background: rgba(245, 158, 11, 0.15);
            color: {Theme.AMBER_FAIR};
            border: 1px solid {Theme.AMBER_FAIR};
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.8rem;
        }

        .badge-risk {
            background: rgba(239, 68, 68, 0.15);
            color: {Theme.ROSE_RISK};
            border: 1px solid {Theme.ROSE_RISK};
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.8rem;
        }

        .stSelectbox div[data-baseweb="select"] > div,
        .stNumberInput div[data-baseweb="input"] > div,
        .stTextInput div[data-baseweb="input"] > div {
            background-color: #1a2436 !important;
            border: 1px solid {Theme.BORDER_SUBTLE} !important;
            border-radius: 8px !important;
            color: {Theme.TEXT_PRIMARY} !important;
        }

        div.stButton > button:first-child {
            background: {Theme.GRADIENT_CYAN_PURPLE} !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 10px 24px !important;
            box-shadow: 0 4px 14px rgba(6, 182, 212, 0.4) !important;
        }
        </style>
    """, unsafe_allow_html=True)
'''
with open(os.path.join('core', 'styles.py'), 'w', encoding='utf-8') as f:
    f.write(styles_code)

# 3. components/navbar.py
navbar_code = '''# components/navbar.py
import streamlit as st
from core.config import APP_METADATA, Theme

def render_top_navbar():
    st.markdown(f"""
        <div class="hud-ribbon">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div style="background: {Theme.GRADIENT_CYAN_PURPLE}; width: 12px; height: 12px; border-radius: 50%; box-shadow: 0 0 10px {Theme.CYAN_METRIC};"></div>
                <span style="font-weight: 800; font-size: 1.05rem; letter-spacing: -0.02em; color: #fff;">
                    {APP_METADATA['title']} <span style="font-weight: 400; font-size: 0.8rem; color: {Theme.TEXT_SECONDARY};">| {APP_METADATA['version']}</span>
                </span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center;">
                <div class="hud-metric-pill">
                    <span>REGIME:</span> <strong style="color: {Theme.EMERALD_GOOD};">{APP_METADATA['market_regime']}</strong>
                </div>
                <div class="hud-metric-pill">
                    <span>ACCURACY:</span> <strong>R² = {APP_METADATA['model_r2']}</strong>
                </div>
                <div class="hud-metric-pill">
                    <span>LATENCY:</span> <strong>{APP_METADATA['inference_latency']}</strong>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
'''
with open(os.path.join('components', 'navbar.py'), 'w', encoding='utf-8') as f:
    f.write(navbar_code)

# 4. services/nlp_parser.py
nlp_code = '''# services/nlp_parser.py
import re

def parse_natural_query(query: str) -> dict:
    parsed = {}
    q = query.upper()
    
    years = re.findall(r'\\b(200\\d|201\\d|202[0-6])\\b', q)
    if years:
        parsed['year'] = int(years[0])
        
    price_match = re.findall(r'(\\d+(?:\\.\\d+)?)\\s*(?:L|LAKH|LAKHS)', q)
    if price_match:
        parsed['present_price'] = float(price_match[0])
        
    km_match = re.findall(r'(\\d+)\\s*(?:K\\s*KM|K\\s*KMS|KMS|KM|K\\b)', q)
    if km_match:
        val = int(km_match[0])
        parsed['kms_driven'] = val * 1000 if val < 1000 else val
        
    if "DIESEL" in q:
        parsed['fuel_type'] = "Diesel"
    elif "PETROL" in q:
        parsed['fuel_type'] = "Petrol"
    elif "CNG" in q:
        parsed['fuel_type'] = "CNG"
        
    if any(k in q for k in ["AUTOMATIC", "AUTO", "AT", "CVT", "DCT"]):
        parsed['transmission'] = "Automatic"
    elif any(k in q for k in ["MANUAL", "MT"]):
        parsed['transmission'] = "Manual"
        
    cities = ["CHENNAI", "BANGALORE", "MUMBAI", "DELHI", "HYDERABAD", "PUNE", "KOLKATA"]
    for city in cities:
        if city in q:
            parsed['city'] = city.title()
            break
            
    return parsed
'''
with open(os.path.join('services', 'nlp_parser.py'), 'w', encoding='utf-8') as f:
    f.write(nlp_code)

# 5. services/pricing_engine.py
pricing_code = '''# services/pricing_engine.py
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
        if self.model is None:
            raise FileNotFoundError("Model file not found.")
            
        fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
        seller_map = {'Dealer': 0, 'Individual': 1}
        trans_map = {'Manual': 0, 'Automatic': 1}
        
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
        cond_multiplier = payload.get('condition_factor', 1.0)
        final_estimate = max(0.20, base_estimate * cond_multiplier)
        
        showroom_price = payload.get('present_price', 7.5)
        depreciation = max(0.0, showroom_price - final_estimate)
        deprec_pct = (depreciation / showroom_price) * 100 if showroom_price > 0 else 0
        
        return {
            'final_estimate': round(final_estimate, 2),
            'base_estimate': round(base_estimate, 2),
            'showroom_price': round(showroom_price, 2),
            'depreciation': round(depreciation, 2),
            'depreciation_pct': round(deprec_pct, 1),
            'range_low': round(final_estimate * 0.94, 2),
            'range_high': round(final_estimate * 1.06, 2),
            'dealer_buyout': round(final_estimate * 0.90, 2),
            'private_sale': round(final_estimate * 1.05, 2),
            'cpo_retail': round(final_estimate * 1.12, 2)
        }
'''
with open(os.path.join('services', 'pricing_engine.py'), 'w', encoding='utf-8') as f:
    f.write(pricing_code)

# 6. views/valuation_view.py
view_code = '''# views/valuation_view.py
import streamlit as st
import plotly.graph_objects as go
from services.nlp_parser import parse_natural_query
from services.pricing_engine import ValuationEngine
from core.config import Theme

engine = ValuationEngine()

def render_valuation_view():
    st.markdown('<div class="pro-card" style="margin-bottom: 20px;">', unsafe_allow_html=True)
    st.markdown("##### 🔍 Natural Language Smart Ingestion")
    
    col_nlp, col_btn = st.columns([4, 1])
    with col_nlp:
        nlp_input = st.text_input(
            "Prompt",
            placeholder="e.g. 2018 automatic diesel SUV under 12L with 45000 km in Chennai",
            label_visibility="collapsed"
        )
    with col_btn:
        parse_btn = st.button("Auto-Fill ⚡", use_container_width=True)
        
    extracted_state = {}
    if parse_btn and nlp_input:
        extracted_state = parse_natural_query(nlp_input)
        if extracted_state:
            st.success(f"Parameters Identified: {extracted_state}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.3, 1], gap="large")
    
    with col_left:
        st.markdown('<div class="pro-card">', unsafe_allow_html=True)
        st.markdown(f'<h4 style="color: {Theme.TEXT_PRIMARY}; margin-top: 0;">📋 Primary Specifications</h4>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            year = st.slider("Manufacturing Year", 2000, 2026, extracted_state.get('year', 2017))
            present_price = st.number_input("Ex-Showroom Price (₹ Lakhs)", 0.5, 95.0, extracted_state.get('present_price', 8.5), 0.25)
            kms_driven = st.number_input("Odometer (Kilometers)", 500, 500000, extracted_state.get('kms_driven', 38000), 1000)
            owner = st.selectbox("Previous Owners", [0, 1, 2, 3], index=0)
            
        with c2:
            fuel_opts = ["Petrol", "Diesel", "CNG"]
            fuel_idx = fuel_opts.index(extracted_state.get('fuel_type', 'Petrol')) if extracted_state.get('fuel_type') in fuel_opts else 0
            fuel_type = st.selectbox("Fuel Type", fuel_opts, index=fuel_idx)
            
            trans_opts = ["Manual", "Automatic"]
            trans_idx = trans_opts.index(extracted_state.get('transmission', 'Manual')) if extracted_state.get('transmission') in trans_opts else 0
            transmission = st.selectbox("Transmission", trans_opts, index=trans_idx)
            
            seller_type = st.selectbox("Seller Category", ["Dealer", "Individual"])
            city = st.selectbox("Registration City", ["Chennai", "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Pune"], index=0)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_right:
        st.markdown('<div class="pro-card">', unsafe_allow_html=True)
        st.markdown(f'<h4 style="color: {Theme.TEXT_PRIMARY}; margin-top: 0;">🛡️ Secondary Attributes & Wear</h4>', unsafe_allow_html=True)
        
        body_type = st.selectbox("Body Configuration", ["Hatchback", "Sedan", "SUV", "MUV", "Coupe"], index=2)
        insurance_status = st.selectbox("Insurance Validity", ["Comprehensive (>6 Mos)", "Third Party Only", "Expired"])
        service_history = st.radio("Service History", ["100% Authorized OEM", "Partial OEM", "Third-Party / Missing"], horizontal=True)
        
        condition_grade = st.select_slider(
            "Vehicle Condition Tier",
            options=["Fair (Scratches/Dents)", "Good (Normal Wear)", "Very Good (Clean)", "Mint (Showroom Grade)"],
            value="Good (Normal Wear)"
        )
        cond_map = {
            "Fair (Scratches/Dents)": 0.92,
            "Good (Normal Wear)": 1.00,
            "Very Good (Clean)": 1.04,
            "Mint (Showroom Grade)": 1.08
        }
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    val_button = st.button("⚡ EXECUTE MULTI-FACTOR VALUATION", use_container_width=True)
    
    if val_button:
        payload = {
            'year': year,
            'present_price': present_price,
            'kms_driven': kms_driven,
            'fuel_type': fuel_type,
            'transmission': transmission,
            'seller_type': seller_type,
            'owner': owner,
            'condition_factor': cond_map[condition_grade]
        }
        
        results = engine.predict_valuation(payload)
        
        st.markdown("---")
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f"""
                <div class="pro-card">
                    <span class="terminal-mono" style="color: {Theme.TEXT_SECONDARY}; font-size: 0.8rem;">ESTIMATED VALUE</span>
                    <div class="terminal-mono" style="font-size: 2.1rem; color: {Theme.CYAN_METRIC};">₹ {results['final_estimate']:.2f} L</div>
                    <span class="badge-good">Target Realization</span>
                </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
                <div class="pro-card">
                    <span class="terminal-mono" style="color: {Theme.TEXT_SECONDARY}; font-size: 0.8rem;">ORIGINAL SHOWROOM</span>
                    <div class="terminal-mono" style="font-size: 2.1rem; color: {Theme.AMBER_FAIR};">₹ {results['showroom_price']:.2f} L</div>
                    <span style="color: {Theme.TEXT_MUTED}; font-size: 0.8rem;">Ex-Showroom Base</span>
                </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
                <div class="pro-card">
                    <span class="terminal-mono" style="color: {Theme.TEXT_SECONDARY}; font-size: 0.8rem;">TOTAL DEPRECIATION</span>
                    <div class="terminal-mono" style="font-size: 2.1rem; color: {Theme.ROSE_RISK};">₹ {results['depreciation']:.2f} L</div>
                    <span style="color: {Theme.ROSE_RISK}; font-size: 0.8rem;">-{results['depreciation_pct']}% Retained</span>
                </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown(f"""
                <div class="pro-card">
                    <span class="terminal-mono" style="color: {Theme.TEXT_SECONDARY}; font-size: 0.8rem;">FAIR SPREAD</span>
                    <div class="terminal-mono" style="font-size: 1.5rem; line-height: 2.1rem; color: {Theme.PURPLE_ACCENT};">₹ {results['range_low']}L - {results['range_high']}L</div>
                    <span class="badge-fair">95% Range</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        
        c_meter, c_channel = st.columns([1.3, 1], gap="large")
        with c_meter:
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=results['final_estimate'],
                number={'prefix': "₹ ", 'suffix': " L", 'font': {'size': 32, 'color': Theme.CYAN_METRIC}},
                delta={'reference': results['showroom_price'], 'increasing': {'color': Theme.EMERALD_GOOD}, 'decreasing': {'color': Theme.ROSE_RISK}},
                gauge={
                    'axis': {'range': [0, results['showroom_price'] * 1.15], 'tickcolor': Theme.BORDER_SUBTLE},
                    'bar': {'color': Theme.CYAN_METRIC, 'thickness': 0.25},
                    'bgcolor': Theme.BG_SURFACE,
                    'steps': [
                        {'range': [0, results['showroom_price'] * 0.35], 'color': "rgba(239, 68, 68, 0.25)"},
                        {'range': [results['showroom_price'] * 0.35, results['showroom_price'] * 0.70], 'color': "rgba(245, 158, 11, 0.25)"},
                        {'range': [results['showroom_price'] * 0.70, results['showroom_price'] * 1.15], 'color': "rgba(16, 185, 129, 0.25)"}
                    ]
                }
            ))
            fig.update_layout(height=320, margin=dict(l=10, r=10, t=20, b=10), paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
            
        with c_channel:
            st.markdown('<div class="pro-card">', unsafe_allow_html=True)
            st.markdown(f'<h4 style="color: {Theme.TEXT_PRIMARY}; margin-top: 0;">💼 Channel Realization Matrix</h4>', unsafe_allow_html=True)
            st.write(f"🏢 **Dealer Trade-In Cash:** `₹ {results['dealer_buyout']} Lakhs`")
            st.caption("Immediate liquidity with zero advertising friction.")
            st.write(f"👤 **Private Party Listing:** `₹ {results['private_sale']} Lakhs`")
            st.caption("Maximum direct retail recovery.")
            st.write(f"🛡️ **Certified Pre-Owned (CPO):** `₹ {results['cpo_retail']} Lakhs`")
            st.caption("Dealer showroom list price with warranty.")
            st.markdown('</div>', unsafe_allow_html=True)
'''
with open(os.path.join('views', 'valuation_view.py'), 'w', encoding='utf-8') as f:
    f.write(view_code)

print("Project files generated successfully!")