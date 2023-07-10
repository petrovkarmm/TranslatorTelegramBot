from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    """
    Машинное состояние
    """
    GET_WORD = State()
    GET_WORD_LANGUAGE = State()
    GET_LANGUAGE_TYPE = State()
    TRANSLATED_TEXT = State()
