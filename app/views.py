from flask.views import MethodView
from flask import render_template
from flask import Response
from models import Book, Author
import json
import os

# temporary list for the no DB stage of this project
members = {
    "Richard": {"issues": 6, "commits": 63, "tests": 0, "resp": "Back-end, Flask"},
    "Rachel": {"issues": 4, "commits": 17, "tests": 0, "resp": "Docker, Uml"},
    "Ruzseth": {"issues": 9, "commits": 48, "tests": 0, "resp": "Documentation, Front-end, Scraping"},
    "Timothy": {"issues": 4, "commits": 51, "tests": 0, "resp": "Front-end, Angular, API requests"},
    "Kyung": {"issues": 2, "commits": 5, "tests": 12, "resp": "Testing, Apiary"}
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
            a["recent_book"]=author.Books[-1].title
            authors.append(a)
        return render_template("authors.html", authors=authors)


class AuthorView(MethodView):

    def get(self, author_id):
        a = Author.query.get(author_id)
        a = a.to_dict()
        a["recent_book"]=author.Books[-1].title
        return render_template("author.html", author=a)


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
            return json.dumps(Book.query.get(book_id))
        else:
            return json.dumps(Book.query.all())


class AuthorAPI(MethodView):

    def get(self, author_id):
        if author_id:
            return json.dumps(Author.query.get(author_id))
        else:
            return json.dumps(Author.query.all())


class RunTests(MethodView):

    def get(self):
        os.system("python3 tests.py > tests.tmp")
        return Response(open('tests.tmp', 'r').read(), mimetype='text/plain')
