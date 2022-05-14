from .models import User
from ..database import users_db
from ..database.users_db import global_ref


def create_test_database():

    users = users_db.get_all()

    if users == []:

        ### Clientes
        users = [
            User(id_="1", name="John", email="john@mail.com", password="123"),
            User(id_="2", name="Elizabeth", email="elizabeth@mail.com", password="123"),
        ]

        for user in users:
            users_db.create(user)

        global_ref.set({"num_users": 2})
