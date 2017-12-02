import csv
from dateutil import parser

def get_rows(filename, date_field=None):
	with open(filename) as f:
		reader = csv.reader(f)
		csv_list = list(reader)
	   
	# get headings
	headings = csv_list[0]
	# remove headings from other data
	csv_list = csv_list[1:]

	# turn the each row into a dictionary
	rows = [ dict(zip(headings, row)) for row in csv_list ]

	if date_field:
		for dictionary in rows:
			dictionary[date_field] = parser.parse(dictionary[date_field], fuzzy=True)

	return rows