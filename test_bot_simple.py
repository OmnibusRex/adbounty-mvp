import asyncio
from telegram import Bot

BOT_TOKEN = "8578390491:AAHA1Vme9Y8fUXe7yrV8alzaaBQ6On96cpI"

async def test():
    bot = Bot(token=BOT_TOKEN)
    me = await bot.get_me()
    print(f"Bot funcionando: {me.first_name} (@{me.username})")

asyncio.run(test())
