from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session
from app.db.db import User, auth
from flask_login import login_user, logout_user, login_required
from flask_principal import Identity, identity_changed, AnonymousIdentity
from app.core.extentions import login_manager


frontend = Blueprint('frontend', __name__)

@frontend.route("/")
@login_required
def home():
    return render_template('base.html')


@login_manager.user_loader
def load_user(login):
    record = auth(login)
    if record:
        return User(login, record.access)


@frontend.route('/logout')
def logout():
    logout_user()

    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())
    return 'Logged out'


@frontend.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        login = request.form['username']
        record = auth(login)
        if record is not None and record.password == request.form['password']:
            user = User(login, record.access)
            login_user(user, remember=True)

            # Tell Flask-Principal the identity changed
            identity_changed.send(current_app._get_current_object(),
                                  identity=Identity(user.id))
            return redirect(url_for('frontend.home'))

        else:
            flash('Неверное имя пользователя или пароль', 'error')
            return redirect(url_for('frontend.login'))
    else:
        return render_template('login.html')