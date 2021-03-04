"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage

API_TOKEN = ''
with open('token.txt', 'r') as f:
    API_TOKEN = f.readline()


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
storage = RedisStorage('localhost', 6379, db=1)

# storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

