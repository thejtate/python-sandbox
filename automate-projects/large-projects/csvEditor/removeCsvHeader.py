#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory. 
for csvFile in os.listdir('.'):
	if not csvFile.endswith('.csv'):
		continue # skip non-csv files

	print('Removing header from '+csvFile+'...')

	# Read the CSV file in (skipping first row).
	csvRows = []
	csvFileObj = open(csvFile)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue # skip the first line
		csvRows.append(row)
	csvFileObj.close()

	# Write out the CSV file.
	csvFileObj = open(os.path.join('headerRemoved',csvFile), 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()