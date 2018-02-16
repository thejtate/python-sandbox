dogNames = []
while True: 
	print('Enter the name of your dogs #' + str(len(dogNames) + 1) + ' (Or enter \'Stop\' to stop.):')
	name = input()
	if name == 'stop':
		break
	dogNames = dogNames + [name] # list concatenation

print('The dog names are:')

for name in dogNames:
	print(' ' + name)