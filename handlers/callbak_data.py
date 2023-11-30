import asyncio
import json

from aiogram import types
from misc import dp, bot
from .sqlit import change_status,get_username,update_status
import random

text_stop = """<b>Аяяй я смотрю, кто-то решил
пошалить 😏

Сначала посмотри видео, а потом нажимай🙏🙃</b>"""



text_dogon = """<b>Аяяй я смотрю, кто-то решил
пошалить 😏

Сначала посмотри видео, а потом нажимай🙏🙃</b>"""

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1002028107373

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


time_flag = 1 # 0 - режим разработчика, где отключены тайм.слипы

@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    await bot.answer_callback_query(call.id)

    if call.data == 'go_1':
        update_status(call.message.chat.id, 1)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='ДАВАЙ🧐', callback_data='go_2')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 52)
        if time_flag == 1:
            await asyncio.sleep(3)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 53)
        if time_flag == 1:
            await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 54, reply_markup=markup)


    if call.data == 'go_2':
        update_status(call.message.chat.id, 2)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='А КАК?🧐', callback_data='go_3')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=56, reply_markup=markup)



    if call.data == 'go_3':
        update_status(call.message.chat.id, 3)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='ДААА', callback_data='go_4')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=58,reply_markup=markup)



    if call.data == 'go_4':
        update_status(call.message.chat.id, 4)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='💸 СПРИНТ 💸', callback_data='go_5')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=61)
        if time_flag == 1:
            await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=62, reply_markup=markup)


    if call.data == 'go_5':
        update_status(call.message.chat.id, 5)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔥НАЧИНАЕМ🔥', callback_data='go_6')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id= 64)
        if time_flag == 1:
            await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=68, reply_markup=markup)



    if call.data == 'go_6':
        update_status(call.message.chat.id, 6)
        await state.update_data(v1='stop')

        markup = types.InlineKeyboardMarkup()
        bat_1 = types.InlineKeyboardButton(text='🔫ДАЛЬШЕ🔫', callback_data='go_7')
        markup.add(bat_1)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=70,reply_markup=markup)
        if time_flag == 1:
            await asyncio.sleep(30)  # 60 сек
        await state.update_data(v1='start')

        # поставить таймер на 30  минут!!
        if time_flag == 1:
            await asyncio.sleep(1800)  # если не нажимал на кнопку в течении 30 минут (1800)
        if ((await state.get_data())['v1']) != 'ready':
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=72)
            await call.message.answer("""Так кайфует тот, кто уже посмотрел видосик выше ☝️ 

<b>Погнали смотреть🙄</b>""", parse_mode='html')



    if call.data == 'go_7':
        try:
            if ((await state.get_data())['v1']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 7)
            await state.update_data(v1='ready')
            await state.update_data(v2='stop')

            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='🤓ПРОЙТИ ТЕСТ🤓', callback_data='go_8')
            markup.add(bat_a)


            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=74,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(60)  # (60 сек)
            await state.update_data(v2='start')

            if time_flag == 1:
                await asyncio.sleep(1800)  # если не нажимал на кнопку в течении 30 минут
            if ((await state.get_data())['v2']) != 'ready':
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=80)
                await call.message.answer("""Вот так, чувствует себя человек, который посмотрел видео и продолжил действовать!

<b>Почему ты забиваешь на свое будущее?</b>

Гоо смотреть и зарабатывать вместе🤗🤑""", parse_mode='html')



    if call.data == 'go_8':
        try:
            if ((await state.get_data())['v2']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 8)
            await state.update_data(v2='ready')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='1️⃣', callback_data='go_9')
            bat_2 = types.InlineKeyboardButton(text='2️⃣', callback_data='answer_false')
            bat_3 = types.InlineKeyboardButton(text='3️⃣', callback_data='answer_false')
            markup.add(bat_1, bat_2, bat_3)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 82,reply_markup=markup)



    if call.data == 'answer_false':
        await bot.send_message(chat_id=call.message.chat.id, text= "<b>Нет, это не арбитраж трафика. Пересмотри видео и попробуй ещё раз🙃</b>", parse_mode='html')

    if call.data == 'go_9':
        update_status(call.message.chat.id, 9)
        await bot.send_message(chat_id=call.message.chat.id, text="""<b>Красава😎 Двигаемся дальше🚀</b>""",parse_mode='html')
        if time_flag == 1:
            await asyncio.sleep(1)

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='⚡️ЕДЕМ ДАЛЬШЕ⚡️', callback_data='go_10')
        markup.add(bat_a)

        await state.update_data(v3='stop')
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=85, reply_markup=markup)
        if time_flag == 1:
            await asyncio.sleep(60)  # (90 сек)
        await state.update_data(v3='start')

        if time_flag == 1:
            await asyncio.sleep(1800)  # если не нажимал на кнопку в течении 30 минут
        if ((await state.get_data())['v3']) != 'ready':
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=88)




    if call.data == 'go_10':
        try:
            if ((await state.get_data())['v3']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 10)
            await state.update_data(v3='ready')
            if time_flag == 1:
                await asyncio.sleep(1)

            await bot.send_message(chat_id=call.message.chat.id, text="""<b>Сейчас создадим с тобой телеграм канал, который в дальнейшем пригодится для заработка😎🤑</b>""",parse_mode='html')

            if time_flag == 1:
                await asyncio.sleep(1)


            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='🫡ГОТОВО✔️', callback_data='go_11')
            markup.add(bat_a)

            await state.update_data(v4='stop')
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=92,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(30)  # (10 сек)
            await state.update_data(v4='start')

            if time_flag == 1:
                await asyncio.sleep(1800)  # если не нажимал на кнопку в течении 30 минут
            if ((await state.get_data())['v4']) != 'ready':
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=95)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=96)




    if call.data == 'go_11':
        try:
            update_status(call.message.chat.id, 11)
            await state.update_data(v4='ready')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=97)

            if time_flag == 1:
                await asyncio.sleep(180) # 4 минуты
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=101)


            if time_flag == 1:
                await asyncio.sleep(360)  # 6 минут
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=103)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=104)


            if time_flag == 1:
                await asyncio.sleep(3600)  # 60 минут
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=106)


            if time_flag == 1:
                await asyncio.sleep(5400)  # 90 минут
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=108)

            if time_flag == 1:
                await asyncio.sleep(86400)  # 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=110)


            if time_flag == 1:
                await asyncio.sleep(21600)  # 6 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=112)


            if time_flag == 1:
                await asyncio.sleep(43200) # 12 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=114)


            if time_flag == 1:
                await asyncio.sleep(43200)  # 12 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=116)



            if time_flag == 1:
                await asyncio.sleep(43200)  # 12 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=118)


            if time_flag == 1:
                await asyncio.sleep(21600)  # 6 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=120)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=121)



            if time_flag == 1:
                await asyncio.sleep(86400)  # 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=123)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=124)


            if time_flag == 1:
                await asyncio.sleep(86400)  # 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=126)

        except:
            pass
