myPets = ['Winry','Tessie','Maggie']
print('Enter a pet name:')
name = input()

if name is myPets:
	print('I do not have a pet named ' + name)
else:
	print(name + ' is my pet.')