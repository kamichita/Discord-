import json
import asyncio
import websockets
import os

TOKEN = os.getenv("TOKEN"))
ICON_PATH = "icon.png"  # icon.png または icon.PNG があると仮定

async def presence():
    async with websockets.connect("wss://gateway.discord.gg/?v=9&encoding=json") as ws:
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
                            "large_image": "icon",  # ここにリッチプレゼンスのアイコン
                            "large_text": "カスタムプレゼンス"
                        }
                    }],
                    "status": "online",
                    "afk": False
                }
            }
        }))
        while True:
            await asyncio.sleep(10)

asyncio.run(presence())
