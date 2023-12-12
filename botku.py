import asyncio
import logging
from datetime import datetime
from telethon import TelegramClient, events

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Konfigurasi
API_ID = 2224425
API_HASH = '997e6338c87f9e5540fe857d6f1b145c'

client = TelegramClient("not_not", API_ID, API_HASH).start()
logger.info(f">>> Bot is running..")

@client.on(events.NewMessage(incoming=True))
async def private_message(event):
    """Tanggapan terhadap pesan baru."""
    if event.is_private:
        username = (await event.get_sender()).first_name
        waktu = datetime.now().strftime("%H:%M:%S")
        new_line = "/n"
        durasi = 999999999999999999999999999999999999999 * 999999999999999999999999999999999999999
        async with client.action(event.chat_id, 'typing'):
            logger.info(f">>> ({waktu}) Chat baru dari {username}")
            await asyncio.sleep(durasi)

# Menjalankan klien Telethon
client.run_until_disconnected()
