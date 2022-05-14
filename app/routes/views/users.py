from flask import Blueprint, render_template, request, flash, jsonify
from ...controllers import users_controller
from ...models.models import User
from ...models.exceptions import NoEntitiesRegistered

users_scope = Blueprint("users_views", __name__, url_prefix="/")

#### CLIENTE
@users_scope.get("/")
def users_get_all():
    try:
        users = users_controller.get_all()
    except NoEntitiesRegistered:
        users = []
        flash("Todavía no registraste ningún user")

    return render_template("users.html", users=users)


#### EDITAR (desde ajax)
@users_scope.post("/editar/")
def user_editar():

    data = request.form.to_dict()
    user_id = (list(data.values()))[0]
    user_ = User(id_=user_id)
    user = users_controller.get_by_id(user_)

    return jsonify(user)


#### BORRAR (desde ajax)
@users_scope.post("/borrar/")
def user_borrar():

    data = request.form.to_dict()
    user_id = (list(data.values()))[0]
    user_ = User(id_=user_id)
    user = users_controller.get_by_id(user_)

    return jsonify(user)
