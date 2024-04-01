import requests

from atomic_habits import settings


class TelegramNotificationBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    def send_habit_notification(self, text, chat_id) -> None:
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
