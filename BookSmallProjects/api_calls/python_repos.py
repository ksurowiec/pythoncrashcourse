import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print(response.status_code, response.elapsed)

response_dict = response.json()
# print(f"Total number of repositories: {response_dict['total_count']}")
#
# # Explore the information about the repositories
# repo_items = response_dict['items']
# print(f"Repositories returned: {len(repo_items)}")
#
# # Examine the first repository
# repo_item = repo_items[0]
# print("\nSelected information about first repository:")
# print("Name: ", repo_item['name'])
# print(f"Owner: {repo_item['owner']['login']}")
#

print(response_dict)
print(type(response_dict))