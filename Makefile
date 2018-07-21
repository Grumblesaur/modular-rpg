all: guide

guide:
	cat\
		character-creation.txt\
		status.txt\
		encumbrance.txt\
		combat.txt\
		skills.txt\
		spells.txt\
	> guide.txt

clean:
	rm guide.txt

