# import requests
from urllib.request import urlopen
import json
from models.py import Author, Book

idbndb_url = "http://isbndb.com/api/v2/json/H2ZRJDOE"
categories = ['science', 'computers']
# r = requests.get(isbndb_url+'/books?q=computers&p=1000')
times_keys = {"books": "f431b40e10777623a234404cda616c35:12:74671670",
              "popular": "b90ce9925426c6515a4d912e1f3d5851:10:74671670"}
best_seller_url = "http://api.nytimes.com/svc/books/v2/"
# lists = ["combined-print-and-e-book-fiction",
#          "combined-print-and-e-book-nonfiction"
#          "hardcover-fiction",
#          "hardcover-nonfiction",
#          "trade-fiction-paperback",
#          "mass-market-paperback",
#          "paperback-nonfiction",
#          "e-book-fiction",
#          "e-book-nonfiction",
#          "hardcover-advice",
#          "paperback-advice",
#          "advice-how-to-and-miscellaneous",
#          "picture-books",
#          "chapter-books",
#          "childrens-middle-grade",
#          "young-adult",
#          "paperback-books",
#          "childrens-middle-grade-hardcover",
#          "childrens-middle-grade-paperback",
#          "childrens-middle-grade-e-book",
#          "young-adult-hardcover",
#          "young-adult-paperback",
#          "young-adult-e-book",
#          "series-books",
#          "hardcover-graphic-books",
#          "paperback-graphic-books",
#          "manga",
#          "combined-print-fiction",
#          "combined-print-nonfiction",
#          "animals",
#          "business-books",
#          "celebrities",
#          "crime-and-punishment",
#          "culture",
#          "education",
#          "espionage",
#          "expeditions-disasters-and-adventures",
#          "family",
#          "fashion-manners-and-customs",
#          "food-and-fitness"]


lists = ["hardcover-fiction", 
         "hardcover-nonfiction", 
         "picture-books", 
         "childrens-middle-grade-hardcover",
         "young-adult-hardcover",
         "hardcover-graphic-books",
         "paperback-graphic-books",
         "manga"]


"""
result["results"]["list_name"] = Category of best sellers list 
result["results"]["books"]["weeks_on_list"] = Weeks book has been on list
result["results"]["books"]["primary_isbn13"] = ISBN of book
result["results"]["books"]["publisher"] = Publisher of book
result["results"]["books"]["description"] = Description of book
result["results"]["books"]["title"] = Title of book
result["results"]["books"]["author"] = Author of book
result["results"]["books"]["book_image"] = Image of book
result["results"]["books"]["amazon_product_url"] = Amazon page of book
"""

# r = requests.get("http://api.nytimes.com/svc/books/v2/lists/" +
#                  lists[0] + ".json?api-key=" + times_keys["books"])





   
for l in lists:
   r = urlopen("http://api.nytimes.com/svc/books/v3/lists/" +
                 l + ".json?api-key=" + times_keys["books"])
   rInfo = r.info()
   rRaw = r.read().decode(rInfo.get_content_charset('utf8'))
   result = json.loads(rRaw)

   # Make a dictionary of the list categories
   book_lists = {}

   # Make a list of book dictionaries
   library = []
   books = result["results"]["books"]
   for book in books:
         count = 0
         if count == 10:
            break
         
         book_title = book["title"]
         book_best_seller_list = result["results"]["list_name"]
         book_best_seller_date = result["results"]["bestsellers_date"]
         # b["weeks_on_list"] = book["weeks_on_list"]
         book_isbn = book["primary_isbn13"]
         book_publisher = book["publisher"]
         book_summary = book["description"]
         book_book_image = book["book_image"]
         book_amazon_link = book["amazon_product_url"]
         # book_url = book["book_image"]
         # b["book_image"] = "".join(book_url.split('\\'))
         # amazon_url = book["amazon_product_url"]
         # b["amazon_link"] = "".join(amazon_url.split('\\'))

         a = book["author"]
         single_author = a.split(' and ')[0]
         lastName = single_author.split(' ')[1]
         firstName = single_author.split(' ')[0]
         book_author = Author(first_name=firstName, last_name=lastName)

         b = Book(isbn=book_isbn, 
                  title=book_title, 
                  summary=book_summary, 
                  best_seller_date=book_best_seller_date,
                  best_seller_list=book_best_seller_list,
                  book_image=book_book_image,
                  amazon_link=book_amazon_link,
                  publisher=book_publisher)
         b.author = book_author
         library.append(b)
         count+=1
   book_lists[l] = library

print(book_lists[0])

# print(result["results"])
