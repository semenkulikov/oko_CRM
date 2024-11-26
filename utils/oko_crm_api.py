import requests
from pprint import pprint
from dotenv import find_dotenv, load_dotenv
import os
import logging

app_log = logging.getLogger(__name__)

if find_dotenv():
    load_dotenv()

API_AUTHORIZATION_TOKEN = os.getenv("API_AUTHORIZATION_TOKEN")


def get_all_users(session: requests.Session) -> dict:
    """
    Функция для получения списка всех пользователей и информации о них.
    :param session: объект сессии
    :return: json
    """
    app_log.info("Запрашиваю информацию о всех юзерах с oko CRM...")
    response = session.get('https://api.okocrm.com/v2/users/')
    if response.status_code == 200:
        return response.json().get("data")
    else:
        print(f"Ошибка: {response.status_code}")
        return None


def get_contact_by_id(session: requests.Session, contact_id: str):
    """
    Функция для получения информации о контакте по его ID.
    :param session: объект сессии
    :param contact_id: ID контакта
    :return: json
    """
    app_log.info(f"Запрашиваю информацию о контакте с ID: {contact_id}...")

    response = session.get(f'https://api.okocrm.com/v2/contacts/{contact_id}/')
    if response.status_code == 200:
        return response.json().get("data")
    else:
        print(f"Ошибка: {response.status_code}")
        return None



def get_all_contacts(session: requests.Session) -> dict:
    """
    Функция для получения списка всех контактов и информации о них.
    :param session: объект сессии
    :return: json
    """
    app_log.info("Запрашиваю информацию о всех контактах с oko CRM...")

    response = session.get('https://api.okocrm.com/v2/contacts/')
    if response.status_code == 200:
        return response.json().get("data")
    else:
        print(f"Ошибка: {response.status_code}")
        return None


def get_all_leads(session: requests.Session) -> dict:
    """
    Функция для получения списка всех сделок и информации о них.
    :param session: объект сессии
    :return: json
    """
    app_log.info("Запрашиваю информацию о всех сделках с oko CRM...")
    response = session.get('https://api.okocrm.com/v2/leads/')
    if response.status_code == 200:
        return response.json().get("data")
    else:
        print(f"Ошибка: {response.status_code}")
        return None


def get_lead_by_id(session: requests.Session, lead_id: str) -> dict:
    """
    Функция для получения информации о сделке по ее ID.
    :param session: объект сессии
    :param lead_id: ID сделки
    :return: json
    """
    app_log.info(f"Запрашиваю информацию о сделке с ID: {lead_id}...")
    response = session.get(f'https://api.okocrm.com/v2/leads/{lead_id}/')
    if response.status_code == 200:
        return response.json().get("data")
    else:
        print(f"Ошибка: {response.status_code}")
        return None



def main():
    app_log.info("Тестовое сообщение...")
    session = requests.session()
    session.headers.update({'Authorization': f'Bearer {API_AUTHORIZATION_TOKEN}',
                            "Accept": "application/json"})
    users_data = get_all_users(session)
    # pprint(users_data)
    contacts_data = get_all_contacts(session)
    # pprint(contacts_data)
    for contact in contacts_data:
        contact_data = get_contact_by_id(session, contact.get("id"))
        print(f"ФИО контакта: {contact_data.get("name")}")
        print(f"Emails контакта: {contact_data.get('emails')}")

    leads_list = get_all_leads(session)
    # pprint(leads_list)
    for lead in leads_list:
        lead_data = get_lead_by_id(session, lead.get("id"))
        print(f"Название сделки: {lead_data.get('name')}")
        print(f"Сумма сделки: {lead_data.get('budget')}")
        print(f"Идентификатор ответственного: {lead_data.get('user_id')}")
        print(f"Контакты: {lead_data.get('contacts')}")
        print(f"Компании: {lead_data.get("companies")}")
        print("----------------------------------------")



if __name__ == '__main__':
    main()
