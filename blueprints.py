from flask import Blueprint
from views import IndexView, AboutView
from views import BooksView, AuthorsView
from views import BookView, AuthorView

blueprint = Blueprint('idb', __name__, template_folder='templates')


blueprint.add_url_rule('/', view_func=IndexView.as_view('Home'))
blueprint.add_url_rule('/about', view_func=AboutView.as_view('About'))
blueprint.add_url_rule('/books', view_func=BooksView.as_view('Books'))
blueprint.add_url_rule('/authors', view_func=AuthorsView.as_view('Authors'))
blueprint.add_url_rule(
    '/author/<author_id>', view_func=AuthorView.as_view('Author'))
blueprint.add_url_rule('/book/<book_id>', view_func=BookView.as_view('Book'))
