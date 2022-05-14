from flask import Blueprint
from .users import users_scope

views_scope = Blueprint('views', __name__, url_prefix='/')
views_scope.register_blueprint(users_scope)