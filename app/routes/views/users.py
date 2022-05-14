from flask import Blueprint, render_template, request, flash, jsonify
from ...controllers import users_controller
from ...models.models import User
from ...models.exceptions import NoEntitiesRegistered

users_scope = Blueprint(
    "users_views",
    __name__,
)


@users_scope.route("/")
@users_scope.route("/get_all")
def users_get_all():
    try:
        users = users_controller.get_all()
    except NoEntitiesRegistered:
        users = []
        flash("Todavía no registraste ningún user")

    return render_template("users.html", users=users)


@users_scope.post("/show_id/")
def show_id():

    data = request.form.to_dict()
    user_id = (list(data.values()))[0]
    user_ = User(id_=user_id)
    user = users_controller.get_by_id(user_)
    users_controller.delete(user)

    return jsonify(user)
