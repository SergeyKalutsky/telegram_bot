import os
import json
from bot import dp, bot
from answers import answer
from aiogram import executor
from helpers import prev_path, calculate_area, make_img_fname, put_key_json
from keyboard import get_keyboard
from keyboard.appartments import keyboard
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

BASEDIR = 'web/app/app/static/data'


def end_path(path):
    k = keyboard[path]
    for val in k.values['inline_keyboard']:
        if path + val[0].text + '/' in keyboard:
            return False
    return True

@dp.message_handler(content_types=['photo'], state='*',)
async def handle_docs_photo(message: Message, state: FSMContext):

    async with state.proxy() as data:
        if 'id' not in data:
            await message.reply("Не выбран id задачи. Пришлите его в ответ")
            return

        img_fname = make_img_fname()
        img_path = os.path.join(BASEDIR, data['id'], 'photo', img_fname)

        put_key_json(data['path'], data, img_fname, photo=True)

        data['path'] = prev_path(data['path'])
    await message.photo[-1].download(img_path)
    await message.reply('Фото сохранено')
    await message.reply(data['path'], reply_markup=keyboard[data['path']])


@dp.message_handler(lambda message: message.text == 'Сохранить', state='*')
async def save_progress(message: Message, state: FSMContext):
    async with state.proxy() as data:
        if 'id' not in data:
            await message.reply("Не выбран id задачи. Пришлите его в ответ")
            return

        print(data.__dict__['_copy'])
        with open(os.path.join(BASEDIR, data['id'], 'data.json'), 'w') as f:
            json.dump(data.__dict__['_copy'], f)
    await message.reply('Прогресс сохранен')


@dp.message_handler(state='*', commands=['start', 'help'])
async def start(message: Message, state: FSMContext):

    async with state.proxy() as data:
        if 'id' not in data:
            await message.reply("Не выбран id задачи. Пришлите его в ответ")
            return
        data['path'] = '/'

    await message.reply("Введите адрес объекта", reply_markup=keyboard['/'])
    await message.reply("init", reply_markup=ReplyKeyboardMarkup([['/start'], ['Назад'], ['Сохранить'], ['Выход']]))


@dp.message_handler(lambda message: message.text == 'Выход', state='*')
async def exit(message: Message, state: FSMContext):
    await state.finish()
    await message.reply('Работа завершена')


@dp.message_handler(lambda message: message.text not in ['Назад', 'Сохранить', 'Главное меню', 'Выход'], state='*')
async def value_saver(message: Message, state: FSMContext):
    async with state.proxy() as data:
        if 'id' not in data:
            if message.text.isdigit():
                data['id'] = message.text
                if not os.path.exists(os.path.join(BASEDIR, data['id'])):
                    os.mkdir(os.path.join(BASEDIR, data['id']))
                    os.mkdir(os.path.join(BASEDIR, data['id'], 'photo'))
                else:
                    path = os.path.join(BASEDIR, data['id'], 'data.json')
                    if os.path.exists(path):
                        with open(path, 'r') as f:
                            ldata = json.load(f)
                            for key in ldata:
                                data[key] = ldata[key]
                if 'photo' not in data:
                    data['photo'] = {}
                await message.reply(f"Выбран id задачи {message.text}")
                return
            else:
                await message.reply("Не выбран id задачи. Пришлите его в ответ")
                return
        
        for i in range(-3, 0):
            key = '/'.join(data['path'][:-1].split('/')[i:])
            if key in answer:
                put_key_json(data['path'], data, message.text)
                data['path'] = prev_path(data['path'])
                await message.reply(f'Значение сохраненно {message.text}')
                await message.reply(data['path'], reply_markup=keyboard[data['path']])
                return

    await message.reply(prev_path(data['path']), reply_markup=keyboard[prev_path(data['path'])])


@dp.message_handler(lambda message: message.text == 'Назад', state='*')
async def backtrack(message: Message, state: FSMContext):
    path = ''
    async with state.proxy() as data:
        if 'id' not in data:
            await message.reply("Не выбран id задачи. Пришлите его в ответ")
            return

        path = prev_path(data['path'])
        data['path'] = path
    await message.reply(data['path'], reply_markup=keyboard[path])


@dp.callback_query_handler(lambda callback_query: True, state='*')
async def process_callback(callback_query: CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    path = ''
    async with state.proxy() as data:
        if 'id' not in data:
            await bot.send_message(callback_query.message.chat.id, "Не выбран id задачи. Пришлите его в ответ")
            return

        path = data['path'] + callback_query.data + '/'
        for i in range(-3, 0):
            key = '/'.join(path[:-1].split('/')[i:])
            if key in answer:
                data['path'] = path
                await bot.send_message(callback_query.message.chat.id, answer[key])
                return

        if path not in keyboard:
            if not end_path(data['path']):
                await bot.send_message(callback_query.message.chat.id,  data['path'], reply_markup=keyboard[path])
                return

            put_key_json(data['path'], data, callback_query.data)
            path = prev_path(data['path'])
            await bot.send_message(callback_query.message.chat.id, f'Значение сохраненно: {callback_query.data}')

        data['path'] = path
    await bot.send_message(callback_query.message.chat.id,  data['path'], reply_markup=keyboard[path])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
