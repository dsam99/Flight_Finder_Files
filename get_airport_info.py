import pickle

# loads the airport data into the program
with open('airports.pickle', 'rb') as f:
	airports = pickle.load(f)

with open('regions.pickle', 'rb') as f:
	regions = pickle.load(f)


def get_airport(iata_code):
	'''Finds airport by IATA code.'''
	return next((airport for airport in airports if airport['iata_code'] == iata_code), None)

def get_region(airport):
	'''Returns the region from an airport dictionary.'''
	if 'iso_region' in airport.keys():
		return next((region for region in regions if region['code'] == airport['iso_region']), None)