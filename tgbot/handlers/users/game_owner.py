from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.commands.user_commands import Commands
from tgbot.data.links import get_room_link
from tgbot.keyboards.reply import OWNER_ENTER_BUTTON, START_GAME_KEYBOARD
from tgbot.misc.states import RoomOwnerEnterState, GameLoopState
from tgbot.models.models import Room, GameMembers


async def new_game(message: Message, state: FSMContext):
    bot = await message.bot.get_me()
    check_room = await Room.query.where(Room.owner == message.from_user.id).gino.first()
    if not check_room:
        await Room.create(
            name=f"{message.from_user.full_name}_{message.from_user.id}",
            owner=message.from_user.id
        )
    else:
        await check_room.update(active_status=True).apply()
    await RoomOwnerEnterState.activate_room.set()
    await state.update_data(activate_room=check_room==check_room.Id)
    await message.answer(
        f"Игровая комната создана.\nСсылка на игровую комнату: {get_room_link(check_room.Id, message.from_user.id, bot.username)}",
        reply_markup=OWNER_ENTER_BUTTON
    )


async def enter_room(message: Message, state= FSMContext):
    async with state.proxy() as data:
        room_id = data['activate_room']
    members = GameMembers.query.where(
        GameMembers.user_id == message.from_user.id
    ).gino.first()
    if not members:
        await GameMembers.create(
            room_id=room_id,
            user_id=message.from_user.id
        )
    await state.finish()
    await GameLoopState.wait_start.set()
    await message.answer("Вы вошли в комнату.\nЖдем других игроков.\nНажмите старт игры для начала игры.",
                         reply_markup=START_GAME_KEYBOARD
                         )


async def start_game(message: Message, state: FSMContext):
    await message.answer("Игра началась")


def register_game_owner_handlers(dp: Dispatcher):
    dp.register_message_handler(
        new_game, text=[Commands.new_game.value])

    dp.register_message_handler(
        enter_room, state=RoomOwnerEnterState.activate_room,
        text=[Commands.owner_enter.value])

    dp.register_message_handler(
        start_game, state=GameLoopState.wait_start,
        text=[Commands.start_game.value])

