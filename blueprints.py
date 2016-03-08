from flask import Blueprint

blueprint = Blueprint('idb',__name__,template_folder='templates')


blueprint.add_url_rule('/',view_func=IndexView.as_view('Home'))
