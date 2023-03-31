from flask import Flask
from my_app.views.products.views import product_blueprint
from my_app.views.users.views import users_blueprint

app = Flask(__name__)
app.register_blueprint(product_blueprint)
app.register_blueprint(users_blueprint)
