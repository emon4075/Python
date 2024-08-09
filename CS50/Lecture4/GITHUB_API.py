import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
response = requests.get(url).json()

try:
    for i in range(50):
        try:
            name = response["items"][i]["name"]
            time_creation = response["items"][i]["created_at"]
            if response["items"][i]["license"]:
                License = response["items"][i]["license"]["name"]
            else:
                License = "No License"
            branch = response["items"][i]["default_branch"]
            github = response["items"][i]["html_url"]
            print("No:", i + 1)
            print("\tName:", name)
            print("\tCreated On:", time_creation)
            print("\tLicense:", License)
            print("\tBranch:", branch)
            print("\tRepo:", github)
        except KeyError as e:
            print(f"KeyError: {e} in item {i}")
            continue
        except IndexError:
            print(f"Only {i} items found in the response.")
            break
except Exception as e:
    print("An error occurred:", e)
