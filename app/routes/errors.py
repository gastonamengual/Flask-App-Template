from flask import Blueprint, flash, redirect, url_for

from ..models.exceptions import EntityExists, NoEntitiesRegistered

errors_scope = Blueprint("errors", __name__)

@errors_scope.app_errorhandler(NoEntitiesRegistered)
def handle_user_not_found(NoEntitiesRegistered):
    flash('No entities registered')
    return redirect(url_for('views.usuarios_views.login'))

@errors_scope.app_errorhandler(EntityExists)
def handle_entity_exists(inst):
    message, path, route = inst.args
    flash(message)
    return redirect(url_for(f'views.{path}.{route}'))