from flask.views import MethodView
from flask import render_template
from models import Book, Author
import json

# temporary list for the no DB stage of this project
members = {
    "Richard": {"issues": 6, "commits": 63, "tests": 0, "resp": "Back-end, Flask"},
    "Rachel": {"issues": 4, "commits": 17, "tests": 0, "resp": "Docker, Uml"},
    "Ruzseth": {"issues": 9, "commits": 48, "tests": 0, "resp": "Documentation, Front-end"},
    "Timothy": {"issues": 4, "commits": 51, "tests": 0, "resp": "Front-end, Angular"},
    "Kyung": {"issues": 2, "commits": 5, "tests": 6, "resp": "Testing, Apiary"}
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
            books.append(book.to_dict())
        return render_template("books.html", books=books)


class AuthorsView(MethodView):

    def get(self):
        authors = []
        for author in Author.query.all():
            authors.append(author.to_dict())
        return render_template("authors.html", authors=authors)


class AuthorView(MethodView):

    def get(self, author_id):
        a = Author.query.get(author_id)
        a = a.to_dict()
        return render_template("author.html", author=a)


class BookView(MethodView):

    def get(self, book_id):
        b = Book.query.get(book_id)
        b = b.to_dict()
        return render_template("book.html", book=b)


class BookAPI(MethodView):

    def get(self, book_id):
        if book_id:
            return json.dumps(Book.query.get(book_id))
        else:
            return json.dumps(Book.query.all())


class AuthorAPI(MethodView):

    def get(self, author_id):
        if author_id:
            return json.dumps(Author.query.get(author_id))
        else:
            return json.dumps(Author.query.all())
