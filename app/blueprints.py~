from flask import Blueprint
from views import IndexView, AboutView
from views import BooksView, AuthorsView
from views import BookView, AuthorView
from views import BookAPI, AuthorAPI
from views import RunTests, Search
from views import CocktailIngredients

blueprint = Blueprint('idb', __name__, template_folder='templates')


blueprint.add_url_rule('/', view_func=IndexView.as_view('Home'))
blueprint.add_url_rule('/about', view_func=AboutView.as_view('About'))
blueprint.add_url_rule('/books', view_func=BooksView.as_view('Books'))
blueprint.add_url_rule('/authors', view_func=AuthorsView.as_view('Authors'))
blueprint.add_url_rule(
    '/author/<author_id>', view_func=AuthorView.as_view('Author'))
blueprint.add_url_rule('/book/<book_id>', view_func=BookView.as_view('Book'))
blueprint.add_url_rule(
    '/api/books/', defaults={'book_id': None},
    view_func=BookAPI.as_view('BooksAPI'))
blueprint.add_url_rule(
    '/api/books/<book_id>', view_func=BookAPI.as_view('BookAPI'))
blueprint.add_url_rule(
    '/api/authors/', defaults={'author_id': None},
    view_func=AuthorAPI.as_view('AuthorsAPI'))
blueprint.add_url_rule(
    '/api/authors/<author_id>', view_func=AuthorAPI.as_view('AuthorAPI'))
blueprint.add_url_rule('/tests', view_func=RunTests.as_view('RunTests'))
blueprint.add_url_rule(
    '/search/<search_string>', view_func=Search.as_view('Search'))
blueprint.add_url_rule(
    '/CocktailIngredients', view_func=CocktailIngredients.as_view('CocktailIngredients'))
