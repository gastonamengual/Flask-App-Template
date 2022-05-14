from ..models.models import User
from .firebase_database import FirebaseDatabase, FirebaseDatabaseConfig


def create_test_database():

    firebase_db = FirebaseDatabase(FirebaseDatabaseConfig(collection_name="Users"))

    users = firebase_db.get_all()

    if users == []:

        firebase_db.initialize_global_ref()

        users = [
            User(id_="1", name="John", email="john@mail.com"),
            User(id_="2", name="Elizabeth", email="elizabeth@mail.com"),
        ]

        for user in users:
            firebase_db.create(user)
