import discord
import asyncio
import os
import sys
from datetime import timedelta

# 從 Railway 環境變數讀取
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1452691099960344734   # 你的頻道 ID

intents = discord.Intents.default()
bot = discord.Client(intents=intents)   # 使用 Client 即可，不需要 commands.Bot

async def send_daily_poll():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if channel is None:
            print("❌ 找不到頻道，請確認 CHANNEL_ID 是否正確")
            return

        print("📊 正在發送每日 Poll...")
        
        poll = discord.Poll(
            question="22:00",                    # Poll 標題
            duration=timedelta(hours=4)          # 持續 4 小時
        )
        poll.add_answer(text="✅ Yes")
        poll.add_answer(text="⏰ Late")
        poll.add_answer(text="❌ Skip")

        await channel.send(
            content="@everyone",
            poll=poll,
            allowed_mentions=discord.AllowedMentions(everyone=True)
        )
        
        print("✅ Poll 已成功發送！")
        
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
    finally:
        # 發送完畢後等待幾秒確保訊息送出，然後關閉 bot
        await asyncio.sleep(8)
        await bot.close()


@bot.event
async def on_ready():
    print(f"✅ Bot 已登入：{bot.user} (ID: {bot.user.id})")
    await send_daily_poll()   # 登入後立刻執行任務並結束


# ==================== 啟動程式 ====================
if __name__ == "__main__":
    if not TOKEN:
        print("❌ 未找到 TOKEN 環境變數！請在 Railway Variables 中設定 TOKEN")
        sys.exit(1)
    
    print("🚀 開始執行每日 Poll 任務...")
    bot.run(TOKEN)