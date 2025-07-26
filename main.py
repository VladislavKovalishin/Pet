import os
from dotenv import load_dotenv
from bot.core import TelegramBot


def main():
    load_dotenv()
    bot_token = os.getenv("TOKEN")
    bot = TelegramBot(bot_token)
    bot.run()


if __name__ == "__main__":
    main()
