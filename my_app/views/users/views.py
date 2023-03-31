from flask import Blueprint
from flask import render_template
from my_app.views.users.models import USERS

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/usuario')
def home():
    return render_template('usuario/user.html', users=USERS)

