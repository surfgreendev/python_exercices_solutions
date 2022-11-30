import pprint

import requests

pp = pprint.PrettyPrinter(indent=4)

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)

print(r.status_code)
# print(r.content)

as_json = r.json()

# print(as_json)

# pp.pprint(as_json)


# explore keys
print(as_json.keys())

# 1st item --> keys --> .keys()
items = as_json["items"]

pp.pprint(items[0])
