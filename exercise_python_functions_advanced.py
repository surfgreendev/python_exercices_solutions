"""
City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned
"""


def city_country(city, country):
    """
    Manage city and countries to a string
    """
    return f"{city.title()}, {country.title()}"


item = city_country("Schweinfurt", "Germany")
print(item)
"""
Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.

"""

dict = {"key": "value", "key2": "value2"}


def make_album(artist_name, album_title):
    """
    Create artist/album title dictionary

    Args:
        artist_name (String): It's a name of an artist.
        album_title (_type_): _description_

    Returns:
        dict: Lorem ipsum
    """
    return {"artist_name": artist_name.title(), "album_title": album_title.title()}


album = make_album("Notorious BIG", "Some album title")
print(album)
