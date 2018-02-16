birthdays = {'Josh':'Jan 1st', 'Emily':'March 6th', 'Winry':'Dec 1st'}

while True:
	print('Enter a name: (leave blank to stop)')
	name = input()

	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have birthday informatuon for ' + name)
		print('What is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('Birthady database updated.')
