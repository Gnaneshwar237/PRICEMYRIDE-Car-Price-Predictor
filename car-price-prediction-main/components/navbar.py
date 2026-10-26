# components/navbar.py
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
