import csv
import datetime
from dateutil import parser
from datetime import date, time, datetime
from random import randint


flight_list = []
# Takes in Lowest_Fares csv file and transforms it into a dictionary
with open('Lowest_Fares.csv') as f:
   reader = csv.reader(f)
   flight_list += list(reader)
   
headings = flight_list[0]
flight_list = flight_list[1:]

# Changing times to datetime
flight_time_change = [] 

for time in flight_list:
	time[2] = time[2][:-5]
	time[2] = parser.parse(str(time[2])[0:9], fuzzy=True)
	flight_time_change.append(time)


# Gathering user inputs
user_location = raw_input("Enter your starting location (ex. SFO, LAX, SEA) : ").upper()
user_s_time = raw_input("Enter your starting time (ex. 1/12/1999): ")
user_e_time = raw_input("Enter your ending time (ex. 1/20/1999): ")


#Checking if flights are starting from the correct location
def correct_location(start , flight_list):
	location_flights = []

	for flight in flight_list:	
		if start == flight[0]:
			location_flights.append(flight)
		else:
			pass
	return location_flights

#Checking if flights are starting at the correct time
def correct_time(start_time , location_flights):
	matching_flights = []
	s_time = parser.parse(start_time, fuzzy=True)

	for flight in location_flights:
		if s_time == flight[2]:
			matching_flights.append(flight)
		else:
			pass 
	return matching_flights

# print(matching_flights)

# Checking for return flights
def return_flights(end_time , m_flights, flight_list):
	able_return_flights = []
	index = randint(0 , len(m_flights))
	flight = m_flights[index-1]
	possbile_return_flights = correct_time(end_time , correct_location(flight[1] , flight_list))
	for p in possbile_return_flights:
		if p[1] == flight[0]:
			able_return_flights.append(p)
		else:
			pass
	return flight + able_return_flights

#print((correct_time(user_e_time , (correct_location(user_location , flight_list)))))

# Function that checks if a return flight exists:
#	for flight in matching_flights:
#		if flight[1] == returnf in flight_time_change:



def flight_finder(flight_list):
	random_list = return_flights(user_e_time , (correct_time(user_s_time , (correct_location(user_location , flight_list)))), flight_list)
	if len(random_list) == 4:
		flight_finder(flight_list)
	else:
		index2 = randint(5 , len(random_list) - 1)
		flight_choice = (random_list[0:4] , random_list[index2])
	return flight_choice

def formatting (flight_tuple):
	price = float(flight_tuple[0][3]) + float(flight_tuple[1][3])
	print("Origin: " + flight_tuple[0][0])
	print("Destination: " + flight_tuple[0][1])
	print("Total Cost: " + str(price))
	print("Starting Date: " + flight_tuple[0][2].isoformat())
	print("Ending Date:" + flight_tuple[1][2].isoformat())

formatting(flight_finder(flight_time_change))