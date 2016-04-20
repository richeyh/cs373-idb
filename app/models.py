"""
The module for all SQLAlchemy database models
"""
from extensions import DB
import re

TAG_RE = re.compile(r'<[^>]+>')


"""
An Author Model
"""


class Author(DB.Model):
    """
    An author of a book.

    Attributes:
        id                  primary key in the database
        first_name          the first name of the author
        last_name           the last name of the author
        bio                 bio of the author
        book_count          # of books in the database by the author
        best_seller_date    last date of best seller by author
        Books               all books the author wrote
        link                link to the author's image
    """
    __tablename__ = "author"
    __searchable__ = ['first_name', 'last_name', 'bio', 'link']
    id = DB.Column(DB.Integer, primary_key=True)
    first_name = DB.Column(DB.String(150))
    last_name = DB.Column(DB.String(150))
    bio = DB.Column(DB.Text())
    book_count = DB.Column(DB.Integer)
    best_seller_date = DB.Column(DB.Date())
    Books = DB.relationship("Book")
    link = DB.Column(DB.String(256))

    def to_dict(self, query_instance=None):
        """
            Method to convert sqlalchmey object to python dict
            Stolen from https://www.prahladyeri.com/blog/2015/07/sqlalchemy-hack-convert-dict.html
        """
        if hasattr(self, '__table__'):
            return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
        else:
            cols = query_instance.column_descriptions
            return {cols[i]['name']: self[i] for i in range(len(cols))}

    def get_html(self, search_term):
        result_string = ""
        if "AND" in search_term:
            search_term = search_term.split("AND")
            search_term[0] = search_term[0].lower().strip()
            search_term[1] = search_term[1].lower().strip()
        elif "OR" in search_term:
            search_term = search_term.split("OR")
            search_term[0] = search_term[0].lower().strip()
            search_term[1] = search_term[1].lower().strip()
        else:
            search_term = search_term.lower()
            search_term = [search_term]
        attributes = {
            "id", "book_count", "best_seller_date", "Books", "link"}
        if hasattr(self, '__table__'):
            for c in self.__table__.columns:
                if(c.name in attributes):
                    attribute = str(getattr(self, c.name))
                else:
                    attribute = str(getattr(self, c.name)).lower()
                attribute = TAG_RE.sub('', attribute)
                rep_attribute = attribute
                for s in search_term:
                    rep_attribute = rep_attribute.replace(
                        s, '<b><i>' + s + '</i></b>')
                if(rep_attribute != attribute):
                    result_string += rep_attribute + " "
        return "<td>" + self.first_name + " " + self.last_name + "</td>" + "<td>" + result_string + "</td>"

    def get_link(self):
        return "/author/" + str(self.id)


"""
A Book Model
"""


class Book(DB.Model):
    """
    A Book object to hold information.

    Attributes:
        id                  primary key for the book object
        isbn                the isbn # for the book
        title               title of the book
        summary             summary of the book by new york times
        best_seller_date    date it made best seller best_seller_list
        best_seller_list    the lists or categorys it made the list for
        book_image          url to the image for the book
        amazon_link         url to the Amazon product page for the book
        author_id           primary key to the books author for linking
        publisher           publisher who published the book
        author              author who wrote the book
        description         the description of the book from Amazon
    """
    __tablename__ = "book"
    __searchable__ = ['isbn', 'title', 'summary',
                      'best_seller_list', 'book_image', 'amazon_link',
                      'publisher', 'description']
    id = DB.Column(DB.Integer, primary_key=True)
    isbn = DB.Column(DB.String(150))
    title = DB.Column(DB.String(150))
    summary = DB.Column(DB.Text())
    best_seller_date = DB.Column(DB.Date())
    best_seller_list = DB.Column(DB.Text())
    book_image = DB.Column(DB.String(150))
    amazon_link = DB.Column(DB.String(256))
    author_id = DB.Column(DB.Integer, DB.ForeignKey(Author.id))
    publisher = DB.Column(DB.String(150))
    author = DB.relationship(Author)
    description = DB.Column(DB.Text())

    def to_dict(self, query_instance=None):
        """
            Method to convert sqlalchmey object to python dict
            Stolen from https://www.prahladyeri.com/blog/2015/07/sqlalchemy-hack-convert-dict.html
        """
        if hasattr(self, '__table__'):
            return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
        else:
            cols = query_instance.column_descriptions
            return {cols[i]['name']: self[i] for i in range(len(cols))}

    def get_html(self, search_term):
        result_string = ""
        if "AND" in search_term:
            search_term = search_term.split("AND")
            search_term[0] = search_term[0].lower().strip()
            search_term[1] = search_term[1].lower().strip()
        elif "OR" in search_term:
            search_term = search_term.split("OR")
            search_term[0] = search_term[0].lower().strip()
            search_term[1] = search_term[1].lower().strip()
        else:
            search_term = search_term.lower()
            search_term = [search_term]
        attributes = {"best_seller_date", "book_image",
                      "amazon_link", "author_id", "author"}
        if hasattr(self, '__table__'):
            for c in self.__table__.columns:
                if(c.name in attributes):
                    attribute = str(getattr(self, c.name))
                else:
                    attribute = str(getattr(self, c.name)).lower()
                attribute = TAG_RE.sub('', attribute)
                rep_attribute = attribute
                for s in search_term:
                    rep_attribute = rep_attribute.replace(
                        s, '<b><i>' + s + '</i></b>')
                if (rep_attribute != attribute):
                    result_string += rep_attribute + " "
        return "<td>" + self.title + "</td>" + "<td>" + result_string + "</td>"

    def get_link(self):
        return "/book/" + str(self.id)

"""
A TeamMember model
"""


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
