from flask import Blueprint, render_template, request, jsonify
from ...controllers import usuarios_controller
from ...models.models import Usuario

from flask_mail import Mail, Message
import numpy as np

mail = Mail()

usuarios_scope = Blueprint('usuarios_views', __name__,)

### LOGIN
@usuarios_scope.route('/')
@usuarios_scope.route('/login')
def login():
    return render_template('usuarios/login.html')

### REGISTER
@usuarios_scope.route('/register')
def register():
    return render_template('usuarios/register.html')

### RESET PASSWORD
@usuarios_scope.route('/reset_password/<token>')
def reset_password(token):
    if len(token) > 1:
        user_id = token[:len(token) - 5]
    else:
        user_id = token
    return render_template("usuarios/reset_password.html", user_id=user_id)

### EDITAR
@usuarios_scope.route('/editar')
def editar():
    usuario_id = request.cookies.get('usuario_id')
    usuario_ = Usuario(id_=usuario_id)
    usuario = usuarios_controller.get_by_id(usuario_)
    
    return render_template("usuarios/usuario_editar.html", usuario=usuario)

### FORGOT PASSWORD
@usuarios_scope.route('/forgot_password/')
def forgot_password():
    return render_template("usuarios/forgot_password.html")

### VALIDATE MAIL
@usuarios_scope.post('/validate_mail/')
def validate_mail():
    data = request.form.to_dict()
    email = (list(data.values()))[0]
    usuario_ = Usuario(email=email)
    try:
        usuario = usuarios_controller.get_by_email(usuario_)
    except:
        usuario = None
    return jsonify(usuario)

### SEND MAIL
@usuarios_scope.post('/send_mail/')
def send_mail():
    
    data = request.form.to_dict()
    email_usuario = (list(data.values()))[0]
    usuario_ = Usuario(email=email_usuario)
    usuario = usuarios_controller.get_by_email(usuario_)

    subject = 'Cambio de contraseña - Comienza tu Emprendimiento'
    token = list(np.random.randint(0, 10, 5))
    token = [str(int) for int in token]
    token = "".join(token)

    body = f'Para cambiar la contraseña, hacé click en el siguiente link: https://emprendeapp.herokuapp.com/reset_password/{usuario.id_}{token}'
    msg = Message(subject=subject,
                sender="emprendeapp2022@gmail.com",
                recipients=[email_usuario], 
                body=body)
    mail.send(msg)

    return 'success'
