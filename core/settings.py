import os

from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')