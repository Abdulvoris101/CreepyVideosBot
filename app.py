import asyncio
from dotenv import load_dotenv
import os
from aiogram import Dispatcher, Bot, types
from aiogram.enums import ParseMode
import logging
import sys

load_dotenv()

BOT_TOKEN = os.environ.get("TOKEN")

dp = Dispatcher()




async def main() -> None:
    from handlers import dp

    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)

    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())