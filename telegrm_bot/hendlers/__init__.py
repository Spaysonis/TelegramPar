from telegrm_bot.hendlers.start import router as start_router
from telegrm_bot.config import dp


dp.include_router(start_router)
