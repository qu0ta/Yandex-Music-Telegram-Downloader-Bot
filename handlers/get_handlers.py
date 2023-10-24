import os
from aiogram import Dispatcher
from aiogram.types import Message
from yandex_music import ClientAsync

from init import bot, AUDIO_DIR
from messages import *
from utils import get_user, add_user


def register_get_handlers(dp: Dispatcher):
    dp.register_message_handler(main_get_handler, commands='get')


async def main_get_handler(msg: Message):
    user_id = msg.from_user.id
    user = get_user(user_id)
    if user is None:
        add_user(user_id, msg)

    args = msg.get_args()
    if not args:
        await msg.answer(MAIN_GET_NOT_ENOUGH_MESSAGE)
        return
    to_delete = await msg.answer('Скачивание...')
    track_name = args.title()

    client = await ClientAsync(os.getenv("YANDEX_TOKEN")).init()
    res = (await client.search(track_name)).best

    await res.result.download_async(AUDIO_DIR + track_name + '.mp3')
    await msg.answer_audio(open(AUDIO_DIR + f'{track_name}.mp3', 'rb').read(), title=track_name, caption=f"""
Встрeчается в альбомах: <b>{res.result.albums[0].title}</b>
Исполнитель: <b>{res.result.artists[0].name}</b>""", parse_mode="HTML", protect_content=True)

    await bot.delete_message(chat_id=user_id, message_id=to_delete.message_id)
