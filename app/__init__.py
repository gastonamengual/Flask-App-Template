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

from .models import test_script
test_script.create_test_database()

from .routes.views.usuarios import mail

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'emprendeapp2022@gmail.com',
    "MAIL_PASSWORD": 'EmprendeApp123'
}
app.config.update(mail_settings)
mail.init_app(app)