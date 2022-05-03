#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [BotStatus Telegram bot by TeLe TiPs] (https://github.com/teletips/Powerful_BotStatus-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/Powerful_BotStatus-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "botstatus_teletips",
    api_id = 7436880,
    api_hash = "09e42655b8fd773801f705b01271a011",
    session_string = "BQDBUkCga3a4K027MsUZ9NtDuCVqu3KoXQ2jvG9d07rlMzbTAXK3M4iiRWjEuy_SIRAA7Ljhd_qcCFIiDZlppQ5qE90FXhU9iYKW-kK4yI95G5PmDNLroxZdZ03nsoHv_-5DxR4ami0O05OLSXtvs4uHzUei_36uhTO-3Qi-7OrU4vR2zI-XqzacHBfnsC5xexl11TlmzN1UonZOY7LC2vbaYWx6PAfSsnnZXg8mmLQcdZR9p7vW--IUurvDx3ZZYxkZXSOIyo6D64VS5Zeo1KfRhxJRxeo6Dz40XP0j2sOS4NFzXS2Az2M_aZ_JrfBZ9YuW0svWjDr1rDUuKzTyqkQwc-RWAQA"
)
TIME_ZONE = "Asia/Kolkata"
BOT_LIST = ["CountdownTimerTestBot"]
CHANNEL_OR_GROUP_ID = -1001539307717
MESSAGE_ID = 2
BOT_ADMIN_IDS = 1944344065
async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_teletips = f"📊 **<u>LIVE BOT STATUS</u>**\n\n**💬 {CHANNEL_OR_GROUP_TYPE}**: {CHANNEL_OR_GROUP_NAME}"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(10)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n🔴 **STATUS**: down ❌"
                            async for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n🟢 **STATUS**: alive ✅"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ Updates every 45min - Powered by Powerful Bot Status</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(6300)
                        
app.run(main_teletips())

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
