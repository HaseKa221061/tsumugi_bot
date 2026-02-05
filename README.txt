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



====================
# Docker関連
====================

春日部つむぎ Discord Bot (Docker版)
埼玉育ちのギャル「春日部つむぎ」が Discord でおしゃべりする Bot です。 Google Gemini API を使って、明るく元気に（たまにいたずらっぽく）返信します。 

# 事前準備
環境変数ファイルの作成: 同じディレクトリに .env ファイルを作成し、以下の内容を記入してください。

DISCORD_BOT_TOKEN=あなたのトークン
GEMINI_API_KEY=あなたのAPIキー

# 構築と管理
1. 設計図から「完成品」を作る (Build)
Dockerfile を元に、Docker イメージを作成します。

docker build -t tsumugi-bot .

2. ボットを起動する (Run)

docker run -d --name tsumugi-bot --env-file .env tsumugi-bot

-d : バックグラウンド
--name [dockerimageの名前] : 起動するイメージを選択
--env-file [.envファイル] : シークレットキーを読み込む

3. 確認 (Logs)
ちゃんとログインできたか、ログをリアルタイムで監視します。

Bash
docker logs -f tsumugi-bot
4. ボットを止める / 消す (Stop & Remove)
Bash
# 一時停止
docker stop tsumugi-bot

# 削除 (プログラムを更新して作り直す前に実行)
docker rm tsumugi-bot

更新手順

イメージを再ビルド: sudo docker build -t tsumugi-bot .

古いコンテナを消す: sudo docker rm -f tsumugi-bot

新しいコンテナを起動: sudo docker run -d --name tsumugi-bot --env-file .env tsumugi-bot

ファイル構成

bot/: ボット本体とペルソナ設定。

services/: Gemini API との通信。 

main.py: ボットを動かすメインスクリプト。

Dockerfile: ラズパイ(ARM)環境向けに最適化したビルド設定。