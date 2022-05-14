from flask import Blueprint, request, redirect, url_for, flash

from ...controllers import users_controller
from ...models.models import User

users_scope = Blueprint("users_api", __name__, url_prefix="/users")


@users_scope.post("/users")
def users_dispatcher():
    data = request.form
    method = data.get("_method")

    user = User(
        id_=data["id_"],
        name=data["name"],
        email=data["email"],
    )

    if method == "POST":
        return create(user)
    elif method == "PUT":
        return update(user)
    elif method == "DELETE":
        return delete(user)
    else:
        raise ValueError("User received an invalid method")


def create(user: User):
    users_controller.create(user)
    flash("User creado con éxito!")
    return redirect(url_for("views.users_views.users"))


def update(user: User):
    users_controller.edit(user)
    flash("User editado con éxito!")
    return redirect(url_for("views.users_views.users"))


@users_scope.post("/delete")
def delete():

    data = request.form
    user_id = data.get("delete_id")
    user_ = User(id_=user_id)
    user = users_controller.get_by_id(user_)

    users_controller.delete(user)

    flash("User borrado con éxito!")
    return redirect(url_for("views.users_views.users"))
