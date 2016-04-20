from flask.views import MethodView
from flask import render_template
from models import Book, Author
import json
import subprocess
import requests

# temporary list for the no DB stage of this project
members = {
    "Richard": {"issues": 17, "commits": 134, "tests": 0, "resp": "Back-end, Flask"},
    "Rachel": {"issues": 5, "commits": 32, "tests": 0, "resp": "Docker/Carina, Database, UML"},
    "Ruzseth": {"issues": 9, "commits": 50, "tests": 0, "resp": "Documentation, Front-end, Scraping"},
    "Timothy": {"issues": 7, "commits": 65, "tests": 0, "resp": "Front-end, Angular, API requests"},
    "Kyung": {"issues": 2, "commits": 18, "tests": 12, "resp": "Testing, RESTful API, Apiary"}
}
total = {"issues": 0, "commits": 0, "tests": 0}
# dynamic snippet to total issues and commits
for name in members:
    attributes = members[name]
    total["issues"] = total["issues"] + attributes["issues"]
    total["commits"] = total["commits"] + attributes["commits"]
    total["tests"] = total["tests"] + attributes["tests"]
members["total"] = total


class IndexView(MethodView):

    def get(self):
        return render_template("home.html")


class AboutView(MethodView):

    def get(self):
        return render_template("about.html", members=members)


class BooksView(MethodView):

    def get(self):
        books = []
        for book in Book.query.all():
            b = book.to_dict()
            if book.author:
                b["first_name"] = book.author.first_name
                b["last_name"] = book.author.last_name
            books.append(b)
        return render_template("books.html", books=books)


class AuthorsView(MethodView):

    def get(self):
        authors = []
        for author in Author.query.all():
            a = author.to_dict()
            a["recent_book"] = author.Books[-1].title
            authors.append(a)
        return render_template("authors.html", authors=authors)


class AuthorView(MethodView):

    def get(self, author_id):
        author = Author.query.get(author_id)
        a = author.to_dict()
        return render_template("author.html", author=a, books=author.Books)


class BookView(MethodView):

    def get(self, book_id):
        book = Book.query.get(book_id)
        b = book.to_dict()
        b["first_name"] = book.author.first_name
        b["last_name"] = book.author.last_name
        return render_template("book.html", book=b)


class BookAPI(MethodView):

    def get(self, book_id):
        if book_id:
            return json.dumps(Book.query.get(book_id).to_dict())
        else:
            books = []
            for book in Book.query.all():
                books.append(book.to_dict())
            return json.dumps(books)


class AuthorAPI(MethodView):

    def get(self, author_id):
        if author_id:
            return json.dumps(Author.query.get(author_id).to_dict())
        else:
            authors = []
            for author in Author.query.all():
                authors.append(author.to_dict())
            return json.dumps(authors)


class RunTests(MethodView):

    def get(self):
        p = subprocess.Popen(["python3", "tests.py"],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
        out, error = p.communicate()
        new_out = ""
        out = out.decode("utf-8")
        error = error.decode("utf-8")
        new_error = ""
        for entry in str(out).split('\n'):
            new_out = new_out + "<br>" + entry
        for entry in str(error).split('\n'):
            new_error = new_error + "<br>" + entry
        return render_template("test.html", out=new_out, error=new_error)


class Search(MethodView):

    def get(self, search_string):
        search_result = []
        if "AND" in search_string:
            search_string = search_string.split("AND")
            if len(search_string) != 2:
                return "error occured OR expects two terms"
            # get both sets then need to find elements in both
            authors_one = Author.query.whoosh_search(search_string[0]).all()
            authors_two = Author.query.whoosh_search(search_string[1]).all()
            authors = []
            for author in authors_one:
                if author in authors_two:
                    authors.append(author)
            # now to repeat above steps but with books
            books_one = Book.query.whoosh_search(search_string[0]).all()
            books_two = Book.query.whoosh_search(search_string[1]).all()
            books = []
            for book in books_one:
                if book in books_two:
                    books.append(book)
            search_string = search_string[0]+" AND "+search_string[1]
        elif "OR" in search_string:
            search_string = search_string.split("OR")
            if len(search_string) != 2:
                return "error occured OR expects two terms"
            authors_one = Author.query.whoosh_search(search_string[0]).all()
            authors_two = Author.query.whoosh_search(search_string[1]).all()
            # snippet to merge two lists
            authors = [x for y in zip(authors_one, authors_two) for x in y]
            if len(authors_one) > len(authors_two):
                authors += authors_one[len(authors_two):len(authors_one)]
            if len(authors_two) > len(authors_one):
                authors += authors_two[len(authors_one):len(authors_two)]
            books_one = Book.query.whoosh_search(search_string[0]).all()
            books_two = Book.query.whoosh_search(search_string[1]).all()
            books = [x for y in zip(books_one, books_two) for x in y]
            if len(books_one) > len(books_two):
                books += books_one[len(books_two):len(books_one)]
            if len(books_two) > len(books_one):
                books += books_two[len(books_one):len(books_two)]
            search_string = search_string[0]+" OR "+search_string[1]
        else:
            authors = Author.query.whoosh_search(search_string).all()
            books = Book.query.whoosh_search(search_string).all()
        search_result = [x for y in zip(authors, books) for x in y]
        if len(authors) > len(books):
            search_result += authors[len(books):len(authors)]
        if len(books) > len(authors):
            search_result += books[len(authors):len(books)]
        return render_template("search.html", result=search_result, search=search_string)


class CocktailIngredients(MethodView):

    def get(self):
        url = 'http://mixopedia.me/api/ingredient'
        ingredients = requests.get(url).json()
        for i in range(len(ingredients)):
            r = requests.get(url + '/' + str(ingredients[i]['id'])).json()[0]
            ingredients[i]['numberOfCocktails'] = r['numberOfCocktails']
            print(i)
        return json.dumps(ingredients)
