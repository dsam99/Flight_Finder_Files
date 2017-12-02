import wikipedia
from get_airport_info import get_airport


'''Returns the content of a corresponding Wikipedia page, 
given the iata code of the airport.'''
def get_summary(iata_code):
    page = get_page(iata_code)
    return page.content


'''Returns the corresponding Wikipedia page according to the 
municipality of the airport. If an exception is thrown, then
the first page option is returned.'''
def get_page(iata_code):
    airport = get_airport(iata_code)
    if airport:
        try:
            page = wikipedia.page(airport['municipality'])
            return page
        except wikipedia.exceptions.DisambiguationError as e:
            page = wikipedia.page(e.options[0])
            return page


    else:
        return None

'''Returns the first image URL of the Wikipedia page of the
city that corresponds to the iata code.'''
def get_img_url(iata_code):
    page = get_page(iata_code)
    return (page.images[0])
