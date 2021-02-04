from bot import dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext


class Adress(StatesGroup):
    adress = State()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await Adress.adress.set()
    await message.reply("Введите адрес объекта")


@dp.message_handler(state='*', commands='cancel')
async def send_adress(message: types.Message, state: FSMContext):
    
    current_state = await state.get_state()
    if current_state is None:
        return
    print(f'Cancelling state {current_state}')

    await state.finish()
    await message.reply('Cancelled.')


@dp.message_handler(state=Adress.adress)
async def process_name(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['adress'] = message.text

    # await state.finish()
    await message.reply('Спасибо')

