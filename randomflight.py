import csv
from dateutil import parser


flight_list = []
# Takes in Lowest_Fares csv file and transforms it into a dictionary
with open('Lowest_Fares.csv') as f:
   reader = csv.reader(f)
   flight_list += list(reader)
   
headings = flight_list[0]
flight_list = flight_list[1:]

'''flight_time_change = [] 
for time in flight_list:
	time[2] = parser.parse(time[2], fuzzy=True)
	flight_time_change += time
'''


user_location = raw_input("Enter your starting location (ex. SFO, LAX, SEA) : ").upper()
user_s_time = raw_input("Enter your starting time (ex. 1/12/1999): ")
user_e_time = raw_input("Enter your ending time (ex. 1/20/1999): ")
# Flights starting at the correct location
location_flights = []

for flight in flight_list:	
	if user_location == flight[0]:
		location_flights += flight
	else:
		pass


print(location_flights)  



# for dictionary in flights:
  # dictionary["FlightDate"] = parser.parse(dictionary["FlightDate"], fuzzy=True)


