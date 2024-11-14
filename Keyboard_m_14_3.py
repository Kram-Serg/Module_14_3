from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import Texts_m_14_3
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.row(button)
kb.insert(button2)
kb.add(button3)

kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
button_inline = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_inline2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.row(button_inline)
kb_inline.insert(button_inline2)

kb_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=f'{Texts_m_14_3.product1}', callback_data='product_buying')],
        [InlineKeyboardButton(text=f'{Texts_m_14_3.product2}', callback_data='product_buying')],
        [InlineKeyboardButton(text=f'{Texts_m_14_3.product3}', callback_data='product_buying')],
        [InlineKeyboardButton(text=f'{Texts_m_14_3.product4}', callback_data='product_buying')]
    ], resize_keyboad=True
)
