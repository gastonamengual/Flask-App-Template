import re
from typing import OrderedDict
from ..models.models import Usuario
from ..models.exceptions import UserNotFound, EntityExists, EmailInvalidFormat

### VALIDATE LOGIN
def validate_login(usuario: Usuario, usuario_encontrado: Usuario) -> None:
    if usuario_encontrado is None:
        raise UserNotFound
    if usuario_encontrado.password != usuario.password:
        raise UserNotFound

##### VALIDATE EMAIL
def validate_email(usuario: Usuario) -> None:
    if not __email_is_valid(usuario.email):
        raise EmailInvalidFormat

###### VALIDATE EMAIL FORMAT
def __email_is_valid(email: str) -> bool:
    if not isinstance(email, str):
        return False

    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    return bool(re.search(regex, email))

#### USER EXISTS
def validate_user_exists(usuario: Usuario) -> None:
    if usuario is not None:
        raise EntityExists('El usuario ya está registrado', 'register', 'register')