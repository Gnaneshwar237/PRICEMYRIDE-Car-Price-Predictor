# core/config.py

class Theme:
    # Primary Backgrounds & Glassmorphism Surfaces
    BG_BASE = "#0b0f19"
    BG_SURFACE = "#111827"
    BG_CARD = "#1f293d"
    BG_CARD_HOVER = "#27354f"
    BORDER_SUBTLE = "#374151"
    BORDER_GLOW = "rgba(6, 182, 212, 0.3)"

    # Typography
    TEXT_PRIMARY = "#f9fafb"
    TEXT_SECONDARY = "#9ca3af"
    TEXT_MUTED = "#6b7280"

    # Status & Signal Accents
    EMERALD_GOOD = "#10b981"
    AMBER_FAIR = "#f59e0b"
    ROSE_RISK = "#ef4444"
    CYAN_METRIC = "#06b6d4"
    PURPLE_ACCENT = "#8b5cf6"

    # Gradients
    GRADIENT_CYAN_PURPLE = "linear-gradient(135deg, #06b6d4 0%, #8b5cf6 100%)"
    GRADIENT_CARD = "linear-gradient(145deg, rgba(31, 41, 61, 0.8) 0%, rgba(17, 24, 39, 0.95) 100%)"


APP_METADATA = {
    "title": "AutoValuate PRO",
    "tagline": "Institutional Used-Car Valuation & Decision Terminal",
    "version": "v5.0-Enterprise",
    "model_r2": "0.884",
    "inference_latency": "14ms",
    "market_regime": "Sellers Market (Low Inventory)",
}