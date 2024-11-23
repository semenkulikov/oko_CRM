from dotenv import find_dotenv, load_dotenv
import os


if find_dotenv():
    load_dotenv()
else:
    exit("Переменные окружения не загружены, т.к. не найден файл .env!")

API_AUTHORIZATION_TOKEN = os.getenv('API_AUTHORIZATION_TOKEN')
