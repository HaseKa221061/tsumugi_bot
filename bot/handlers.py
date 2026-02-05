# bot/handlers.py

from services.gemini_service import GeminiService

class MessageHandler:
    """
    メッセージイベント処理を担当
    """

    user_name: str

    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service

    async def handle_ping(self, message):
        """
        pingコマンドの応答処理
        """
        await message.channel.send("""
 _____ _   _ __  __ _   _ ____   ___  _   _  ____ _
|_   _| | | |  \/  | | | |  _ \ / _ \| \ | |/ ___| |
  | | | | | | |\/| | | | | |_) | | | |  \| | |  _| |
  | | | |_| | |  | | |_| |  __/| |_| | |\  | |_| |_|
  |_|  \___/|_|  |_|\___/|_|    \___/|_| \_|\____(_)
        """)

    async def handle_mention(self, message):
        """
        Bot がメンションされた場合の応答処理
        """

        # ユーザー名を取得
        self.user_name = message.author.display_name

        user_text = message.content

# ユーザー名: {self.user_name}　必要ならprompt内に入れる
        prompt = f"""
ユーザーの発言:
{user_text}
"""
        
        reply = self.gemini_service.generate_reply(prompt)
        await message.channel.send(reply)
