from flask import Blueprint, render_template, url_for
from flask import current_app as app

from flask_jinja_tut.api import fetch_products


home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static')


@home_bp.route('/blueprints/', methods=['GET'])
def home():
    """Homepage."""
    products = fetch_products(app)
    return render_template(
        'blueprints_home.html',
        title='Flask Blueprint Demo',
        subtitle='Demonstration of Flask blueprints in action.',
        template='home-template',
        products=products,
        nav=[
            {'name': 'Back home', 'url': url_for('home')},
        ]
    )
