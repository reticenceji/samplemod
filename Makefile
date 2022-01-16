init:
	pip install -r requirements.txt

doc:
	pdoc --html src -o doc/

test: src
	pytest src/*
	pytest test