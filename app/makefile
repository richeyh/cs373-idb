test:
	coverage3 run --branch test.py
	coverage3 report -m

start: 
	python3 manage.py db init
	python3 manage.py db upgrade
	python3 manage.py db migrate
	python3 fetch_data.py

