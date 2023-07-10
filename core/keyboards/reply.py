from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='⏳ Помощь'
        ),
    ],
], resize_keyboard=True, one_time_keyboard=True)


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='🚀 Старт')
    keyboard_builder.button(text='🌐 Перевод')
    keyboard_builder.button(text='📖 Контакты')
    keyboard_builder.button(text='⏳ Помощь')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )