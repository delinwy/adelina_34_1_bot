from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        'start questionnaire <3',
        callback_data='start_questionnaire'
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        '- :; yes!!',
        callback_data='okay_yes'
    )
    no_button = InlineKeyboardButton(
        '- :; no :(',
        callback_data='okay_no'
    )
    markup.add(yes_button)
    markup.add(no_button)
    return markup

