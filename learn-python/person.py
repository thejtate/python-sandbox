# File person.py (final)
"""
Record and process information about people. 
Run this file directly to test its classes. 
"""

from classtools import AttrDisplay

class Person(AttrDisplay): 
	"""
	Create and process persons recors
	"""
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))

class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self, name, 'Manager', pay)
	def giveRaise(self, percent, bonus=0.10):
		Person.giveRaise(self, percent + bonus)

class Department:
	def __init__(self, *args):
		self.members = list(args)
	def addMember(self, person):
		self.members.append(person)
	def giveRaises(self, percent):
		for person in self.members:
			person.giveRaises(percent)
	def showAll(self):
		for person in self.members:
			print(person)

if __name__ == '__main__':
	#self test
	josh = Person('Josh')
	emily = Person('Emily Tate', job='dev', pay=100000) 
	print(josh)
	print(emily)
	print(josh.lastName(), emily.lastName()) 
	emily.giveRaise(.10)
	print(emily)
	winry = Manager('Winry Tate', 50000) 
	winry.giveRaise(.10)
	print(winry.lastName())
	print(winry)