"""
Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
"""
my_friends = ["Julian", "David", "Alexej", "Andreas"]
print(my_friends[0])
print(my_friends[1])
print(my_friends[2])
print(my_friends[3])

"""
Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the
person’s name.
"""
try:
    welcome_message = f"Hey {my_friends[5]}, how are you today"
except IndexError as e:
    welcome_message = f"Hey {my_friends[0]}, how are you today"

print(welcome_message)


"""
Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""
transportation = ["honda", "mazda", "mercedes"]

message = f"I would like to own a {transportation[0].title()} motorcycle."
print(message)
