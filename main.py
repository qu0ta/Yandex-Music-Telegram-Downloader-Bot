import os

from aiogram import executor, Dispatcher
from init import dp
from handlers import register_base_handlers, register_get_handlers


def on_startup(_):
    print("Бот был запущен.")


def on_shutdown(_):
    print("Бот был отключен.")


def register_handlers() -> None:
    register_base_handlers(dp)
    register_get_handlers(dp)


if __name__ == '__main__':
    register_handlers()
    executor.start_polling(dp, skip_updates=True)  # , on_startup=on_startup, on_shutdown=on_shutdown)
