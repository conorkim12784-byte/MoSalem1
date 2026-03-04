import logging
import asyncio

from pyrogram import Client, idle
from pyrogram.errors.exceptions.bad_request_400 import BadRequest
from pyrogram.errors import BadMsgNotification

from config import TOKEN, disabled_plugins, log_chat, API_ID, API_HASH
from utils import get_restarted, del_restarted

with open("version.txt") as f:
    version = f.read().strip()


async def start_bot():
    client = Client("Cv_BeTa", API_ID, API_HASH,
                    bot_token=TOKEN,
                    workers=24,
                    parse_mode="html",
                    plugins=dict(root="plugins", exclude=disabled_plugins))
    
    while True:
        try:
            await client.start()
            wr = get_restarted()
            del_restarted()
            try:
                print("Bot started\n"
                      f"Version: {version}")
                if wr:
                    await client.edit_message_text(wr[0], wr[1], "Restarted successfully.")
            except BadRequest:
                logging.warning("Unable to send message to log_chat.")
            await idle()
            break
        except BadMsgNotification:
            logging.warning("BadMsgNotification: time sync issue, retrying in 5 seconds...")
            try:
                await client.stop()
            except Exception:
                pass
            await asyncio.sleep(5)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            try:
                await client.stop()
            except Exception:
                pass
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(start_bot())
