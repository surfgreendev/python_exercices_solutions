from github_api_consumer import GithubApiConsumer

if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    # url = "https://github.com/dfjlsafjdsa"
    github_api = GithubApiConsumer(url)
    github_api.query_github()
    # github_api.describe_response()
    # github_api.write_user_info_to_csv()
    github_api.find_highest_amount_of_open_issues()
