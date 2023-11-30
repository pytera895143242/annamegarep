from aiogram import types
from misc import dp,bot
from .sqlit import get_data_tag
import asyncio

ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID_3 = 941730379 #Джейсон
ADMIN_ID_4 = 678623761 # Бекир

ADMIN_ID =[ADMIN_ID_1,ADMIN_ID_2,ADMIN_ID_3,ADMIN_ID_4,1079844264,807911349, 6789001261]


@dp.message_handler(content_types=['text', 'photo', 'video_note', 'animation', 'document', 'video','file'])
async def all_message(message: types.Message):
    if message.chat.id in ADMIN_ID:
        try:
            id = message.forward_from.id
            data = get_data_tag(id)
            await message.answer(f"Этот человек от {data}")
        except:
            await message.answer("Скорее всего у пользователя закрыт акк")
