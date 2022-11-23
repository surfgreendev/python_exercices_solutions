"""
Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for logging
in again.
"""

# 1. Create list with 5 usernames called user_names
user_names = ["Carl", "Martin", "Ulrich", "Toby", "Christian", "Admin"]
# 2. For ... In ... Loop => print(f"xyz {name}")
for user in user_names:
    # 2a. If name == "admin": ==> print("... special greeting")
    if user.lower() == "admin":
        print("Hello Admin, would you like to see a status report?")
    # 2b. else print(hello {name}, thank you for ...)
    else:
        print(f"Hello {user}, thank you for logging in.")


"""
No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
"""

# user_names = []

# 1. If not list ==> We need to find some users
if not user_names:
    print("We need to find some users!")
else:
    user_names.clear()
    # for idx in range(0, len(user_names)):
    #   user_names[idx] = ""
    #   user_names.pop(idx)
    #   del user_names[idx]
# 2. Iterate thorugh list and use pop() ==> print(name your' logged out)
print("List", user_names)

"""
OPTIONAL:
Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.

"""

# 1. current_users = [......]
current_users = ["Carl", "Martin", "Ulrich", "Toby", "Christian", "Admin"]
# 2. new_users = [.....]
new_users = ["Carl", "Martin", "Frank", "Alexey", "Franz", "Susanne"]
# 3. for user in new_users => if user in current_users ==> print "enter a new username"
for new_user in new_users:
    if new_user in current_users:
        print("Enter a new username")
    else:
        print("User name is available")
# 3a. else print "username is available"

# HINT: use .lower() on names
