# bot/client.py

import discord
from bot.handlers import MessageHandler

class TsumugiBotClient(discord.Client):
    """
    Spring日部つむぎBot本体
    """

    def __init__(self, handler: MessageHandler):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.handler = handler

    async def on_ready(self):
        print(f"ログイン完了: {self.user}")

    async def on_message(self, message):
        # Bot 自身には反応しない
        if message.author.bot:
            return

        # tumupingコマンドに対応
        if message.content.startswith("!tumuping"):
            await self.handler.handle_ping(message)

        # メンションされたら返信
        if self.user in message.mentions:
            await self.handler.handle_mention(message)
