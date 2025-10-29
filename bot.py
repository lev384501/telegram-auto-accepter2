from telethon import TelegramClient, events
import asyncio
import os

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
PHONE_NUMBER = os.environ['PHONE_NUMBER']

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(PHONE_NUMBER)
    print("✅ UserBot запущен! Автоматически принимаю заявки...")
    
    @client.on(events.ChatAction)
    async def handler(event):
        if event.user_joined_request:
            try:
                await event.approve()
                print(f"✅ Принял заявку от {event.user_id}")
            except Exception as e:
                print(f"❌ Ошибка: {e}")
    
    await client.run_until_disconnected()

asyncio.run(main())
