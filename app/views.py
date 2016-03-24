from flask.views import MethodView
from flask import render_template

# temporary list for the no DB stage of this project
members = {
    "Richard": {"issues": 5, "commits": 5, "tests": 0, "resp": "Back-end, Flask"},
    "Rachel": {"issues": 5, "commits": 5, "tests": 0, "resp": "Docker, Uml"},
    "Ruzseth": {"issues": 5, "commits": 5, "tests": 0, "resp": "Documentation, Front-end"},
    "Timothy": {"issues": 5, "commits": 5, "tests": 0, "resp": "Front-end, Angular"},
    "Kyung": {"issues": 5, "commits": 5, "tests": 0, "resp": "Testing, Apiary"}
}
books = [{"title": 'All the Light We Cannot See',
          "first_name": 'Anthony', "last_name": 'Doerr',
          "publisher": 'Scribner', "best_seller_list": 'Hardcover',
          "best_seller_date": '2016-03-12', "ISBN": '9781476746586',
          "book_image": "http://t2.gstatic.com/images?q=tbn:ANd9GcQNwFitSZQv7-IP7HkD6AJv_1M0VF4cQ5ydz6dlQU_w9IipF2zu", "id": 0, "author_id": 0},
         {"title": 'The Girl on the Train', "first_name": 'Paula',
          "last_name": 'Hawkins', "publisher": 'Riverhead',
          "best_seller_list": 'Hardcover', "best_seller_date": '2016-03-12',
             "ISBN": '9781594633669',
             "id": 1, "book_image": "http://t0.gstatic.com/images?q=tbn:ANd9GcT7qekXzNKAn6ca_gmMP0yczMpJuhN5FAE80JbbYs5aYXk4u7Dd", "author_id": 1},
         {"title": 'Go Set a Watchman', "first_name": 'Harper',
          "last_name": 'Lee', "publisher": 'HarperCollins',
          "best_seller_list": 'Hardcover', "best_seller_date": '2016-03-12',
             "ISBN": '9780062409850', "id": 2, "book_image": "http://www.wired.com/wp-content/uploads/2015/07/go-set-a-watchman-582x890.jpg", "author_id": 2}
             ]

authors = [{"last_name": 'Doerr', "first_name": 'Anthony',
            "book_count": 1, "recent_book": books[0]["title"],
            "best_seller_date": '2016-03-12', "id":0, "Link": "https://www.facebook.com/anthonydoerr","book_id":0},
           {"last_name": 'Hawkins', "first_name": 'Paula',
            "book_count": 1, "recent_book": books[1]["title"],
            "best_seller_date": '2016-03-12', "id":1, "Link": "https://www.facebook.com/PaulaHawkinsWriter", "book_id":1},
           {"last_name": 'Lee', "first_name": 'Harper',
            "book_count": 1, "recent_book": books[2]["title"],
            "best_seller_date": '2016-03-12', "id":2, "Link": "https://www.facebook.com/harperlee", "book_id":2}
           ]
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
        return render_template("books.html", books=books)


class AuthorsView(MethodView):

    def get(self):
        return render_template("authors.html", authors=authors)


class AuthorView(MethodView):

    def get(self, author_id):
        a = authors[int(author_id)]
        return render_template("author.html", author=a)


class BookView(MethodView):

    def get(self, book_id):
        b = books[int(book_id)]
        return render_template("book.html", book=b)
