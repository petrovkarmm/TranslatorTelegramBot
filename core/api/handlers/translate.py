from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from core.utils.statesform import StepsForm

from core.keyboards.reply import get_reply_keyboard

from core.api.keyboards.reply import (select_language_type_keyboard, confirm_or_cancel_translate)
from core.api.api import ApiTranslater

from core.api.api_settings import languages, languages_codes

# Словарь для сравнения выбранных языков, создан, чтобы не допустить перевода одинаковых языков. (иначе сбой API)
# 65, 84, 85(сравнение) строчки
data_languages = {}


async def cancel(message: Message, state: FSMContext):
    """
    Универсальная функция сброса данных на каждом этапе машинного состояния
    :param message: Отмена
    :param state: Текущая сессия перевода
    :return: None
    """
    await state.clear()
    await message.answer(f'Данные успешно сброшены. ', reply_markup=get_reply_keyboard())


async def start_state(message: Message, state: FSMContext):
    """
    Переход в этапное машинное состояние core.utils.statesform.py StepsForm
    :param message: /translate , Перевод
    :param state: StepsForm
    :return: None
    """
    await message.answer(f'{message.from_user.first_name}, введите слово для перевода.')
    await state.set_state(StepsForm.GET_WORD)


async def get_text(message: Message, state: FSMContext):
    """
    Переход в первое состояние GET_TEXT класса StepsForm, сохранение в дату введенного слова.
    :param message: Слово пользователя
    :param state: StepsForm
    :return: None
    """
    await state.update_data(word=message.text)
    await message.answer(f'Выберите <b>на каком языке написано слово</b>:',
                         reply_markup=select_language_type_keyboard)
    await state.set_state(StepsForm.GET_WORD_LANGUAGE)


async def get_text_language(message: Message, state: FSMContext) -> None:
    """
    Переход во второе состояние GET_WORD_LANGUAGE класса StepsForm, сохранение в дату языка слова.
    :param message: Язык слова пользователя
    :param state: StepsForm
    :return: None, выход из состояния + очистка даты, если была произведена ошибка ввода.
    """
    if not languages.get(message.text.upper()):
        await message.answer(f'Выбранный язык перевода {message.text} не существует. Пожалуйста, начните заново.',
                             reply_markup=get_reply_keyboard())
        return await state.clear()
    data_languages['1'] = message.text
    await state.update_data(text_language=message.text)
    await state.set_state(StepsForm.GET_LANGUAGE_TYPE)
    await message.answer(f'Выберите желаемый язык перевода.',
                         reply_markup=select_language_type_keyboard)


async def get_language_type_and_confirm(message: Message, state: FSMContext) -> None:
    """
    Переход в третье состояние GET_LANGUAGE_TYPE класса StepsForm, сохранение в дату язык перевода.
    Вывод итоговых данных для дальнейшего подтверждения
    :param message: На какой язык производить перевод
    :param state: StepsForm
    :return: None, выход из состояния + очистка даты, если была произведена ошибка ввода.
    """
    if not languages.get(message.text.upper()):
        await message.answer(f'Выбранный язык перевода {message.text} не существует. Пожалуйста, начните заново.',
                             reply_markup=get_reply_keyboard())
        return await state.clear()
    data_languages['2'] = message.text
    if data_languages.get('1') == data_languages.get('2'):
        await message.answer('Язык слова и язык перевода одинаковые. Пожалуйста, начните заново.',
                             reply_markup=get_reply_keyboard())
        return await state.clear()
    await state.update_data(language=message.text)

    context_data = await state.get_data()
    text = context_data.get('word')
    text_language = context_data.get('text_language')
    language = context_data.get('language')
    await message.answer('<b>Вот введенные вами данные:</b>')
    data_user = f'Слово: {text}\n' \
                f'Язык текста: {languages.get(text_language)}\n' \
                f'Выбранный язык перевода: {languages.get(language)}\n'
    await message.answer(f'{data_user}')
    await message.answer(f'Произвести перевод?', reply_markup=confirm_or_cancel_translate)
    await state.set_state(StepsForm.TRANSLATED_TEXT)


async def translate_text(message: Message, state: FSMContext):
    """
    Переход в четвертое состояние TRANSLATED_TEXT класса StepsForm, сохранение в дату язык перевода.
    Отправка context_data в класс перевода, в случае отсутствия слова в словаре (или неверно указанном языке слова)
    выдается сообщение об ошибке. Данные стираются.
    В случае ином перевод отправляется пользователю
    :param message: Подтверждение перевода
    :param state: StepsForm
    :return: None
    """
    context_data = await state.get_data()
    word = context_data.get('word')

    text_language = context_data.get('text_language')
    text_language_code = int(languages_codes.get(text_language))

    language = context_data.get('language')
    language_code = int(languages_codes.get(language))

    # Отправка данных в core.api.api.py класс ApiTranslater для получения перевода
    translator_object = ApiTranslater(word, text_language_code, language_code)
    translate_answer = translator_object.get_translation

    if translate_answer:
        await message.answer(f'Переведённое слово: {translate_answer}', reply_markup=get_reply_keyboard())
        await state.clear()
    else:
        await message.answer(f'Ошибка передачи данных. Неверно указан язык слова или слово отсутствует в словаре',
                             reply_markup=get_reply_keyboard())
        await state.clear()
