"""
Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""


class Car:
    def __init__():
        pass


class Table:
    pass


class Chair:
    pass


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """
        Describes the current restaurant.

        Returns:
            String: A description of a restaurant's cuisine.
        """
        return f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}"

    def open_restaurant(self):
        """
        Opens the restaurant
        """
        print(f"The restaurant {self.restaurant_name.title()} is open")


my_dict = [
    {"name": "Pizza place", "cuisine_type": "italien"},
    {"name": "Gasthof", "cuisine_type": "german"},
]


my_restaurant = Restaurant("Pizza place", "Italien")


print(my_restaurant)
print(my_restaurant.describe_restaurant())
my_restaurant.open_restaurant()
