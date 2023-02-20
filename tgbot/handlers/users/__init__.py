from aiogram import Dispatcher

from .game_owner import register_game_owner_handlers
from .user import register_user


def register_all_user_handlers(dp: Dispatcher):
    register_user(dp)
    register_game_owner_handlers(dp)
