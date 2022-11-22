"""
Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
"""

foods = ("burger", "schnitzel", "leberkaes semmel", "suppe")

for food in foods:
    print(f"Food is: {food.title()}")


# foods(0) = "pizza"
