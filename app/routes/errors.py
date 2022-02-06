from flask import Blueprint, flash, redirect, url_for

from ..models.exceptions import UserNotFound, EmailInvalidFormat, EntityExists

errors_scope = Blueprint("errors", __name__)

@errors_scope.app_errorhandler(UserNotFound)
def handle_user_not_found(UserNotFound):
    flash('El email o la contraseña son incorrectos')
    return redirect(url_for('views.usuarios_views.login'))

@errors_scope.app_errorhandler(EmailInvalidFormat)
def handle_email_invalid_format(EmailInvalidFormat):
    flash('El email no tiene el formato correcto')
    return redirect(url_for('views.register_views.register'))

@errors_scope.app_errorhandler(EntityExists)
def handle_entity_exists(inst):
    message, path, route = inst.args
    flash(message)
    return redirect(url_for(f'views.{path}.{route}'))