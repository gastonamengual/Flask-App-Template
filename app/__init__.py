from flask import Flask, request

from config import Config

from .routes import api_scope, errors_scope, views_scope

from app.routes.api.base import api_scope
from app.routes.views.base import views_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)
app.secret_key = "super secret key"

app.register_blueprint(errors_scope, url_prefix="/")
app.register_blueprint(api_scope, url_prefix="/api")
app.register_blueprint(views_scope, url_prefix="/")

from .database import initialize_db
initialize_db.create_test_database()