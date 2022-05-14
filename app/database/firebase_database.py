from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

from ..models.models import Entity, User
from .abstract_database import AbstractDatabase, AbstractDatabaseConfig

import firebase_admin
from firebase_admin import credentials, firestore

DATABASE_URL = "https://comienza-tu-emprendimiento-default-rtdb.firebaseio.com"
DB_CREDENTIALS = {
    "type": "service_account",
    "project_id": "flask-app-template-d7f81",
    "private_key_id": "c840309b4eacbefba5d3c98758086d578bf8665d",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCf+RpNlbuN1Az7\nH1ZQbGbN6uiqsp0CIbFuEG4kvJp7xL/I0/tIEBmgDH69aoRpYgXwDrdtap8uZ3Ur\nlP51xOOgAVsbcu9H2DJkQN79pBMJNGwzDaB8MpbTCcpfcb1M4NzTSoop7VWnpbjc\nBqwP3rN5EHlSixw/U01dtamj3NZT84Ju5gLFrHDk++cJ7ISx+b1P07aDy1FSX2vH\nuclxTpcnpAOsCRjSitXn0IxH0D0vO5HtPNsxL/I1CWgewVBcdKIO2hOahqm6x5aq\n76rXcLLTEQc8p9iK//OJwRwishVZVY2RN0WORGRGVzWrIAhrqCoV/HMleysug268\neybl5uONAgMBAAECggEAD73igbn3P8ibEmcOBlH0d9Ti2lFDM/9+xzbkr8bDaOR+\nftOlSX0UGHTCT/9YUkpsDShVknXIfjd+BzDdLVeXkpovje7sbuRuaQEdMFZh7Sj0\ncL2pii8sOk4fVO8LUrJZ6IzQNbn+EMY0/6nEardeb85YMfAwcmbPGSaUL+S+Tnpj\nCZphqDty/EONj7DgX8+lyIZauNWM+rFQ6f8403VtpguiJE/CnG+mnQZk4sxJN3VT\n76pnoelzN8LBsUwZR+EPTuhGZyL/TTikPbZTjw8Sb6N/56TcyUK0N6EYO21kTOKG\nvuLPSjGvN4cgHKvubDo5TUoKFfgt92KBeA6MNNEeXQKBgQDNE1II6sjI6cmUIKLs\nFTOOs4IVm9S3dvWAknupn1mL+9z74EZlQ8KkH0iYS/ilvj9CWUknM0T1zybR09gq\nGbvUJ6zEnW1GJ1+YKN6ber3nSwmnmuWlPBHPlNH5orgmTYMXRCSadA9MKPeVojwH\nCIxeAeZ/Nf9AVODeut8kpRVd8wKBgQDHsp1p0DTx8kiFWvWtEXrQuPlVrK+r6L1q\nTWmE5icESOc3bvR7vL1bAC9Gi0HbfZZbDORyreMpIIl9t/bSWBCaxpphjNKiFqTK\nSy8jjVc8empkyWJvuIrDH/PI4pimRbS0aLgTL3IhZSuO5OJ0Gj2Y481BJN1fsWd1\n+6eCnaeYfwKBgBit/Y5jKvy63e58qv68YnMG+V2+XjAiGdN6TXWRXsZw7hxF1lLz\nf6Yeua7SXb8ckSJb+mjES8VFQ8e2teoDJM6YY7tZsr/hlyiJqpiNgfMm3aeVBZQI\nEaCoqUhgo8bAR0lygvEvjHO+7mTMnGrARZw+oE2o4uoMDO/hD1+qmlKvAoGAOver\nM8ufVrJMZ9RsJya6NVfpiDrtxL188R7awbuUWdeNLvk8iC07XNu5GgOU9tMmyswL\nyTE/mq1Y7B6ea45FmO58N8H1kJdPIc0BpmXeFKWxNQGiZ4r+ro+I1RDUMoTyzzL8\n5+1irinJqvA7Tj1RYwwhV9Mi61bfTh95X0BedNECgYALHMcuJ/fI8hkFGODkBYGW\nzMiKGNWocXoeA7TzA8dBlPwyuJ5T6VX/h9PitxCTac6UX2xHSGIi8kX8Dur4Wchw\nQ54ssXTmgwu8nGfz8c8CokJr6WK9CZzCmNSSN+GR8CWnyrWVSVOJyNyWc0eF8OHr\nSzOkbwL1sk6g/FdBcfZPwg==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-lmrsh@flask-app-template-d7f81.iam.gserviceaccount.com",
    "client_id": "112618109853569125538",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lmrsh%40flask-app-template-d7f81.iam.gserviceaccount.com",
}


@dataclass
class FirebaseDatabaseConfig(AbstractDatabaseConfig):
    collection_name: str = ""


@dataclass
class FirebaseDatabase(AbstractDatabase[FirebaseDatabaseConfig]):
    def __post_init__(self):
        app_initialized = firebase_admin._apps
        if not app_initialized:
            cred = credentials.Certificate(DB_CREDENTIALS)
            firebase_admin.initialize_app(cred, {"databaseURL": DATABASE_URL})

    @property
    def db(self):
        return firestore.client()

    @property
    def entity_ref(self):
        return self.db.collection(self.config.collection_name)

    @property
    def global_ref(self):
        return self.db.collection("Global").document(self.config.collection_name)

    def initialize_global_ref(self):
        self.global_ref.set({self.config.collection_name: 0})

    def create(self, entity: Entity) -> Entity:
        entity.id_ = self.autoincrement_id()
        self.entity_ref.document(entity.id_).set(asdict(entity))
        return entity

    def autoincrement_id(self) -> str:

        doc_dict: Dict[str, str] = self.global_ref.get().to_dict()

        if doc_dict is None:
            new_id = "1"
            self.global_ref.set({self.config.collection_name: new_id})
            return new_id

        num_users: str = doc_dict[self.config.collection_name]
        new_id = str(int(num_users) + 1)
        self.global_ref.set({self.config.collection_name: new_id})

        return new_id

    def get_by_id(self, entity: Entity) -> Optional[Entity]:
        docs = self.entity_ref.where("id_", "==", entity.id_).get()

        if docs == []:
            return None

        for doc in docs:
            entity_found = User(**doc.to_dict())  # TODO Change harcoded User
        return entity_found

    def get_all(self) -> List[Entity]:

        docs = self.entity_ref.get()
        if docs == []:
            return []

        results = []
        for doc in docs:
            results.append(User(**doc.to_dict()))  # TODO Change harcoded User

        return results

    def update_by_id(self, entity: Entity) -> Entity:
        self.entity_ref.document(entity.id_).update(asdict(entity))
        return entity

    def delete_by_id(self, entity: Entity) -> None:
        self.entity_ref.document(entity.id_).delete()
