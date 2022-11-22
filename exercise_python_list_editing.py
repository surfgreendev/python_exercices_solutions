"""
Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

guests = ["Andrew", "Sebastian", "Frank", "Hillary", "Martin"]
print(guests)
invitation_message = f"Hi {guests[0]}, you're invited for dinner."
print(invitation_message)

"""
Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

Start with your program from above (Guest List). Add a print statement at the
end of your program stating the name of the guest who can’t make it.

Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.

Print a second set of invitation messages, one for each person who is still
in your list.
"""


print(f"{guests[1]}, cannot make it to your party.")
# Replace Sebastian with Julian
new_guest = "Julian"
# del guests[1]
guests.remove("Sebastian")
guests.insert(1, new_guest)
print(guests)


"""
More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from above. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

guests.insert(0, "Arnold")

middle_pos = int(len(guests) / 2)
print(middle_pos)
guests.insert(middle_pos, "Peter")
print(guests)
guests.append("Daniel")
print(guests)

"""
Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.


• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.


"""

print(f"Cannot invite {guests.pop()} you. Sorry!")

# print(f"Cannot invite {guests[-1]} you. Sorry!")

# del guests[-1]

print(f"Cannot invite {guests.pop()} you. Sorry!")
print(f"Cannot invite {guests.pop()} you. Sorry!")
print(f"Cannot invite {guests.pop()} you. Sorry!")
print(f"Cannot invite {guests.pop()} you. Sorry!")
print(f"Cannot invite {guests.pop()} you. Sorry!")

print(guests)

"""
• Print a message to each of the two people still on your list, letting them
know they’re still invited.


• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.

"""
del guests[-1]
del guests[-1]

my_num = 4555

print("Empty guest list %s - %d" % (guests, my_num))


my_long_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
    12,
    1,
    2,
    321,
    3,
    321,
    321,
    3213,
    21,
    5,
    43,
    765,
    765,
    8,
    768,
    769,
    87978,
    12,
]
