from aiogram import Bot
from aiogram.dispatcher import router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.settings import admin_id

from core.keyboards.reply import start_keyboard, get_reply_keyboard
from core.keyboards.inline import select_my_contacts


async def get_contacts(message: Message, bot: Bot):
    await message.answer(f'Ссылки для связи',
                         reply_markup=select_my_contacts)


async def get_help(message: Message, bot: Bot):
    """
    Хендлер на /help
    :param message: Сообщение /help
    :param bot:
    :return:
    """
    await bot.send_message(message.from_user.id, f"<b>Приветствую, "
                                                 f"{message.from_user.first_name}.\n\n</b>"
                                                 f"Это мой телеграм бот созданный "
                                                 f"в рамках пет-проекта. "
                                                 f"Данный бот создан для перевода слов при помощи "
                                                 f"стороннего API словарей Lingvo.\n"
                                                 f"Ответ приходит в виде мини-карточки с переводом.\n\n"
                                                 f"Для начала работы далее можете нажать на кнопку "
                                                 f"<b>Перевод</b> или воспользоваться командой <b>/translate</b>")

    await bot.send_message(message.from_user.id, f"Доступные языки перевода:\n\n"
                                                 f"RU: русский 🇷🇺\nEN: английский 🇺🇸\n"
                                                 f"UK: украинский 🇺🇦\nFR: французский 🇲🇫",
                                                 reply_markup=get_reply_keyboard())

    await bot.send_message(message.from_user.id, f"Ссылки для контакта: ",
                                                 reply_markup=select_my_contacts)


async def get_start(message: Message, bot: Bot):
    """
    Хендлер на /start
    :param message: Сообщение /start
    :param bot:
    :return:
    """
    await bot.send_message(admin_id, text=f'Твоим ботом воспользовался пользователь. ')
    await bot.send_message(message.from_user.id, f"<b>Добро пожаловать в телеграм!\n"
                                                 f"Для полного ознакомления с ботом "
                                                 f"прошу использовать следующую команду:"
                                                 f" /help. Она доступна у вас в меню и в качестве кнопки.</b>",
                           reply_markup=start_keyboard)



