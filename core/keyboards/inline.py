from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from core.settings import admin_id

select_my_contacts = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Мой профиль в телеграмм.',
            url=f'tg://user?id={str(admin_id)}',
        )
    ]
])