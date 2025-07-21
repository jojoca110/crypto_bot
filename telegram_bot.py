

class TelegramBot:
    """Handles Telegram notifications for trading bot"""

    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.enabled = bool(bot_token and chat_id)

        if self.enabled:
            print("Telegram notifications enabled")


