from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from core.settings import settings

select_my_contacts = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Мой профиль в телеграмм.',
            url=f'tg://user?id={str(settings.bots.admin_id)}',
        )
    ]
])