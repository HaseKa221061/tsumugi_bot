# 軽量なPythonイメージを使用
FROM python:3.12-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存ライブラリのインストール
# キャッシュを利用してビルドを速くするため、先にコピー
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをすべてコピー
COPY . .

# Botを実行
CMD ["python", "main_launcher.py"]