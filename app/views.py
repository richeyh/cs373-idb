from flask.views import MethodView
from flask import render_template

# temporary list for the no DB stage of this project
members = {
    "Richard": {"issues": 5, "commits": 5, "tests": 0, "resp": "backend and flask"},
    "Rachel": {"issues": 5, "commits": 5, "tests": 0, "resp": "docker and uml"},
    "Ruzseth": {"issues": 5, "commits": 5, "tests": 0, "resp": "documentation and html"},
    "Timothy": {"issues": 5, "commits": 5, "tests": 0, "resp": "html and angular"},
    "Kyung": {"issues": 5, "commits": 5, "tests": 0, "resp": "unit tests and apiuary"}
}
books = [{"title": 'All the Light We Cannot See',
          "first_name": 'Anthony', "last_name": 'Doerr',
          "publisher": 'Scribner', "best_seller_list": 'Hardcover',
          "best_seller_date": '2016-03-12', "ISBN": '9781476746586',
          "Link": "", "id": 1},
         {"title": 'The Girl on the Train', "first_name": 'Paula',
          "last_name": 'Hawkins', "publisher": 'Riverhead',
          "best_seller_list": 'Hardcover', "best_seller_date": '2016-03-12',
             "ISBN": '9781594633669',
             "id": 2, "Link": ""},
         {"title": 'Go Set a Watchman', "first_name": 'Harper',
          "last_name": 'Lee', "publisher": 'HarperCollins',
          "best_seller_list": 'Hardcover', "best_seller_date": '2016-03-12',
             "ISBN": '9780062409850', "id": 3, "Link": ""}
         ]

authors = [{"last_name": 'Doerr', "first_name": 'Anthony',
            "book_count": 1, "recent_book": books[0]["title"],
            "best_seller_date": '2016-03-12', "id":1},
           {"last_name": 'Hawkins', "first_name": 'Paula',
            "book_count": 1, "recent_book": books[1]["title"],
            "best_seller_date": '2016-03-12', "id":2},
           {"last_name": 'Lee', "first_name": 'Harper',
            "book_count": 1, "recent_book": books[2]["title"],
            "best_seller_date": '2016-03-12', "id":3}
           ]


class IndexView(MethodView):

    def get(self):
        return render_template("home.html")


class AboutView(MethodView):

    def get(self):
        # dynamic snippet to total issues and commits
        total = {"issues": 0, "commits": 0, "tests": 0}
        for name in members:
            attributes = members[name]
            total["issues"] = total["issues"] + attributes["issues"]
            total["commits"] = total["commits"] + attributes["commits"]
            total["tests"] = total["tests"] + attributes["tests"]
        members["total"] = total
        return render_template("about.html", members=members)


class BooksView(MethodView):

    def get(self):
        return render_template("books.html", books=books)


class AuthorsView(MethodView):

    def get(self):
        return render_template("authors.html", authors=authors)


class AuthorView(MethodView):

    def get(self, author_id):
        a = authors[author_id]
        return render_template("author.html", author=a)


class BookView(MethodView):

    def get(self, book_id):
        b = books[book_id]
        return render_template("book.html", book=b)
