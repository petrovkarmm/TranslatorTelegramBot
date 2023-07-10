import asyncio
import logging

from core.settings import admin_id, bot_token

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from core.api.handlers import translate
from core.handlers.handlers import (get_start,
                                    get_help,
                                    get_contacts)

from core.utils.statesform import StepsForm

from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    """
    Установка дефолтных команд во время начала бота. Отправка сообщения создателю о том, что ботом кто-то воспользовался
    :param bot:
    :return:
    """
    await set_commands(bot)
    await bot.send_message(admin_id, text=f'Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(admin_id, text='Бот выключен!')


async def start():
    """
    Начало логирования при старте бота. Вывод в терминал.
    :return:
    """
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(token=bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_start, F.text.lower() == '🚀 старт')

    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(get_help, F.text.lower() == '⏳ помощь')

    dp.message.register(get_contacts, Command(commands=['contacts']))
    dp.message.register(get_contacts, F.text.lower() == '📖 контакты')

    dp.message.register(translate.start_state, Command(commands=['translate']))
    dp.message.register(translate.start_state, F.text.lower() == '🌐 перевод')

    dp.message.register(translate.cancel, F.text.lower() == 'отмена')

    dp.message.register(translate.get_text, StepsForm.GET_WORD)
    dp.message.register(translate.get_text_language, StepsForm.GET_WORD_LANGUAGE)
    dp.message.register(translate.get_language_type_and_confirm, StepsForm.GET_LANGUAGE_TYPE)
    dp.message.register(translate.translate_text, StepsForm.TRANSLATED_TEXT)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
