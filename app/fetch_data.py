# import requests
from urllib.request import urlopen
import json

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
         b = {}
         b["title"] = book["title"]
         b["best_seller_list"] = result["results"]["list_name"]
         b["weeks_on_list"] = book["weeks_on_list"]
         b["ISBN"] = book["primary_isbn13"]
         b["publisher"] = book["publisher"]
         b["summary"] = book["description"]
         b["author"] = book["author"]
         b["book_image"] = book["book_image"]
         # book_url = book["book_image"]
         # b["book_image"] = "".join(book_url.split('\\'))
         b["amazon_link"] = book["amazon_product_url"]
         # amazon_url = book["amazon_product_url"]
         # b["amazon_link"] = "".join(amazon_url.split('\\'))
         library.append(b)
         count+=1
   book_lists[l] = library

print(book_lists)

# print(result["results"])
