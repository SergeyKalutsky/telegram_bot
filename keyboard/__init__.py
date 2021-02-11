from aiogram.types.inline_keyboard import InlineKeyboardButton as InlineKeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardMarkup as InlineKeyboardMarkup


def get_keyboard(menu_items):
    keyboard = InlineKeyboardMarkup()
    for menu_item in menu_items:
        btn = InlineKeyboardButton(menu_item, callback_data=menu_item)
        keyboard.add(btn)
    return keyboard

keyboard = {}
answer = {}
return_menu = {}
