from tinydb import TinyDB
from tinydb.database import Document
import requests

db = TinyDB('db.json', indent=4)

users = db.table('users')


def get_users(n: int) -> list[dict]:
    url = "https://randomuser.me/api/"
    payload = {"results": n}

    response = requests.get(url=url, params=payload)

    if response.status_code == 200:
        users = []
        for user in response.json()['results']:
            users.append({
                'first_name': user['name']['first'],
                'last_name': user['name']['last'],
                'gender': user['gender'],
                'country': user['location']['country'],
                'city': user['location']['city'],
                'email': user['email'],
                'age': user['dob']['age'],
                'phone': user['phone'],
                'nat': user['nat'],
            })

        return users


users_data = get_users(5000)
users.insert_multiple(users_data)

