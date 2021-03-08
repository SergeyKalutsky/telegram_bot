import logging
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage


con = sqlite3.connect('web/app/app/db/project.db')

API_TOKEN = ''
with open('token.txt', 'r') as f:
    API_TOKEN = f.readline()


# Configure logging
logging.basicConfig(filename='debug.log',
                    filemode='a',
                    format='%(asctime)s, %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

# Initialize bot and dispatcher
storage = RedisStorage('localhost', 6379, db=1)

# storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

con.execute('SELECT * FROM jobs WHERE id = 20').fetchone()