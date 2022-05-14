from typing import List
from ..helpers import helper
from ..database import users_db
from ..models.models import User


def create(user: User) -> User:
    user_found = users_db.get_by_id(user)
    helper.validate_exists(user_found)
    return users_db.create(user)


def edit(user: User) -> User:
    return users_db.update_by_id(user)


def delete(user: User):
    users_db.delete_by_id(user)
    return None


def get_all() -> List[User]:
    users = users_db.get_all()
    return users


def get_by_id(user_: User) -> User:
    user = users_db.get_by_id(user_)
    return user
