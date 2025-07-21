# === API CONFIG ===

# BINANCE
API_KEY = "Your api key"
API_SECRET = "Your secret key"

# TELEGRAM
TG_BOT_TOKEN = "Your bot token"
TG_CHAT_ID = "Your chat id"

# === AGGRESSIVENESS SETTINGS ===
AGGRESSIVENESS_LEVEL = "MODERATE"

AGGRESSIVENESS_PRESETS = {
    "MODERATE": {
        "leverage": 3,
        "min_confidence": 0.6,
        "max_position_per_asset": 0.25,
        "reserve_cash": 0.2,
        "max_positions": 6,
        "position_base_percent": 0.08
    },
    "AGGRESSIVE": {
        "leverage": 5,
        "min_confidence": 0.55,
        "max_position_per_asset": 0.4,
        "reserve_cash": 0.05,
        "max_positions": 8,
        "position_base_percent": 0.15
    },
    "VERY_AGGRESSIVE": {
        "leverage": 10,
        "min_confidence": 0.5,
        "max_position_per_asset": 0.6,
        "reserve_cash": 0.02,
        "max_positions": 10,
        "position_base_percent": 0.25
    }
}

# === TRADING PARAMETERS ===
MIN_SAFE_MARGIN_LEVEL = 1.3
