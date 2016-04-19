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

    # ----------------
    # Author.to_dict()
    # ----------------

    def test_author_to_dict_1(self):
        with app.app_context():
            testauthor = Author(id=1, first_name='Anthony', last_name='Doerr')
            dictauthor = testauthor.to_dict()
            self.assertEqual(testauthor.first_name, dictauthor['first_name'])

    def test_author_to_dict_2(self):
        with app.app_context():
            testauthor = Author(id=1, first_name='Paula', last_name='Hawkins')
            dictauthor = testauthor.to_dict()
            self.assertEqual(testauthor.last_name, dictauthor['last_name'])

    def test_author_to_dict_3(self):
        with app.app_context():
            testauthor = Author(id=1, first_name='Harper', last_name='Lee', bio='hi')
            dictauthor = testauthor.to_dict()
            self.assertEqual(testauthor.bio, dictauthor['bio'])

    # -----------------
    # Author.get_html()
    # -----------------

    def test_author_get_html_1(self):
        with app.app_context():
            testauthor = Author(id=1, first_name='Anthony', last_name='Doerr')
            htmlauthor = testauthor.get_html('anthony')
            self.assertEqual("<td>Anthony Doerr</td><td><b></i>anthony</i></b> doerr none None None None</td>", htmlauthor)

    # def test_author_get_html_1(self):
    #     with app.app_context():
    #         testauthor = Author(id=1, first_name='Anthony', last_name='Doerr')
    #         htmlauthor = testauthor.get_html('doerr')
    #         self.assertEqual("<td>Anthony Doerr</td><td>anthony <button class='btn btn-primary' disabled=True>doerr</button></td>", htmlauthor)
    
    # -----------------
    # Author.get_link()
    # -----------------
    # def test_author_get_link_1(self):

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

    # --------------
    # Book.to_dict()
    # --------------

    def test_book_to_dict_1(self):
        with app.app_context():
            testbook = Book(id=1, title='ALL THE LIGHT WE CANNOT SEE', isbn='1', summary='hi')
            dictbook = testbook.to_dict()
            self.assertEqual(testbook.title, dictbook['title'])

    def test_book_to_dict_2(self):
        with app.app_context():
            testbook = Book(id=1, title='ALL THE LIGHT WE CANNOT SEE', isbn='1', summary='hi')
            dictbook = testbook.to_dict()
            self.assertEqual(testbook.isbn, dictbook['isbn'])

    def test_book_to_dict_3(self):
        with app.app_context():
            testbook = Book(id=1, title='ALL THE LIGHT WE CANNOT SEE', isbn='1', summary='hi')
            dictbook = testbook.to_dict()
            self.assertEqual(testbook.summary, dictbook['summary'])

    # ---------------
    # Book.get_html()
    # ---------------

    # ---------------
    # Book.get_link()
    # ---------------    


# ----
# Main
# ----

if __name__ == '__main__':
    main()
