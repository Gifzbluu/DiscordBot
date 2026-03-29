import discord
from discord.ext import commands, tasks
from datetime import time, timedelta
import os

# 讀取TOKEN
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1452691099960344734  # 整數形式，不用引號

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 每天 18:00 UTC+8 = 10:00 UTC
@tasks.loop(time=time(hour=10, minute=0))
async def daily_poll():
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        print("❌ 找不到頻道")
        return

    print("📊 發送每日 Poll...")

    poll = discord.Poll(
        question="22:00",            # Poll 標題
        duration=timedelta(hours=4)  # 官方 Poll UI 持續時間
    )
    poll.add_answer(text="✅ Yes")
    poll.add_answer(text="⏰ Late")
    poll.add_answer(text="❌ Skip")

    await channel.send(
        content="@everyone",
        poll=poll,
        allowed_mentions=discord.AllowedMentions(everyone=True)
    )

    print("✅ Poll 已發送")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    daily_poll.start()

bot.run(TOKEN)

from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def home():
    return "Bot is alive!"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# 啟動 Web Server 在背景執行
t = Thread(target=run)
t.start()