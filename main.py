import asyncio

from telegrm_bot.config import bot
from telegrm_bot.hendlers import dp



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())