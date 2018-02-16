#!python3
"""Use 3.x only keyword-only args"""

import sys

def print3(*args, **kwargs):
	sep = kwargs.pop('sep',' ')
	end = kwargs.pop('end', '\n')
	file = kwargs.pop('file', sys.stdout)

	if kwargs: 
		raise TypeError('extra keywords:{}'.format(kwargs))

	output = ''
	first = True

	for arg in args: 
		output += ('' if first else sep) + str(arg)
		first = False

	file.write(output + end)