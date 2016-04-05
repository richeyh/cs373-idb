test:
	coverage3 run --branch test.py
	coverage3 report -m

start: 
	python3 manage.py DB init
	python3 manage.py DB upgrade
	python3 manage.py DB migrate

