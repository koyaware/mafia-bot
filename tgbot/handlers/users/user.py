from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import USER_KEYBOARDS
from tgbot.models.models import Users, Room, GameMembers


async def user_start(message: Message):
    user = await Users.query.where(Users.tg_id == message.from_user.id).gino.first()
    if not user:
        await Users.create(tg_id=message.from_user.id)
    else:
        await message.answer(
            "Привет!\nЭто бот для игры в Мафию🤵",
            reply_markup=USER_KEYBOARDS
        )
    if "room" in message.text:
        split_text = message.text.split("_")
        owner_id, room_id = int(split_text[-2]), int(split_text[-1])
        found_room: Room = await Room.query.where(
            Room.owner == owner_id).where(
            Room.Id == room_id).where(
            Room.active_status == True).where(
            Room.busy == False
        ).gino.first()
        if not found_room:
            await message.answer("Комната не найдена.\nВозможно игра завершилась или запустилась.")
            return
        current_member = await GameMembers.query.where(
            GameMembers.user_id == message.from_user.id
        ).gino.first()
        if current_member and current_member.is_playing:
            await message.answer("Вы уже находитесь в другой комнате.")
            return
        if not current_member:
            await GameMembers.create(
                user_id=message.from_user.id, room_id=room_id
            )
        else:
            await current_member.update(is_playing=True).apply()
        username = message.from_user.username
        await message.bot.send_message(found_room.owner, f"В комнату присоединился участник:\n{f'Его ник:  @{username}'if username else f'Его имя:  {message.from_user.full_name}'}"
        )
        await message.answer("Вы успешно присоединились в комнату.\nЖдем начала игры.")


def register_user(dp: Dispatcher):
    dp.register_message_handler(
        user_start, commands=["start"], state="*", commands_prefix="!/"
    )
