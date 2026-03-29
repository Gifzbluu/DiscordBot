import discord
from discord.ext import commands
from datetime import timedelta
import os  # 用環境變數安全存TOKEN

# 讀取TOKEN
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 你的頻道ID  # 整數形式，不用引號

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        print("❌ 找不到頻道（檢查 CHANNEL_ID 或權限）")
        return

    print("📊 發送 Poll（即時測試）...")

    poll = discord.Poll(
        question="22:00",
        duration=timedelta(hours=1)  # 測試用，1小時最安全
    )

    poll.add_answer(text="✅ Yes")
    poll.add_answer(text="⏰ Late")
    poll.add_answer(text="❌ Skip")

    await channel.send(
        content="@everyone",
        poll=poll,
        allowed_mentions=discord.AllowedMentions(everyone=True)
    )

    print("✅ Poll 已發送（官方 UI）")

bot.run(TOKEN)