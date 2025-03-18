import json
import asyncio
import websockets
import os

TOKEN = os.getenv("TOKEN")

async def presence():
    async with websockets.connect("wss://gateway.discord.gg/?v=9&encoding=json") as ws:
        # Discordに接続してIdentifyを送信
        await ws.send(json.dumps({
            "op": 2,
            "d": {
                "token": TOKEN,
                "properties": {
                    "$os": "windows",
                    "$browser": "chrome",
                    "$device": "pc"
                },
                "presence": {
                    "activities": [{
                        "name": "Kamichita",
                        "type": 0,  # Playing
                        "assets": {
                            "large_image": "kamichita_icon",  # Discord開発者ポータルにアップした画像のキー
                            "large_text": "kamichita"
                        }
                    }],
                    "status": "online",
                    "afk": False
                }
            }
        }))

        while True:
            # 定期的にプレゼンスを更新（5分ごと）
            await ws.send(json.dumps({
                "op": 3,
                "d": {
                    "since": None,
                    "activities": [{
                        "name": "Kamichita",
                        "type": 0,
                        "assets": {
                            "large_image": "kamichita_icon",
                            "large_text": "カスタムプレゼンス"
                        }
                    }],
                    "status": "online",
                    "afk": False
                }
            }))
            await asyncio.sleep(300)  # 5分ごとに更新

asyncio.run(presence())
