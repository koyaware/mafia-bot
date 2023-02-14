from aiogram import Dispatcher

from tgbot.handlers.admin.admin import register_admin


def register_admin_handlers(dp: Dispatcher):
    register_admin(dp)
