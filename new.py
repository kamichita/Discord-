import time
import os
from pypresence import Presence

# Developer Portalで作成したアプリケーションのIDを設定します
CLIENT_ID = "1279674787865825342"  # あなたのアプリケーションIDに置き換えてください
TOKEN = os.getenv("TOKEN")

try:
    # プレゼンスクライアントを初期化して接続
    RPC = Presence(CLIENT_ID)
    RPC.connect()
    
    # リッチプレゼンスを更新
    # ここで「kamichita_icon」はDeveloper Portalにアップロードした画像のアセットキーです
    RPC.update(
        state="Playing",  # 状態
        details="Kamichita247",  # 詳細
        large_image="kamichita_icon",  # Developer Portalでアップロードした画像のキー
        large_text="Kamichita247",  # 画像にカーソルを合わせた時に表示されるテキスト
        start=int(time.time())  # 開始時間（現在時刻から）
    )
    
    print("リッチプレゼンスが有効になりました。Ctrl+Cで終了します。")
    # 接続を維持
    while True:
        time.sleep(15)  # Discordにはレート制限があるため、15秒ごとに更新
except KeyboardInterrupt:
    print("リッチプレゼンスを終了しました。")
    RPC.close()
