#!/usr/bin/env python3

# -------------------------------
# Copyright (C) 2016
# IBDB
# -------------------------------

# -------
# Imports
# -------

from io             import StringIO
from urllib.request import urlopen
from unittest       import main, TestCase
from models 		import *
import json, postgresql
import datetime

# ----------
# TestModels
# ----------

class TestModels (TestCase):

	# ------
	# Author
	# ------

	def test_model_author_1(self):
		testauthor = Author.query.get(1)
		self.assertEqual(testauthor.id, 1)

	def test_model_author_2(self):
		testauthor = Author.query.filter_by(first_name='Anthony', last_name='Doerr')
		self.assertEqual(testauthor[0].first_name='Anthony')
		self.assertEqual(testauthor[0].last_name='Doerr')

	def test_model_author_3(self):
		testauthor = Author.query.filter_by(first_name='Paula', last_name='Hawkins')
		self.assertEqual(testauthor[0].books[0].title='THE GIRL ON THE TRAIN')

	# ----
	# Book
	# ----

	def test_model_book_1(self):
		testbook = Book.query.get(1)
		self.assertEqual(testbook.id, 1)

	def test_model_book_2(self):
		testbook = Book.query.filter_by(title='ALL THE LIGHT WE CANNOT SEE').all()
		self.assertEqual(testbook[0].title, 'ALL THE LIGHT WE CANNOT SEE')

	def test_model_book_3(self):
		testbook = Book.query.filter_by(title='THE GIRL ON THE TRAIN').all()
		self.assertEqual(testbook[0].author.first_name, 'Paula')

	# ----------
	# TeamMember
	# ----------

	def test_model_teammember_1(self):
		testmember = TeamMember.query.get(1)
		self.assertEqual(testmember.id, 1)

	def test_model_teammember_2(self):
		testmember = TeamMember.query.filter_by(name='Richard Huettel')
		self.assertEqual(testmember[0].name='Richard Huettel')

	def test_model_teammember_3(self):
		testmember = TeamMember.query.filter_by(name='Rachel Choi')
		self.assertEqual(testmember[0].name='Rachel Choi')

# ----
# Main
# ----

if __name__ == '__main__' :
	main()
