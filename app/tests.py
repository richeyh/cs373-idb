#!/usr/bin/env python3

# -------------------------------
# Copyright (C) 2016
# IBDB
# -------------------------------

# -------
# Imports
# -------

from unittest import main, TestCase
from models import *
from app import app
# ----------
# TestModels
# ----------


class TestModels (TestCase):

    # ------
    # Author
    # ------

    def test_model_author_1(self):
        with app.app_context():
            testauthor = Author.query.get(1)
            self.assertEqual(testauthor.id, 1)

    def test_model_author_2(self):
        with app.app_context():
            testauthor = Author.query.filter_by(
                first_name='Anthony', last_name='Doerr')
            self.assertEqual(testauthor[0].first_name, 'Anthony')
            self.assertEqual(testauthor[0].last_name, 'Doerr')

    def test_model_author_3(self):
        with app.app_context():
            testauthor = Author.query.filter_by(
                first_name='Paula', last_name='Hawkins')
            self.assertEqual(
                testauthor[0].Books[0].title, 'THE GIRL ON THE TRAIN')

    # ----
    # Book
    # ----

    def test_model_book_1(self):
        with app.app_context():
            testbook = Book.query.get(1)
            self.assertEqual(testbook.id, 1)

    def test_model_book_2(self):
        with app.app_context():
            testbook = Book.query.filter_by(
                title='ALL THE LIGHT WE CANNOT SEE').all()
            self.assertEqual(testbook[0].title, 'ALL THE LIGHT WE CANNOT SEE')

    def test_model_book_3(self):
        with app.app_context():
            testbook = Book.query.filter_by(
                title='THE GIRL ON THE TRAIN').all()
            self.assertEqual(testbook[0].author.first_name, 'Paula')

# ----
# Main
# ----

if __name__ == '__main__':
    main()
