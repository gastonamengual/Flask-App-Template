
from flask import Blueprint, request, redirect, url_for, make_response, flash

from ...controllers import usuarios_controller
from ...models.models import Usuario

usuarios_scope = Blueprint('usuarios_api', __name__, url_prefix='/usuarios_api')

### LOGIN
@usuarios_scope.route('/login', methods=['POST'])
def login():
    data = request.form
    usuario = Usuario(id_ = None,
                      nombre = None,
                      email = data["email"],
                      password = data["password"])

    usuario = usuarios_controller.login(usuario)

    resp = make_response(redirect(url_for('views.emprendimientos_views.emprendimientos')))
    print(url_for('views.emprendimientos_views.emprendimientos'))
    resp.set_cookie('usuario_id', usuario.id_)

    return resp

#### REGISTER
@usuarios_scope.route('/register', methods=['POST'])
def register():
    data = request.form
    usuario = Usuario(id_ = None,
                      nombre = data["nombre"], 
                      email = data["email"],
                      password = data["password"])

    usuario = usuarios_controller.create(usuario)

    resp = make_response(redirect(url_for('views.emprendimientos_views.emprendimientos')))
    resp.set_cookie('usuario_id', usuario.id_)
   
    return resp

#### EDITAR
@usuarios_scope.route('/editar', methods=['POST'])
def editar():

    data = request.form

    usuario = Usuario(id_ = data.get("id_"),
                      nombre = data['nombre'],
                      email = data['email'], 
                      password = data['password'])

    usuarios_controller.edit(usuario)
    flash('Usuario editado con éxito!')
    return redirect(url_for('views.emprendimientos_views.emprendimientos'))

#### BORRAR
@usuarios_scope.route('/borrar', methods=['POST'])
def borrar():

    data = request.form

    usuario = Usuario(id_ = data.get("id_"))

    return redirect(url_for('views.emprendimientos_views.emprendimientos'))

#### RESET PASSWORD
@usuarios_scope.route('/reset_password', methods=['POST'])
def reset_password():

    data = request.form

    usuario_id = data.get("id_")
    usuario_ = Usuario(id_=usuario_id)  
    usuario = usuarios_controller.get_by_id(usuario_)
    
    password_actual = data['password_actual']
    password_nueva = data['password_nueva']
    password_confirmar = data['password_confirmar']

    if password_actual == usuario.password:

        if password_nueva == password_confirmar:
            usuario.password = password_nueva

            usuarios_controller.edit(usuario)
            flash('Contraseña cambiada con éxito!')
            return redirect(url_for('views.emprendimientos_views.emprendimientos'))
        else:
            flash('Las contraseñas no coinciden!')
            return redirect(url_for('views.usuarios_views.reset_password', token=usuario_id))
    else:
        flash('La contraseña actual no es correcta')
        return redirect(url_for('views.usuarios_views.reset_password', token=usuario_id))