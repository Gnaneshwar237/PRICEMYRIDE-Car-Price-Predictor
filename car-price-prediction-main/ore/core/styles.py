# core/styles.py
import streamlit as st

def inject_design_system():
    css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        .stApp {
            background: radial-gradient(circle at 15% 15%, #131d31 0%, #0b0f19 90%);
            color: #f9fafb;
        }

        .hud-ribbon {
            background: #111827;
            border: 1px solid #374151;
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
            color: #06b6d4;
            border: 1px solid #334155;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .pro-card {
            background: linear-gradient(145deg, rgba(31, 41, 61, 0.8) 0%, rgba(17, 24, 39, 0.95) 100%);
            border: 1px solid #374151;
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
            color: #10b981;
            border: 1px solid #10b981;
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.8rem;
        }

        .badge-fair {
            background: rgba(245, 158, 11, 0.15);
            color: #f59e0b;
            border: 1px solid #f59e0b;
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.8rem;
        }

        .badge-risk {
            background: rgba(239, 68, 68, 0.15);
            color: #ef4444;
            border: 1px solid #ef4444;
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.8rem;
        }

        .stSelectbox div[data-baseweb="select"] > div,
        .stNumberInput div[data-baseweb="input"] > div,
        .stTextInput div[data-baseweb="input"] > div {
            background-color: #1a2436 !important;
            border: 1px solid #374151 !important;
            border-radius: 8px !important;
            color: #f9fafb !important;
        }

        div.stButton > button:first-child {
            background: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 100%) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 10px 24px !important;
            box-shadow: 0 4px 14px rgba(6, 182, 212, 0.4) !important;
        }
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)