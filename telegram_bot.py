import requests


class TelegramBot:
    """Handles Telegram notifications for trading bot"""

    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.enabled = bool(bot_token and chat_id)

        if self.enabled:
            print("Telegram notifications enabled")
            self.send_message("Trading Bot Connected!\n\nReady to send trading updates.")

    def send_message(self, message):
        """Send message to Telegram"""
        if not self.enabled:
            return False

        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            data = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, data=data, timeout=10)
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Telegram error: {e}")
            return False


