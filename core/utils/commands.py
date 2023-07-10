from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    """
    Кнопки доступные всё время, кроме как во время нахождения в машинном состоянии
    :param bot:
    :return:
    """
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='translate',
            description='Начать перевод'
        ),
        BotCommand(
            command='contacts',
            description='Ссылки для связи'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
