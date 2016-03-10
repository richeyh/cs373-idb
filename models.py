from extensions import DB

class Author(DB.model):
	#need to add fields below
	__tablename__="author"
	id = DB.Column(DB.Integer, primary_key=True)
	first_name = DB.Column(DB.String(150))
	last_name = DB.Column(DB.String(150))
	book_count = DB.Column(DB.Integer)
	best_seller_date = DB.Column(DB.date())
	Books = DB.relationship("Book")

class Publisher(DB.model):
	#need to add fields below
	__tablename__="publisher"
	id = DB.Column(DB.Integer, primary_key=True)
	name = DB.Column(DB.String(150))
	location = DB.Column(DB.String(150))
	book_count = DB.Column(DB.Integer)
	Books = DB.relationship("Book")
	metadata = DB.Column(DB.String(256)) #categories of books they are known for

class Book(DB.model):
	#need to add fields below
	__tablename__="book "
	id = DB.Column(DB.Integer, primary_key=True)
	isbn = DB.Column(DB.String(150))
	title = DB.Column(DB.String(150))
	summary = DB.Column(DB.Text())
	price = DB.Column(DB.String(150))
	best_seller_date = DB.Column(DB.date())
	best_seller_list = DB.Column(DB.String(150))
	book_image = DB.Column(DB.String(150))
	author_id = DB.Column(DB.Integer, DB.ForeignKey(Author))
	publisher_id = DB.Column(DB.Integer, DB.ForeignKey(Publisher))


class TeamMember(DB.model):
	id = DB.Column(DB.Integer, primary_key=True)
	image_url = DB.Column(DB.String(150))
	name = DB.Column(DB.String(150))
	bio = DB.Column(DB.Text())
	resp = DB.Column(DB.String(150))
	issues = DB.Column(DB.Integer)
	commits = DB.Column(DB.Integer)
	tests = DB.Column(DB.Integer)