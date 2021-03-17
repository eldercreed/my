from pyrogram import Client, filters
import time
import asyncio

app = Client("my_account")


@app.on_message(filters.regex("Hola") & filters.chat("@ElderofAssasinCreed_Bot"))
def from_chat(client, message):
    time.sleep(5)
    app.send_message("@ElderofAssasinCreed_Bot","Soy el mejor /help")
    print("Run...........")

app.run()