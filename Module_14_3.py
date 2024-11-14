from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboard_m_14_3 import *
import Texts_m_14_3

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer(f'Название: {Texts_m_14_3.product1} | Описание: {Texts_m_14_3.product_description1}'
                         f' | Цена: {Texts_m_14_3.price1}')
    with open('files/1.png', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(f'Название: {Texts_m_14_3.product2} | Описание: {Texts_m_14_3.product_description2}'
                         f' | Цена: {Texts_m_14_3.price2}')
    with open('files/2.png', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(f'Название: {Texts_m_14_3.product3} | Описание: {Texts_m_14_3.product_description3}'
                         f' | Цена: {Texts_m_14_3.price3}')
    with open('files/3.png', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(f'Название: {Texts_m_14_3.product4} | Описание: {Texts_m_14_3.product_description4}'
                         f' | Цена: {Texts_m_14_3.price4}')
    with open('files/4.png', 'rb') as img:
        await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_buy)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.callback_query_handler(text='calories')
async def set_gender(call):
    await call.message.answer('Укажите Ваш пол "m" или "w"')
    await call.answer()
    await UserState.gender.set()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(f'{Texts_m_14_3.formulas_m}\n {Texts_m_14_3.formulas_w}')
    await call.answer()


@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender_user=message.text.lower())
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growht(message, state):
    await state.update_data(age_user=message.text)
    await message.answer('Введите свой рост в см')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_user=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    global calories
    await state.update_data(weight_user=message.text)
    data = await state.get_data()
    if data['gender_user'] == 'm':
        calories = (10 * float(data['weight_user']) + 6.25
                    * float(data['growth_user']) - 5 * float(data['age_user']) + 5)
    elif data['gender_user'] == 'w':
        calories = (10 * float(data['weight_user']) + 6.25
                    * float(data['growth_user']) - 5 * float(data['age_user']) - 161)
    await message.answer(f'Ваша суточная норма калорий составляет {calories}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def star_massage(message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
