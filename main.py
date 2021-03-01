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


@dp.message_handler(content_types=['photo'], state='*',)
async def handle_docs_photo(message: Message, state: FSMContext):

    img_fname = make_img_fname()
    img_path = os.path.join('data/photo', img_fname)

    async with state.proxy() as data:
        put_key_json(data['path'], data, img_fname, photo=True)

        data['path'] = prev_path(data['path'])
    await message.photo[-1].download(img_path)
    await message.reply('Фото сохранено')
    await message.reply(data['path'], reply_markup=keyboard[data['path']])


@dp.message_handler(state='*', commands=['start', 'help'])
async def send_welcome(message: Message, state: FSMContext):

    await state.finish()

    async with state.proxy() as data:
        data['path'] = '/'
        if 'photo' not in data:
            data['photo'] = {}
    await message.reply("Введите адрес объекта", reply_markup=keyboard['/'])
    await message.reply("init", reply_markup=ReplyKeyboardMarkup([['/start'], ['Назад'], ['Сохранить'], ['Перегрузить']]))


@dp.message_handler(lambda message: message.text == 'Сохранить', state='*')
async def save_progress(message: Message, state: FSMContext):
    async with state.proxy() as data:
        print(data.__dict__['_copy'])
        with open('data/test.json', 'w') as f:
            json.dump(data.__dict__['_copy'], f)
    await message.reply('Прогресс сохранен')

@dp.message_handler(lambda message: message.text == 'Перегрузить', state='*')
async def load_progress(message: Message, state: FSMContext):
    async with state.proxy() as data:
        with open('data/test.json', 'r') as f:
            ldata = json.load(f)
            for key in ldata:
                data[key] = ldata[key]
    # print(type(data))
    print(data)
    await message.reply('Прогресс загружен с последнего сохранения')


@dp.message_handler(lambda message: message.text not in ['Назад', 'Сохранить', 'Главное меню', 'Перегрузить'], state='*')
async def value_saver(message: Message, state: FSMContext):
    p_comm = '/Общие сведения/Площадь/Общая/'
    p_live = '/Общие сведения/Площадь/Жилая/'
    async with state.proxy() as data:
        if data['path'] in [p_comm, p_live]:
            if not message.text.isdigit():
                await message.reply(f'Введенно неверное значение, повторите еще раз')
                return

        put_key_json(data['path'], data, message.text)
        data['path'] = prev_path(data['path'])
    await message.reply(f'Значение сохраненно {message.text}')
    await message.reply(data['path'], reply_markup=keyboard[data['path']])


@dp.message_handler(lambda message: message.text == 'Назад', state='*')
async def bactrack(message: Message, state: FSMContext):
    path = ''
    async with state.proxy() as data:
        path = prev_path(data['path'])
        data['path'] = path
    await message.reply(data['path'], reply_markup=keyboard[path])


@dp.callback_query_handler(lambda callback_query: True, state='*')
async def process_callback(callback_query: CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    path = ''
    async with state.proxy() as data:

        if callback_query.data == 'Нежилая':
            p_comm = '/Общие сведения/Площадь/Общая/'
            p_live = '/Общие сведения/Площадь/Жилая/'
            if p_comm in data and p_live in data:

                area = calculate_area(data)
                keyboard['/Общие сведения/Площадь/Нежилая/'] = get_keyboard(
                    [f'рассчитано {area} м^2 правильно?'])
                keyboard[f'/Общие сведения/Площадь/Нежилая/рассчитано {area} м^2 правильно?/'] = get_keyboard([
                                                                                                              'Да', 'Нет'])
                answer[f'рассчитано {area} м^2 правильно?/Нет'] = "Введите правильное значение"
            else:
                path = prev_path(data['path'])
                data['path'] = path
                msg = 'Значения для жилой и нежилой не введены'
                await bot.send_message(callback_query.message.chat.id,  msg, reply_markup=keyboard[path])
                return

        path = data['path'] + callback_query.data + '/'
        for i in range(-3, 0):
            key = '/'.join(path[:-1].split('/')[i:])
            if key in answer:
                data['path'] = path
                await bot.send_message(callback_query.message.chat.id, answer[key])
                return

        if path not in keyboard:
            put_key_json(data['path'], data, callback_query.data)
            path = prev_path(data['path'])
            await bot.send_message(callback_query.message.chat.id, f'Значение сохраненно: {callback_query.data}')

        data['path'] = path
    await bot.send_message(callback_query.message.chat.id,  data['path'], reply_markup=keyboard[path])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
