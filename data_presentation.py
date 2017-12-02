import randomflight.py;

# Outputs all information about the chosen flights
def data_presentation (flight_tuple):
	price = float(flight_tuple[0][3]) + float(flight_tuple[1][3])
	print("Origin: " + flight_tuple[0][0])
	print("Destination: " + flight_tuple[0][1])
	print("Total Cost: " + str(price))
	print("Starting Date: " + flight_tuple[0][2].isoformat())
	print("Ending Date:" + flight_tuple[1][2].isoformat())

formatting(randomflight.flight_finder(flight_time_change))