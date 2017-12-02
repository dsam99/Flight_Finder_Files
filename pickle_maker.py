import csv
import pickle
import datetime
from dateutil import parser
from datetime import date, time, datetime
from random import randint

flight_list = []
# Takes in Lowest_Fares csv file and transforms it into a dictionary
with open('Lowest_Fares.csv') as f:
   reader = csv.reader(f)
   flight_list += list(reader)
   
flight_list = flight_list[1:]

# Changing times to datetime
flight_time_change = [] 

for time in flight_list:
	time[2] = time[2][:-5]
	time[2] = parser.parse(str(time[2])[0:9], fuzzy=True)
	flight_time_change.append(time)

with open('flights.pickle', 'wb') as f:
	pickle.dump(flight_time_change, f)
