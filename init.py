import os
from yandex_music import ClientAsync
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv('.env')
bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())
AUDIO_DIR = os.path.join(os.path.dirname(__file__), 'audio/')
IMG_DIR = os.path.join(os.path.dirname(__file__), 'img/')

