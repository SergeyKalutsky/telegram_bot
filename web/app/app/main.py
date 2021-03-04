
from app.core.config import DefaultConfig
from app.core.extentions import login_manager
from app.db.db import db
from flask_login import current_user
from flask import render_template, Flask
from flask_principal import Principal, Permission, RoleNeed, identity_loaded, UserNeed

# Import Blueprints
from app.blueprints.frontend.views import frontend
from app.blueprints.data_collection.views import data_collection

app = Flask(__name__)
app.config.from_object(DefaultConfig)


# Register blueprints
app.register_blueprint(frontend)
app.register_blueprint(data_collection)

# Extention configs
login_manager.init_app(app)
login_manager.login_view = "frontend.login"
login_manager.setup_app(app)
db.init_app(app)
principals = Principal(app)
admin_permission = Permission(RoleNeed('admin'))


@app.errorhandler(403)
def authorisation_failed(e):
    message = 'Для доступа на страницу необходимы права администратора'
    return render_template('base.html', text=message)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user

    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    # Assuming the User model has a list of roles, update the
    # identity with the roles that the user provides
    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role))