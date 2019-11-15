import requests
import json


def get_movies_from_tastedive(str):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction["q"] = str
    params_diction["limit"] = 5

    get_movies_resp = requests.get(baseurl, params=params_diction)
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(get_movies_resp.url)  # Paste the result into the browser to check it out...
    x = get_movies_resp.json()
    level_two = x["Similar"]["Info"]
    #print(json.dumps(x, indent=4, sort_keys=True))
    for item in level_two:
        return item['Name']


# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")
