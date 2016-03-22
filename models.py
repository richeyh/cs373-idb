from extensions import DB


class Author(DB.Model):
    """
    id: primary key in the database
    first_name: the first name of the author
    last_name: the last name of the author
    book_count: # of books in the database by the author
    best_seller_date: last date of best seller by author
    Books: all books the author wrote
    """
    __tablename__ = "author"
    id = DB.Column(DB.Integer, primary_key=True)
    first_name = DB.Column(DB.String(150))
    last_name = DB.Column(DB.String(150))
    book_count = DB.Column(DB.Integer)
    best_seller_date = DB.Column(DB.date())
    Books = DB.relationship("Book")


class Book(DB.Model):
    """
    id: primary key for the book object
    isbn: the isbn # for the book
    title: title of the book
    summary: summary of the book by new york times
    price: prise of the book
    best_seller_date: date it made best seller best_seller_list
    best_seller_list: the list or category it made the list for
    book_image: url to the image for the book
    author_id: primary key to the books author for linking
    publisher_id: primary key to the books publisher for linking
    """
    __tablename__ = "book "
    id = DB.Column(DB.Integer, primary_key=True)
    isbn = DB.Column(DB.String(150))
    title = DB.Column(DB.String(150))
    summary = DB.Column(DB.Text())
    price = DB.Column(DB.String(150))
    best_seller_date = DB.Column(DB.date())
    best_seller_list = DB.Column(DB.String(150))
    book_image = DB.Column(DB.String(150))
    author_id = DB.Column(DB.Integer, DB.ForeignKey(Author))
    publisher = DB.Column(DB.String(150))
    author = DB.relationship(Author)


class TeamMember(DB.Model):
    """
    id: primary key for TeamMember
    image_url: url of image for picture
    name: name of user
    bio: biography for user
    resp: responsibilities
    issue: # of issues created
    commits: # of commits
    tests: # of tests written
    """
    id = DB.Column(DB.Integer, primary_key=True)
    image_url = DB.Column(DB.String(150))
    name = DB.Column(DB.String(150))
    bio = DB.Column(DB.Text())
    resp = DB.Column(DB.String(150))
    issues = DB.Column(DB.Integer)
    commits = DB.Column(DB.Integer)
    tests = DB.Column(DB.Integer)
