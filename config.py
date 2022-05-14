from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = True

    DATABASE_URL = "https://comienza-tu-emprendimiento-default-rtdb.firebaseio.com"
    DB_CREDENTIALS = "credentials.json"

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"