import requests
countries = requests.get("https://api.worldbank.org/v2/indicator", 
    params={"format": "json", "per_page": 1000}).json()


for idd in countries[1]:
    print(idd["id"] ,"->", idd["name"] , end = "\n")