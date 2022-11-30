from utilities.menu import Menu
from utilities.utilities import Chair, Table


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.chairs = []
        self.tables = []
        self.menu = None

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

    def add_chair(self, color, material):
        chair = Chair(color, material)
        self.chairs.append(chair)

    def show_chairs(self):
        for chair in self.chairs:
            print("fdksjalkf " + chair)

    def add_table(self, color, size):
        table = Table(color, size)
        self.tables.append(table)

    def tell_me_about_your_tables(self):
        for table in self.tables:
            table.show_attributes(self)

    def add_menu(param, param1):
        self.menu = Menu(param, param1)


restaurant_carl = Restaurant("name", "deutsch")
restaurant_carl.add_chair("green", "wood")
restaurant_carl.add_chair("red", "plastic")
...
