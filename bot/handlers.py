# bot/handlers.py

from services.gemini_service import GeminiService

class MessageHandler:
    """
    メッセージイベント処理を担当
    """

    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service

    async def handle_mention(self, message):
        """
        Bot がメンションされた場合の応答処理
        """
        user_text = message.content
        reply = self.gemini_service.generate_reply(user_text)
        await message.channel.send(reply)
