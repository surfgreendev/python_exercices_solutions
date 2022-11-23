"""
Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.

• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.

• Use a loop to print the name of each river included in the dictionary.

• Use a loop to print the name of each country included in the dictionary.
"""

# rivers = {}
# add key value pairs
rivers = {"main": "germany", "rhein": "germany", "nile": "egypt"}

for name, country in rivers.items():
    print(f"The river {name.title()} runs through {country.title()}")

for river in rivers:  # Alternative: key in rivers.keys()
    print(river.title())

for country in set(rivers.values()):
    print(country.title())
# print .items(), .keys(), .values()
