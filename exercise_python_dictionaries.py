"""
Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""

# person = {}
person_1 = {
    "first_name": "Carl",
    "last_name": "Bednorz",
    "age": 40,
    "city": "Schweinfurt",
}

print(person_1["first_name"])
pass
# print(dict[key])


"""
Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""
person_fav_numbers = {}
person_fav_numbers["michael"] = 34
person_fav_numbers["sebastian"] = 55
person_fav_numbers["frank"] = 34
print(person_fav_numbers)

fav_num = person_fav_numbers["michael"]
print("Michael's fav number is " + str(fav_num))
# person_fav_numbers = {"sebastian": 34}
# person_fav_numbers = {}
# person_fav_numbers["sebastian"] = 34


"""
Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.

• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""

glossary = {
    "lists": "Lorem ipsum doloret ...",
    "for-loops": "For Loops are awesome",
    "if-else": "Conditional queries with if else, true and false",
}

print(glossary)
print("Lists: " + glossary["lists"])

glossary = {
    "lists": "Lorem ipsum doloret ...",
    "for-loops": "For Loops are awesome",
    "if-else": "Conditional queries with if else, true and false",
}
