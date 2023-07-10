from core.settings import settings

api_token = settings.bots.api_token
BASE_URL_POST = 'https://developers.lingvolive.com/api/v1.1/authenticate'

languages_codes = {
    'EN': 1033,
    'RU': 1049,
    'UK': 1058,
    'FR': 1036,
}

languages = {
    'RU': 'русский',
    'EN': 'английский',
    'UK': 'украинский',
    'FR': 'французский'
}