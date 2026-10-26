# views/valuation_view.py
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
