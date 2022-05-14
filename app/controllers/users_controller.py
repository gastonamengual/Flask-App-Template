from typing import List
from ..helpers import helper
from ..database.firebase_database import FirebaseDatabase, FirebaseDatabaseConfig
from ..models.models import User


def create(user: User) -> User:
    firebase_db = FirebaseDatabase(FirebaseDatabaseConfig(collection_name="Users"))
    user_found = firebase_db.get_by_id(user)
    helper.validate_exists(user_found)
    return firebase_db.create(user)


def edit(user: User) -> User:
    firebase_db = FirebaseDatabase(FirebaseDatabaseConfig(collection_name="Users"))
    return firebase_db.update_by_id(user)


def delete(user: User):
    firebase_db = FirebaseDatabase(FirebaseDatabaseConfig(collection_name="Users"))
    firebase_db.delete_by_id(user)
    return None


def get_all() -> List[User]:
    firebase_db = FirebaseDatabase(FirebaseDatabaseConfig(collection_name="Users"))
    users = firebase_db.get_all()
    return users


def get_by_id(user_: User) -> User:
    firebase_db = FirebaseDatabase(FirebaseDatabaseConfig(collection_name="Users"))
    user = firebase_db.get_by_id(user_)
    return user
