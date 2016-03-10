from extensions import DB

class Author(DB.model):
	#need to add fields below
	__tablename__="author"
	name = DB.Column(DB.String(150))

class Publisher(DB.model):
	#need to add fields below
	__tablename__="publisher"
	name = DB.Column(DB.String(150))

class Book(DB.model):
	#need to add fields below
	__tablename__="book "
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