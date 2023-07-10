from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


select_language_type_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='RU'
        ),
    ],
    [
        KeyboardButton(
            text='EN'
        ),
    ],
    [
        KeyboardButton(
            text='UK'
        ),
    ],
    [
        KeyboardButton(
            text='FR'
        ),
    ],
    [
        KeyboardButton(
            text='❎ Отмена',
            description='Сброс данных'
        ),
    ],
], resize_keyboard=True, one_time_keyboard=True)

confirm_or_cancel_translate = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='✅ Да',
            descruption='Произвести перевод'
        ),
    ],
    [
        KeyboardButton(
            text='❎ Отмена',
            description='Сброс данных'
        ),
    ],
], resize_keyboard=True, one_time_keyboard=True)