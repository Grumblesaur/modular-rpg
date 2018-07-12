all: clean check

clean:
	rm attr/__pycache__ opt/__pycache__ __pycache__ -rf

check:
	python3 Rules.py

