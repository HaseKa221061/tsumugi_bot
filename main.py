# main.py

import os
from dotenv import load_dotenv

from services.gemini_service import GeminiService
from bot.handlers import MessageHandler
from bot.client import TsumugiBotClient

def main():
    load_dotenv()

    token = os.getenv("DISCORD_BOT_TOKEN")
    api_key = os.getenv("GEMINI_API_KEY")

    # Gemini Service
    gemini = GeminiService(api_key)

    # Handler
    handler = MessageHandler(gemini)

    # Client
    client = TsumugiBotClient(handler)

    # Run bot
    client.run(token)


if __name__ == "__main__":
    main()
