from aiogram.types import Message
from aiogram import Dispatcher

from init import AUDIO_DIR
from messages import WELCOME_MESSAGE
from utils import get_user, add_user


def register_base_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(register_user, commands='start', state='*')


async def register_user(msg: Message) -> None:
    user_id = msg.from_user.id
    user = get_user(user_id)
    if user is None:
        add_user(user_id, msg)

    await msg.answer(WELCOME_MESSAGE)
