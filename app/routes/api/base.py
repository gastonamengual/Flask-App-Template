from flask import Blueprint
from .users import users_scope

api_scope = Blueprint('api', __name__, url_prefix='/api')
api_scope.register_blueprint(users_scope)
