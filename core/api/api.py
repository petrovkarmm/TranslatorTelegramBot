import requests
from core.api.api_settings import api_token, BASE_URL_POST


class ApiTranslater:

    def __init__(self, word: str, text_language_code: int, language_code: int) -> None:
        """
        Класс API translater:
        Обновляет токен для дальнейшей работы при помощи POST запроса
        Использует токен и входящие данные для получения перевода в GET запросе
        Сохраняет в себе перевод слова в переменную self.__translation
        Или сохраняет в self.__translation None, если слово отсутствует в словаре или был нарушен ввод языка
        :param word: Слово для перевода
        :param text_language_code: Язык слова
        :param language_code: Язык на который необходимо произвести перевод
        """

        headers_for_post = {
                "Authorization": f"Basic {api_token}"
        }

        get_token = requests.post(BASE_URL_POST, headers=headers_for_post)

        headers_for_get = {
            "Authorization": f"Bearer {get_token.text}"
        }

        # По какой-то причине была ошибка 404,
        # что указывало на неверный отправляемый адрес, пришлось передать данные так...
        url = f'https://developers.lingvolive.com/api/v1/Minicard' \
              f'?text={word}&' \
              f'srcLang={int(text_language_code)}&' \
              f'dstLang={int(language_code)}&' \
              f'isCaseSensitive=isCaseSensitive'

        get_request = requests.get(url, headers=headers_for_get)

        if get_request.status_code == 404:
            self.__translation = None

        else:
            self.__translation = get_request.json()['Translation'].get('Translation')

    @property
    def get_translation(self) -> str:
        """
        Функция геттер, используется в последнем машинном состоянии translate_text в core.api.handlers.translate
        :return: Перевод слова
        """
        return self.__translation
