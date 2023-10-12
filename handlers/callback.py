import sqlite3

from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_one_keyboard
from database.sql_commands import Database


async def start_questionnaire(call: types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text='r u okay?',
        reply_markup=await questionnaire_one_keyboard()
    )


async def yes_answer(call: types.CallbackQuery):
    print(call)
    try:
        Database().sql_insert_user_response(
            user_id=call.from_user.id,
            question='r u okay?',
            answer='yes',
        )
    except sqlite3.IntegrityError:
        pass

    await bot.send_message(
        chat_id=call.message.chat.id,
        text='glad u r okay!^^',
    )


async def no_answer(call: types.CallbackQuery):
    print(call)
    try:
        Database().sql_insert_user_response(
            user_id=call.from_user.id,
            question='r u okay?',
            answer='no',
        )
    except sqlite3.IntegrityError:
        pass

    await bot.send_message(
        chat_id=call.message.chat.id,
        text='take care of yourself!^^',
    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire,
                                       lambda call: call.data == 'start_questionnaire')
    dp.register_callback_query_handler(yes_answer,
                                       lambda call: call.data == 'okay_yes')
    dp.register_callback_query_handler(no_answer,
                                       lambda call: call.data == 'okay_no')
