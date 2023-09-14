from tinydb import TinyDB
from tinydb.database import Document
import requests

db = TinyDB('db.json', indent=4)

users = db.table('users')


def user_by_id(id: int) -> Document:
    pass


def users_by_id(id: int) -> list[Document]:
    pass


def users_by_gender(gender: str) -> list[Document]:
    pass


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


