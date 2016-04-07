# import requests
from urllib.request import urlopen
import json
from models import Author, Book
from Scraper import bookScrape
from app import app
from extensions import DB

# idbndb_url = "http://isbndb.com/api/v2/json/H2ZRJDOE"
# categories = ['science', 'computers']
# r = requests.get(isbndb_url+'/books?q=computers&p=1000')
times_keys = {"books": "f431b40e10777623a234404cda616c35:12:74671670",
              "popular": "b90ce9925426c6515a4d912e1f3d5851:10:74671670"}
best_seller_url = "http://api.nytimes.com/svc/books/v3/"

lists = ["combined-print-and-e-book-fiction",
         "combined-print-and-e-book-nonfiction",
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
         "food-and-fitness",
         "games-and-activities",
         "hardcover-business-books",
         "health",
         "humor",
         "indigenous-americans",
         "paperback-business-books",
         "hardcover-political-books",
         "race-and-civil-rights",
         "relationships",
         "religion-spirituality-and-faith",
         "science",
         "sports",
         "travel"]


# result["results"]["list_name"] = Category of best sellers list
# result["results"]["books"]["weeks_on_list"] = Weeks book has been on list
# result["results"]["books"]["primary_isbn13"] = ISBN of book
# result["results"]["books"]["publisher"] = Publisher of book
# result["results"]["books"]["description"] = Description of book
# result["results"]["books"]["title"] = Title of book
# result["results"]["books"]["author"] = Author of book
# result["results"]["books"]["book_image"] = Image of book
# result["results"]["books"]["amazon_product_url"] = Amazon page of book
for category in lists:
    r = urlopen("http://api.nytimes.com/svc/books/v3/lists/" +
                category + ".json?api-key=" + times_keys["books"])
    rInfo = r.info()
    rRaw = r.read().decode(rInfo.get_content_charset('utf8'))
    result = json.loads(rRaw)

    # Make a dictionary of the list categories
    book_lists = {}

    # Make a list of book objects
    list_of_book_objects = []
    try:
        books = result["results"]["books"]
    except Exception as e:
        print("*"*80)
        print(result)
        print(category)
        print("*"*80)
        books = []
    for book in books:

        # Empty list
        del list_of_book_objects[:]

        # Book title
        book_title = book["title"]

        # Best Seller List Name
        book_best_seller_list = result["results"]["list_name"]

        # Best Seller List date
        book_best_seller_date = result["results"]["bestsellers_date"]

        # ISBN
        book_isbn = book["primary_isbn13"]

        # Publisher
        book_publisher = book["publisher"]

        # Summary
        book_summary = book["description"]

        # Image
        book_book_image = book["book_image"]

        # Amazon link
        book_amazon_link = book["amazon_product_url"]

        # Author object
        a = book["author"]
        single_author = a.split(' and ')[0]
        if len(single_author.split(' ')) >= 2:
            lastName = single_author.split(' ')[1]
        else:
            lastName = "None"
        firstName = single_author.split(' ')[0]
        with app.app_context():
            author = Author.query.filter_by(first_name=firstName).filter_by(last_name=lastName).all()
        if len(author) > 0:
            book_author = author[0]
        else:
            book_author = Author(first_name=firstName, last_name=lastName)
            with app.app_context():
                DB.session.add(book_author)
                DB.session.commit()
        with app.app_context():
            q_book = Book.query.filter_by(isbn=book_isbn).all()
        if len(q_book) > 0:
            b = q_book[0]
            b.best_seller_list = b.best_seller_list+", "+book_best_seller_list
        else:
            b = Book(isbn=book_isbn,
                     title=book_title,
                     summary=book_summary,
                     best_seller_date=book_best_seller_date,
                     best_seller_list=book_best_seller_list,
                     book_image=book_book_image,
                     amazon_link=book_amazon_link,
                     publisher=book_publisher)
            b.author = book_author
        with app.app_context():
            try:
                DB.session.add(b)
                DB.session.commit()
            except Exception:
                print("Handling weird book summary")
                DB.session.delete(b)
                DB.session.delete(book_author)
                DB.session.commit()
        list_of_book_objects.append(b)
    # Add book objects in a specific best seller list to the general
    # dictionary of book lists
    book_lists[category] = list_of_book_objects
total = 0
hits = 0
with app.app_context():
    for book in Book.query.all():
        hits += bookScrape(book)
        total += 1
print("succesfully loaded in "+str(total)+" books")
print("succesfully loaded in "+str(hits)+" authors")
