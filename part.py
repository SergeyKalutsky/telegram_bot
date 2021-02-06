from bot import dp, bot
from keyboards import keyboard_dict, answer_dict, return_path_dict
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext


class Adress(StatesGroup):
    adress = State()
    streat = State()


def prev_path(path): return '/'.join(path.split('/')[:-2]) + '/'


@dp.message_handler(state='*', commands=['start', 'help'])
async def send_welcome(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['path'] = '/'
    await message.reply("Введите адрес объекта", reply_markup=keyboard_dict['/'])
    await message.reply("init", reply_markup=ReplyKeyboardMarkup([['назад'], ['Главное меню'], ['Сохранить']]))


@dp.message_handler(lambda message: message.text == 'Сохранить', state='*')
async def save_progress(message: Message, state: FSMContext):
    async with state.proxy() as data:
        print(data)
    await message.reply('Прогресс сохранен')


@dp.message_handler(lambda message: message.text not in ['назад', 'Сохранить', 'Главное меню'], state='*')
async def value_saver(message: Message, state: FSMContext):
    path = ''
    async with state.proxy() as data:
        data[data['path']] = message.text
        data['path'] = return_path_dict[data['path']]
        path = data['path']
    await message.reply('Значение сохраненно', reply_markup=keyboard_dict[path])


@dp.message_handler(lambda message: message.text == 'назад', state='*')
async def bactrack(message: Message, state: FSMContext):
    path = ''
    async with state.proxy() as data:
        path = prev_path(data['path'])
        data['path'] = path
    await message.reply('----------------------', reply_markup=keyboard_dict[path])


def get_keyboard(menu_items):
    keyboard = InlineKeyboardMarkup()
    for menu_item in menu_items:
        btn = InlineKeyboardButton(menu_item, callback_data=menu_item)
        keyboard.add(btn)
    return keyboard


@dp.callback_query_handler(lambda callback_query: True, state='*')
async def process_callback_button1(callback_query: CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    path = ''
    async with state.proxy() as data:
        path = data['path'] + callback_query.data + '/'
        if path in answer_dict:
            await bot.send_message(callback_query.message.chat.id, answer_dict[path])
            return
        if path not in keyboard_dict:
            data[data['path']] = callback_query.data
            path = return_path_dict[data['path']]
        data['path'] = path
    await bot.send_message(callback_query.message.chat.id, '----------------------', reply_markup=keyboard_dict[path])
