from dataclasses import asdict
from typing import List, Optional

from ..models.models import User
from .base_db import db


user_ref = db.collection("Users")
global_ref = db.collection("Global").document("num_users")


def create(user: User) -> User:
    user.id_ = autoincrement_id()
    user_ref.document(user.id_).set(asdict(user))
    return user


def autoincrement_id() -> int:

    doc_dict = global_ref.get().to_dict()

    if doc_dict is None:
        new_id = "1"
        global_ref.set({"num_users": new_id})
        return new_id

    num_users = doc_dict["num_users"]
    new_id = str(int(num_users) + 1)
    global_ref.set({"num_users": new_id})

    return new_id


def get_by_id(user: User) -> Optional[User]:
    docs = user_ref.where("id_", "==", user.id_).get()

    if docs == []:
        return None

    for doc in docs:
        user_encontrado = User(**doc.to_dict())
    return user_encontrado


def get_all() -> List[User]:

    docs = user_ref.get()
    if docs == []:
        return []

    results = []
    for doc in docs:
        results.append(User(**doc.to_dict()))

    return results


def update_by_id(user: User) -> User:
    user_ref.document(user.id_).update(asdict(user))
    return user


def delete_by_id(user: User) -> None:
    user_ref.document(user.id_).delete()
