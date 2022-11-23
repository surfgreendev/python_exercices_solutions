"""
Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
"""

# pets = []
# pet_1 = {"color", "name", ...}

# = pets [pet_1, ... , n]

# for in

pets = []
pet_1 = {"name": "Jack", "color": "black", "type": "cat"}
pet_2 = {"name": "Brutus", "color": "white", "type": "dog"}
pet_3 = {"name": "Franck", "color": "green", "type": "frog"}

pets.append(pet_1)
pets.append(pet_2)
pets.append(pet_3)

for pet in pets:
    print("My pet is called " + pet["name"].title() + "\n")
    for k, v in pet.items():
        print("Detail Info - " + k + ": " + v)

"""
Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
"""
favorite_places = {
    "eric": ["bear mountain", "death valley", "tierra del fuego"],
    "erin": ["hawaii", "iceland"],
    "willie": ["mt. verstovia", "the playground", "new hampshire"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")

"""
Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""
cities = {
    "santiago": {
        "country": "chile",
        "population": 6_310_000,
        "nearby mountains": "andes",
    },
    "talkeetna": {
        "country": "united states",
        "population": 876,
        "nearby mountains": "alaska range",
    },
    "kathmandu": {
        "country": "nepal",
        "population": 975_453,
        "nearby mountains": "himilaya",
    },
}

for city, city_info in cities.items():
    country = city_info["country"].title()
    population = city_info["population"]
    mountains = city_info["nearby mountains"].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mounats are nearby.")
