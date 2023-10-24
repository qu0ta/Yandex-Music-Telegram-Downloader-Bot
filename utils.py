import datetime
from typing import Union

from aiogram.types import Message

from db.db_session import session, User


def add_user(user_id: int, msg: Message) -> None:
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    username = msg.from_user.username
    today = datetime.datetime.today()

    user = User(
        tg_id=user_id,
        first_name=first_name,
        last_name=last_name,
        username=username,
        registration_date=today
    )
    session.add(user)
    session.commit()


def get_user(user_id: int) -> Union[User, None]:
    user = session.query(User).get(user_id)
    return user
