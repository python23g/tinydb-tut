from tinydb import TinyDB, Query
from tinydb.database import Document


db = TinyDB('db.json', indent=4)

users = db.table('users')
q = Query()


def user_by_id(id: int) -> Document:
    user = users.get(doc_id=id)
    return user

def users_by_id(ids: list[int]) -> list[Document]:
    return users.get(doc_ids=ids)


def users_by_gender(gender: str) -> list[Document]:
    return users.search(q.gender == gender)


def users_by_country(country: str) -> list[Document]:
    pass


def users_by_city(city: str) -> list[Document]:
    pass


def users_by_age(age: int) -> list[Document]:
    pass


def users_by_nat(nat: str) -> list[Document]:
    pass


def users_in_range(min_age: int, max_age: int) -> list[Document]:
    pass


def users_by_country_and_city(country: str, city: str) -> list[Document]:
    pass


def users_by_country_and_city(country: str, city: str) -> list[Document]:
    pass


