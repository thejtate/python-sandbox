# file makedb.py
from person import Person, Manager

josh = Person('Josh Tate')
emily = Person('Emily Tate', job='My wife', pay=50000)
winry = Manager('Winry Tate', 100000)

import shelve
db = shelve.open('persondb')
for obj in (josh, emily, winry):
	db[obj.name] = obj
db.close()