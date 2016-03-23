import requests

idbndb_url = "http://isbndb.com/api/v2/json/H2ZRJDOE"
categories = ['science', 'computers']
# r = requests.get(isbndb_url+'/books?q=computers&p=1000')
times_keys = {"books": "f431b40e10777623a234404cda616c35:12:74671670",
              "popular": "b90ce9925426c6515a4d912e1f3d5851:10:74671670"}
best_seller_url = "http://api.nytimes.com/svc/books/v2/"
lists = ["combined-print-and-e-book-fiction",
         "combined-print-and-e-book-nonfiction"
         "hardcover-fiction",
         "hardcover-nonfiction",
         "trade-fiction-paperback",
         "mass-market-paperback",
         "paperback-nonfiction",
         "e-book-fiction",
         "e-book-nonfiction",
         "hardcover-advice",
         "paperback-advice",
         "advice-how-to-and-miscellaneous",
         "picture-books",
         "chapter-books",
         "childrens-middle-grade",
         "young-adult",
         "paperback-books",
         "childrens-middle-grade-hardcover",
         "childrens-middle-grade-paperback",
         "childrens-middle-grade-e-book",
         "young-adult-hardcover",
         "young-adult-paperback",
         "young-adult-e-book",
         "series-books",
         "hardcover-graphic-books",
         "paperback-graphic-books",
         "manga",
         "combined-print-fiction",
         "combined-print-nonfiction",
         "animals",
         "business-books",
         "celebrities",
         "crime-and-punishment",
         "culture",
         "education",
         "espionage",
         "expeditions-disasters-and-adventures",
         "family",
         "fashion-manners-and-customs",
         "food-and-fitness"]

r = requests.get("http://api.nytimes.com/svc/books/v2/lists/" +
                 lists[0] + ".json?api-key=" + times_keys["books"])
result = r.json()
print(result["results"])
