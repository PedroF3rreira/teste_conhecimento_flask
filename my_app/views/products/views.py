from flask import Blueprint
from flask import render_template
from my_app.views.products.models import PRODUCTS

product_blueprint = Blueprint('product', __name__)


@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)


@product_blueprint.route('/produto/<key>')
def produto(key):
    produto = PRODUCTS.get(key)
    return render_template('produto/produto.html', produto=produto)


@product_blueprint.route('/produto/<id>/deletar', methods=['GET', 'DELETE'])
def product_delete(id):
    produto = PRODUCTS.get(id)
    return f'{ produto }'
