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
with open("test.csv") as csv_file:
    data = CsvWriter(csv_file, "rb")

my_list = [
    1,
    2,
    3223,
    432,
    432,
    32,
    341,
    432,
    4312,
    4324,
    3214,
    432,
    432,
    432,
    432,
    4321,
    45,
    6,
    54,
    767453,
]
