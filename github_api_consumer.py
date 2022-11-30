import csv
import pprint

import requests

pp = pprint.PrettyPrinter(indent=4)

"""
    try:
    response = requests.get(self.url, timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
    
"""


class GithubApiConsumer:
    """
    Manages querying the github api
    and doing some data analysis on
    the response data.
    """

    def __init__(self, url):
        """
        Initialising required data

        Args:
            url (string): The url to
        """
        self.url = url
        # Expecting a dictionary here
        self.github_response = {}

    def query_github(self):
        """
        Queries the github url and
        transforms the http json response
        to a dictionary.
        """
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            self.github_response = r.json()
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    def describe_response(self):
        """
        describing the response dict with
        a pretty printer.
        """
        pp.pprint(self.github_response)

    def write_user_info_to_csv(self):
        """
        Writing github repo user info to a csv
        """
        print("Start processing")
        file_name = "github_user_info.csv"
        items = self.github_response["items"][:10000]
        pp.pprint(items)
        with open(file_name, "w") as csvfile:
            for item in items:
                repo_name = item["name"]
                owner = item["owner"]
                owner_id = owner["id"]
                owner_login = owner["login"]
                owner_type = owner["type"]
                row = [repo_name, owner_id, owner_login, owner_type]
                spamwriter = csv.writer(csvfile, delimiter=",")
                print("Writing Row: " + str(row))
                spamwriter.writerow(row)

    def find_highest_amount_of_open_issues(self):
        print("Processiung")
        # items["open_issues_count"]
        repositories = []
        for item in self.github_response["items"]:
            repositories.append(
                {
                    "name": item["name"],
                    "url": item["html_url"],
                    "owner": item["owner"]["login"],
                    "issues_count": item["open_issues_count"],
                }
            )
            pp.pprint(repositories)
            sorted_list = sorted(
                repositories, key=lambda d: d["issues_count"], reverse=True
            )

            print("Sorted List:")

            pp.pprint(sorted_list)
