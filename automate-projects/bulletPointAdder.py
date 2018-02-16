#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

#Sepearte lines and add bullets
lines = text.split('. ')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i] # add start to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)