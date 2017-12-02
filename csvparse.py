import csv
from dateutil import parser

flight_list = []
with open('Lowest_Fares.csv') as f:
   reader = csv.reader(f)
   flight_list += list(reader)
   
headings = flight_list[0]
flight_list = flight_list[1:]


flights = [ dict(zip(headings, row)) for row in flight_list ]

for dictionary in flights:
   dictionary["FlightDate"] = parser.parse(dictionary["FlightDate"], fuzzy=True)

print(flights[0:4])