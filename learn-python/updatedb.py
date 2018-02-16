# File updatedb.py: update Person object on database
import shelve 
db = shelve.open('persondb')

for key in sorted(db):
	print(key, '\t=>', db[key])

winry = db['Winry Tate']
winry.giveRaise(.10)
db['Winry Tate'] = winry
db.close()