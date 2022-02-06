from ..helpers import usuarios_helper
from ..database import usuarios_db
from ..models.models import Usuario

#### LOGIN
def login(usuario: Usuario) -> Usuario:
    usuario_encontrado = usuarios_db.get_by_email(usuario)
    usuarios_helper.validate_login(usuario, usuario_encontrado)
    return usuario_encontrado

#### REGISTER USER
def create(usuario: Usuario) -> Usuario:
    usuarios_helper.validate_email(usuario)
    usuario_encontrado = usuarios_db.get_by_email(usuario)
    usuarios_helper.validate_user_exists(usuario_encontrado)
    usuario_creado = usuarios_db.create(usuario)
    return usuario_creado

#### GET BY ID
def get_by_id(usuario_: Usuario) -> Usuario:
    usuario = usuarios_db.get_by_id(usuario_)
    return usuario

#### GET BY MAIL
def get_by_email(usuario_: Usuario) -> Usuario:
    usuario = usuarios_db.get_by_email(usuario_)
    return usuario

#### EDITAR
def edit(usuario: Usuario) -> Usuario:
    return usuarios_db.update_by_id(usuario)

#### DELETE
def delete(usuario: Usuario):
    usuarios_db.delete_by_id(usuario)
    return None