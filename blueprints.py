from flask import Blueprint
from views import IndexView

blueprint = Blueprint('idb', __name__, template_folder='templates')


blueprint.add_url_rule('/', view_func=IndexView.as_view('Home'))
