	#! python 3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? 				 # area code - group 1
    (\s|-|\.)? 						 # separator - group 2
    (\d{3}) 						 # first 3 digits - group 3
    (\s|-|\.)						 # separator - group 4
    (\d{4}) 						 # last 4 digits - group 5
    (\s*(ext|x|ext.)				 # extension - group 6
    \s*								 # group 7
    (\d{2,5}))?   					 # group 8
    )''', re.VERBOSE)						

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+   # username - group 1
	@ 				    # @ symbol - group 2
	[a-zA-Z0-9.-]+      # domain name - group 3
	(\.[a-zA-Z]{2,4})   # dot-something - group 4
	)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

# Find matches in clipboard
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy results to the clipboard. 
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')