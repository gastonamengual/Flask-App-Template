import firebase_admin
from firebase_admin import credentials, firestore
from config import Config

cred = credentials.Certificate(Config.DB_CREDENTIALS)
firebase_admin.initialize_app(cred, {'databaseURL' : Config.DATABASE_URL})
db = firestore.client()