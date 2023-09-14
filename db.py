from tinydb import TinyDB, Query
from tinydb.database import Document


db = TinyDB('db.json', indent=4)

users = db.table('users')
q = Query()


def user_by_id(id: int) -> Document:
    return users.get(doc_id=id)


def users_by_id(ids: list[int]) -> list[Document]:
    return users.get(doc_ids=ids)


def users_by_gender(gender: str) -> list[Document]:
    return users.search(q.gender == gender)


def users_by_country(country: str) -> list[Document]:
    return users.search(q.country == country)


def users_by_city(city: str) -> list[Document]:
    return users.search(q.city == city)


def users_by_age(age: int) -> list[Document]:
    return users.search(q.age == age)


def users_by_nat(nat: str) -> list[Document]:
    return users.search(q.nat == nat)


def users_gt(age: int) -> list[Document]:
    """greater then"""
    return users.search(q.age > age)


def users_gte(age: int) -> list[Document]:
    """greater then or eaqual to"""
    return users.search(q.age >= age)


def users_lt(age: int) -> list[Document]:
    """less then"""
    return users.search(q.age < age)


def users_lte(age: int) -> list[Document]:
    """less then or eaqual to"""
    return users.search(q.age <= age)


def users_in_range(min_age: int, max_age: int) -> list[Document]:
    return users.search((q.age > min_age) & (q.age < max_age))


def users_by_country_and_city(country: str, city: str) -> list[Document]:
    pass


data = {
    "age": 18,
    "dfadsfas": "fdasfds"
}

users.update(data, q.first_name == 'Johnni')