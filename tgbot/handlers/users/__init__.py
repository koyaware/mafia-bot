from aiogram import Dispatcher

from .user import register_user


def register_all_user_handlers(dp: Dispatcher):
    register_user(dp)
