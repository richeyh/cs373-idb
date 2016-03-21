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

# ----------
# TestModels
# ----------

class TestModels (TestCase):

	# ----
	# Book
	# ----

	def test_model_book_1(self):
		testbook = Book(1, '1234', 'The Book', 'About the book', '$100.00', '2016-3-21', 'New York Times', 'image', 1, 1)
		self.assertEqual(testbook.title, 'The Book')
		self.assertEqual(testbook.id, 1)

# ----
# Main
# ----

if __name__ == '__main__' :
	main()
