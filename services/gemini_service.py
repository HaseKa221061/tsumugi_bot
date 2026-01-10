# services/gemini_service.py

from google import genai
from google.genai.types import GenerateContentConfig
from bot.persona import TsumugiPersona

class GeminiService:
    """
    Gemini API との通信を担当するサービスクラス
    """

    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def generate_reply(self, user_text: str) -> str:
        """
        入力テキストに対する Gemini の返答を生成
        """    
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_text,
                config=GenerateContentConfig(
                    system_instruction=TsumugiPersona.system_prompt
                )
            )
            return response.text

        except Exception as e:
            # 429エラーを含むAPI例外対応
            error_message = str(e).lower()
            
            if "429" in error_message or "resource" in error_message or "quota" in error_message:
                response = self.client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=user_text,
                config=GenerateContentConfig(
                    system_instruction=TsumugiPersona.system_prompt
                    )
                )
                return response.text
            
            else:
                return f"ちょっと急に用事思い出しちゃった💦\n詳細: {str(e)}"