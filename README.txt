environment
    Python 3.12.10

install
    (python -m venv venv)
    (.\venv\Scripts\activate)
    pip install -r requirements.txt

    mkdir .env
    DISCORD_BOT_TOKEN=your_discord_key
    GEMINI_API_KEY=your_api_key

execute
    python main.py



discordのbotの作り方(discord developers)

    参考記事
    https://qiita.com/als/items/cb078585ac212285c671

    この記事に乗ってない設定項目
    以下の権限を与えてください

    OAuth2/Bot Permissions [
        Send Messages = true
        Read Message History = true
        View Channels = true
    ]

    Bot/Message Content Intent = true