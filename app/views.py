from flask.views import MethodView
from flask import render_template
from flask import Response
from models import Book, Author
import json
import subprocess

# temporary list for the no DB stage of this project
members = {
    "Richard": {"issues": 17, "commits": 134, "tests": 0, "resp": "Back-end, Flask"},
    "Rachel": {"issues": 5, "commits": 32, "tests": 0, "resp": "Docker, Uml"},
    "Ruzseth": {"issues": 9, "commits": 50, "tests": 0, "resp": "Documentation, Front-end, Scraping"},
    "Timothy": {"issues": 7, "commits": 65, "tests": 0, "resp": "Front-end, Angular, API requests"},
    "Kyung": {"issues": 2, "commits": 18, "tests": 12, "resp": "Testing, Apiary"}
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
        a["recent_book"] = author.Books[-1].title
        a["book_id"] = author.Books[-1].id
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
        out = str(out)
        error = str(error)
        out = out.replace('\n', "<br>")
        error = error.replace('\n', "<br>")
        return render_template("test.html", out=out, error=error)
