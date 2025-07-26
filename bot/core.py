import requests
import time


class TelegramBot:
    _instance = None

    def __new__(cls, token):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, TOKEN):
        self.token = TOKEN
        self.url = 'https://api.telegram.org/bot{}/'

    def get_last_update(self):
        url = self.url + "getUpdates?timeout=10"
        response = requests.get(url)
        result = response.json()["result"]
        if result:
            return result[-1]
        return None

    def get_chat_id(self, update):
        return update["message"]["chat"]["id"]

    def get_user_id(self, update):
        return update["message"]["from"]["id"]

    def get_message_text(self, update):
        return update["message"]["text"]

    def send_message(self, chat_id, text):
        url = self.url + "sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        requests.post(url, json=payload)

    def run(self):
        while True:
            time.sleep(5)
            update = self.get_last_update()
            chat_id = self.get_chat_id(update)
            user_id = self.get_user_id(update)
            text = self.get_message_text(update)
            self.send_message(chat_id, text)

