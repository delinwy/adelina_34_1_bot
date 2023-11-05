from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        'start questionnaire <3',
        callback_data='start_questionnaire'
    )
    registration_button = InlineKeyboardButton(
        'registration <3',
        callback_data='fsm_start'
    )
    my_profile_button = InlineKeyboardButton(
        'my profile <3',
        callback_data='my_profile'
    )
    random_profile_button = InlineKeyboardButton(
        'view profile <3',
        callback_data='random_profile'
    )
    reference_menu_button = InlineKeyboardButton(
        'referral menu <3',
        callback_data='reference_menu'
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profile_button)
    markup.add(reference_menu_button)
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


async def admin_keyboard():
    markup = InlineKeyboardMarkup()
    admin_user_list_button = InlineKeyboardButton(
        'User List',
        callback_data='admin_user_list'
    )
    markup.add(admin_user_list_button)
    return markup


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    user_form_like_button = InlineKeyboardButton(
        'like ^^',
        callback_data=f'user_form_like_{owner_tg_id}'
    )
    user_form_dislike_button = InlineKeyboardButton(
        'dislike',
        callback_data='random_profile'
    )
    markup.add(user_form_like_button)
    markup.add(user_form_dislike_button)
    return markup


async def edit_delete_form_keyboard():
    markup = InlineKeyboardMarkup()
    edit_form_button = InlineKeyboardButton(
        'edit ✏',
        callback_data='fsm_start'
    )
    delete_form_button = InlineKeyboardButton(
        'delete 🗑️',
        callback_data='delete_profile'
    )
    markup.add(edit_form_button)
    markup.add(delete_form_button)
    return markup


async def my_profile_register():
    markup = InlineKeyboardMarkup()
    registration_button = InlineKeyboardButton(
        'registration <3',
        callback_data='fsm_start'
    )
    markup.add(registration_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_link_button = InlineKeyboardButton(
        'referral link <3',
        callback_data='reference_link'
    )
    reference_list_button = InlineKeyboardButton(
        'referral list <3',
        callback_data='reference_list'
    )
    markup.add(reference_link_button)
    markup.add(reference_list_button)
    return markup


