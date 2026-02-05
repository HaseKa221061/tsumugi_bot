# Python 3.12.0 の軽量イメージを使用
FROM python:3.12.0-slim

# 作業ディレクトリを設定
WORKDIR /app

# 環境変数の設定
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 依存関係のインストールに必要なシステムパッケージを導入
# gcc, libc-dev, libffi-dev など、cffiのビルドに必要なものをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコード全体をコピー
COPY . .

# main.py を実行
CMD ["python", "main.py"]