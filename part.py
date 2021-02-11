import json
from bot import dp, bot
from keyboard.supporting_elements import keyboard, answer, return_menu
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from helpers import prev_path, set_return_path



@dp.message_handler(state='*', commands=['start', 'help'])
async def send_welcome(message: Message, state: FSMContext):
    
    await state.finish()

    async with state.proxy() as data:
        data['path'] = '/'
    await message.reply("Введите адрес объекта", reply_markup=keyboard['/'])
    await message.reply("init", reply_markup=ReplyKeyboardMarkup([['назад'], ['Главное меню'], ['Сохранить']]))


@dp.message_handler(lambda message: message.text == 'Сохранить', state='*')
async def save_progress(message: Message, state: FSMContext):
    async with state.proxy() as data:
        print(data.__dict__['_copy'])
        with open('test.json', 'w') as f:
            json.dump(data.__dict__['_copy'], f)
    await message.reply('Прогресс сохранен')


@dp.message_handler(lambda message: message.text not in ['назад', 'Сохранить', 'Главное меню'], state='*')
async def value_saver(message: Message, state: FSMContext):
    path = ''
    async with state.proxy() as data:
        print(data['path'])
        data[data['path']] = message.text
        data = set_return_path(data)
        path = data['path']
    await message.reply('Значение сохраненно', reply_markup=keyboard[path])


@dp.message_handler(lambda message: message.text == 'назад', state='*')
async def bactrack(message: Message, state: FSMContext):
    path = ''
    async with state.proxy() as data:
        path = prev_path(data['path'])
        data['path'] = path
    await message.reply('----------------------', reply_markup=keyboard[path])


@dp.callback_query_handler(lambda callback_query: True, state='*')
async def process_callback(callback_query: CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    path = ''
    async with state.proxy() as data:
        path = data['path'] + callback_query.data + '/'
        if path in answer:
            data['path'] = path
            await bot.send_message(callback_query.message.chat.id, answer[path])
            return
        if path not in keyboard:
            data[data['path']] = callback_query.data
            path = set_return_path(data)['path']
        data['path'] = path
    await bot.send_message(callback_query.message.chat.id, '----------------------', reply_markup=keyboard[path])
