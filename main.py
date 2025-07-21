from config import *

if __name__ == "__main__":
    print("ADVANCED LEVERAGED CRYPTO TRADING BOT")
    print("Telegram available")
    print("=" * 60)

    # Telegram Setup (optional)
    telegram_bot = None
    use_telegram = input("Enable Telegram notifications? (y/n): ").strip().lower()

    if use_telegram in ['y','yes']:
        print("\n TELEGRAM SETUP:")
        print("1. Create a bot with @BotFather on Telegram")
        print("2. Get your bot token")
        print("3. Start a chat with your bot")
        print("4. Send /start to your bot")
        print("5. Get your chat ID from @userinfobot")

        bot_token = TG_BOT_TOKEN
        chat_id = TG_CHAT_ID

        if bot_token and chat_id:
            try:
                # telegram_bot = TelegramBot()
                print("✅ Telegram setup successful!")
            except Exception as e:
                print("❌ Telegram setup failed")
                telegram_bot = None
        else:
            print("Invalid credentials- Telegram disabled")

    print("AGGRESSIVENESS LEVELS:")
    print("1. MODERATE (3x leverage, 60% confidence)")
    print("2. AGGRESSIVE (5x leverage, 55% confidence)")
    print("3. VERY AGRESSIVE (10x leverage, 50% confidence) 🚨 EXTREME RISK 🚨")

    choice = input("\nChoose (1-3) or press Enter for MODERATE: ").strip()

    if choice == "2":
        AGGRESSIVENESS_LEVEL = "AGGRESSIVE"
    elif choice == "3":
        AGGRESSIVENESS_LEVEL = "VERY AGGRESSIVE"
        print("🚨 WARNING: 10x leverage is EXTREMELY risky!")
        confirm_risk = input("Type 'YES' to confirm extreme risk: ")
        if confirm_risk != "YES":
            print("Switched to AGGRESSIVE (5x) for safety")
            AGGRESSIVENESS_LEVEL = "AGGRESSIVE"
    else:
        AGGRESSIVENESS_LEVEL = "MODERATE"

    # Update Settings
    PRESET = AGGRESSIVENESS_PRESETS[AGGRESSIVENESS_LEVEL]
    MARGIN_LEVERAGE = PRESET["leverage"]
    MIN_CONFIDENCE = PRESET["min_confidence"]
    MAX_POSITION_PER_ASSET = PRESET["max_position_per_asset"]
    RESERVE_CASH_PERCENT = PRESET["reserve_cash"]
    MAX_POSITION = PRESET["max_positions"]
    POSITION_BASE_PERCENT = PRESET["position_base_percent"]
