"""
Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

val = "val"
print(val == "val")  # True

val = "new val"
print(val != "val")  # True

val_1 = "value"
val_2 = "Value"
print(val_1 == val_2.lower())  # True

num_1 = 1
print(num_1 == 1)  # True
print(num_1 != 1)  # False

print(num_1 >= 2)  # False
print(num_1 < 2)  # True

check_list = ["bernie", "frank", "boris", "toby"]

user_to_check = "Bernie"

if user_to_check.lower() in check_list:
    print(f"{user_to_check.title()} is in the list")

user_to_check = "Peter"

if user_to_check.lower() not in check_list:
    print("He's not in the list")
