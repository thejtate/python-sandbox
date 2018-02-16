def bacon():
	global eggs 
	eggs = '500'

def spam(): 
	global eggs
	eggs = 'spam'


def ham():
	print(eggs)

eggs = 42
spam()
bacon()
print(eggs)