# services/gemini_service.py

import google.generativeai as genai
from bot.persona import TsumugiPersona

class GeminiService:
    """
    Gemini API との通信を担当するサービスクラス
    """

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=TsumugiPersona.system_prompt
        )

    def generate_reply(self, user_text: str) -> str:
        """
        入力テキストに対する Gemini の返答を生成
        """
        response = self.model.generate_content(user_text)
        return response.text
