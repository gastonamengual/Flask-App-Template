from ..models.models import User
from ..models.exceptions import EntityExists


def validate_exists(user: User) -> None:
    if user is not None:
        raise EntityExists("The user is already registered", "users", "producto_crear")
