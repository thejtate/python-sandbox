#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backToZip(folder):
	# Backup the entire contents of "folder" into a zip. 
	folder = os.path.abspath(folder) # make sure folder is absolute
	
	# Figure out the filename this code should use based on
	# what files already exist.
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename): 
			break
		number = number + 1

	#Create the zip file
	print('Creating %s...' % (filename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# Walk the entire folder tree and compress the files in each folder.
	for d, sd, f in os.walk(folder):
		print('Adding files in %s...' % (d))
		# Add the current folder to the Zip file
		backupZip.write(d)
		# Add all the files in this folder to the Zip file
		for filename in f:
			if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
				continue # don't backup the backup ZIP files
			backupZip.write(os.path.join(d, filename))
	backupZip.close()
	print('Done.')

backToZip('quizGenerator')