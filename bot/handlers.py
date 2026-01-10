# bot/handlers.py

from services.gemini_service import GeminiService

class MessageHandler:
    """
    メッセージイベント処理を担当
    """

    user_name: str

    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service

    async def handle_mention(self, message):
        """
        Bot がメンションされた場合の応答処理
        """

        # ユーザー名を取得
        self.user_name = message.author.display_name

        user_text = message.content

        prompt = f"""
ユーザー名: {self.user_name}
ユーザーの発言:
{user_text}
"""
        
        reply = self.gemini_service.generate_reply(prompt)
        await message.channel.send(reply)
