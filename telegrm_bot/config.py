
from aiogram import Bot, Dispatcher

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

dp = Dispatcher()
bot = Bot(token=TOKEN)








