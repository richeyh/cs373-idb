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


class IndexView(MethodView):

    def get(self):
        return render_template("home.html")


class AboutView(MethodView):

    def get(self):
        return render_template("about.html", members=members)
