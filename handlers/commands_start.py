from aiogram import types
from misc import dp, bot
from .sqlit import reg_user, get_username
from .callbak_data import reg_p
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1002028107373
reg_user(1,'1')  # Запуск в БД


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    if len(message.text) == 6:
        reg_user(message.chat.id, '1')  # Регистрация в БД
    else:
        reg_user(message.chat.id, message.text[7:])  # Регистрация в БД

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ГООО🏍', callback_data='go_1')
    markup.add(bat_a)

    await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 50,reply_markup=markup)

