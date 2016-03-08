from extensions import DB

class Author(DB.model):
	#need to add fields below


class Book(DB.model):
	#need to add fields below

class Publisher(DB.model):
	#need to add fields below


class TeamMember(DB.model):
	id = DB.Column(DB.Integer, primary_key=True)
	image_url = DB.Column(DB.String(150))
	name = DB.Column(DB.String(150))
	bio = DB.Column(DB.Text())
	resp = DB.Column(DB.String(150))
	issues = DB.Column(DB.Integer)
	commits = DB.Column(DB.Integer)
	tests = DB.Column(DB.Integer)