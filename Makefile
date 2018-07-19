all: clean check

guide:
	cat status.txt encumbrance.txt combat.txt skills.txt spells.txt > guide.txt

clean:
	rm attr/__pycache__ opt/__pycache__ __pycache__ -rf

check:
	python3 Rules.py

