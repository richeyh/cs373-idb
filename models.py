from extensions import DB


class Author(DB.Model):
    """
    An author of a book.

    Attributes:
        id                  primary key in the database
        first_name          the first name of the author
        last_name           the last name of the author
        book_count          # of books in the database by the author
        best_seller_date    last date of best seller by author
        Books               all books the author wrote
        Link                Link to the authors facebook page
    """
    __tablename__ = "author"
    id = DB.Column(DB.Integer, primary_key=True)
    first_name = DB.Column(DB.String(150))
    last_name = DB.Column(DB.String(150))
    book_count = DB.Column(DB.Integer)
    best_seller_date = DB.Column(DB.Date())
    Books = DB.relationship("Book")
    link = DB.Column(DB.String(256))


class Book(DB.Model):
    """
    A Book object to hold information.

    Attributes:
        id                  primary key for the book object
        isbn                the isbn # for the book
        title               title of the book
        summary             summary of the book by new york times
        best_seller_date    date it made best seller best_seller_list
        best_seller_list    the list or category it made the list for
        book_image          url to the image for the book
        author_id           primary key to the books author for linking
        publisher           publisher who published the book
        author              author who wrote the book
    """
    __tablename__ = "book"
    id = DB.Column(DB.Integer, primary_key=True)
    isbn = DB.Column(DB.String(150))
    title = DB.Column(DB.String(150))
    summary = DB.Column(DB.Text())
    best_seller_date = DB.Column(DB.Date())
    best_seller_list = DB.Column(DB.String(150))
    book_image = DB.Column(DB.String(150))
    author_id = DB.Column(DB.Integer, DB.ForeignKey(Author.id))
    publisher = DB.Column(DB.String(150))
    author = DB.relationship(Author)


class TeamMember(DB.Model):
    """
    A TeamMember object for use latter to track changing statistics.

    Attributes:
        id          primary key for TeamMember
        image_url   url of image for picture
        name        name of user
        bio         biography for user
        resp        responsibilities
        issue       # of issues created
        commits     # of commits
        tests       # of tests written
    """
    id = DB.Column(DB.Integer, primary_key=True)
    image_url = DB.Column(DB.String(150))
    name = DB.Column(DB.String(150))
    bio = DB.Column(DB.Text())
    resp = DB.Column(DB.String(150))
    issues = DB.Column(DB.Integer)
    commits = DB.Column(DB.Integer)
    tests = DB.Column(DB.Integer)
