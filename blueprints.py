from flask import Blueprint
from views import IndexView, AboutView
from views import BooksView

blueprint = Blueprint('idb', __name__, template_folder='templates')


blueprint.add_url_rule('/', view_func=IndexView.as_view('Home'))
blueprint.add_url_rule('/about', view_func=AboutView.as_view('About'))
blueprint.add_url_rule('/books', view_func=BooksView.as_view('Books'))
