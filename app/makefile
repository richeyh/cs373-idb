test:
	coverage3 run --branch test.py
	coverage3 report -m

init:
	python3 manage.py db init
	python3 manage.py db upgrade
	python3 manage.py db migrate
	python3 manage.py db upgrade

upgrade:
	python3 manage.py db upgrade

migrate:
	python3 manage.py db migrate

fetch:
	python3 fetch_data.py

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__
