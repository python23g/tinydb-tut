from tinydb import TinyDB
from tinydb.database import Document
import requests

db = TinyDB('db.json', indent=4)

males = db.table('males')
females = db.table('females')


def get_users(n: int, gender: str) -> list[dict]:
    url = "https://randomuser.me/api/"
    payload = {"results": n, "gender": gender}

    response = requests.get(url=url, params=payload)

    if response.status_code == 200:
        users = []
        for user in response.json()['results']:
            users.append({
                "full_name": f'{user["name"]["first"]} {user["name"]["last"]}',
                "age": user['dob']['age'],
                'address': f'{user["location"]["country"]}, {user["location"]["city"]}, {user["location"]["street"]["number"]}',
                'phone': user['phone'],
                'email': user['email'],
                'image': user['picture']['large']
            })

        return users


def add_users(users: list[dict], table: TinyDB):
    table.insert_multiple(users)


def clear_db(table: TinyDB):
    table.truncate()

clear_db(males)
clear_db(females)