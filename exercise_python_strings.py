"""
Personal Message: Store a person’s name in a variable, and print a message
to that person. Your message should be simple, such as, "Hello Eric,
would you like to learn some Python today?"
"""

"""

"""

" "

my_name = "Eric"
welcome_message = "Hello " + my_name + ", would you like..."
print(welcome_message)

f_welcome_message = f"Hello {my_name} would you like ..."
print(f_welcome_message)

"""
Store a person’s name in a variable, and then print that person’s
name in lowercase, uppercase, and titlecase.
"""
print(welcome_message.lower())
print(welcome_message.upper())
print(welcome_message.title())


def make_lower():
    return


"""
Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
"""
quote = "Albert Einstein said, 'A person who never ...'"
quote_2 = 'Albert Einstein said, "A person who never ..."'
print(quote)
print(quote_2)


"""
Famous Quote 2: Repeat Exercise above, but this time store the famous person’s
name in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message.
"""
first_name = "Albert"
last_name = "Einstein"
famous_person = first_name + " " + last_name

message = famous_person + " once said, 'A person who never ...'"
print(message)

"""
Stripping Names: Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
"""
my_name_2 = "\t\tCarl Bednorz   \n\n"
print(my_name_2)

print(my_name_2.lstrip())
print(my_name_2.rstrip())
print(my_name_2.strip())
print(my_name_2)
# Comment
my_name_2 = my_name_2.strip()

print(my_name_2)


class MyObject:
    """
    This class ...
    """

    def __init__(self):
        """
        _summary_
        """
        pass
