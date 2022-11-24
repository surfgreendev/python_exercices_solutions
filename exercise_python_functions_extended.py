"""
T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


def make_shirt(size, text):
    print(f"Size: {size}, Message to print: {text}")


make_shirt("XL", "Hello World")
make_shirt(size="XL", text="Hello World with keyword argument")
make_shirt(text="Hello World with keyword argument", size="XL")


"""
Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""


def make_shirt_extended(size="L", text="I love Python"):
    print(f"Size: {size}, Message to print: {text}")


make_shirt_extended()
make_shirt_extended("M", "Another Message")


"""
Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""


def describe_city(city, country="France"):
    print(f"{city.title()} is in {country.title()}")


describe_city("Berlin", "Deutschland")
describe_city(city="Paris")
describe_city("Lissabon", "Portugal")
