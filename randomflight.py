import csv
import datetime
from dateutil import parser
from datetime import date, time, datetime


flight_list = []
# Takes in Lowest_Fares csv file and transforms it into a dictionary
with open('Lowest_Fares.csv') as f:
   reader = csv.reader(f)
   flight_list += list(reader)
   
headings = flight_list[0]
flight_list = flight_list[1:]
print(flight_list)

# Changing times to datetime
flight_time_change = [] 

for time in flight_list:
	time[2] = time[2][:-5]
	time[2] = parser.parse(str(time[2])[0:9], fuzzy=True)
	flight_time_change.append(time)

print(flight_time_change)

# Gathering user inputs
user_location = raw_input("Enter your starting location (ex. SFO, LAX, SEA) : ").upper()
user_s_time = raw_input("Enter your starting time (ex. 1/12/1999): ")
user_e_time = raw_input("Enter your ending time (ex. 1/20/1999): ")


#Checking if flights are starting from the correct location
location_flights = []

for flight in flight_list:	
	if user_location == flight[0]:
		location_flights.append(flight)
	else:
		pass

#Checking if flights are starting at the correct time
matching_flights = []
s_time = parser.parse(user_s_time, fuzzy=True)

for flight in location_flights:
	if s_time == flight[2]:
		matching_flights.append(flight)
	else:
		pass 

#print(matching_flights)

#Checking for return flights
matching_return_flights = []
e_time = parser.parse(user_e_time, fuzzy=True)
destinations = []

for flight in matching_flights:
	destinations.append(flight[1])




