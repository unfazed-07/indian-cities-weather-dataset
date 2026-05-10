import requests
indicators = "SE.ADT.LITR.ZS;SH.DYN.MORT;SH.XPD.CHEX.GD.ZS;EN.ATM.CO2E.PC;EG.ELC.ACCS.ZS;ER.LND.PTLD.ZS"


countries = requests.get(f"https://api.worldbank.org/v2/country/all/indicator/{indicators}",
                        params= {"format":"json", "date":"2022:2025", "per_page":300}).json()

countries = countries[1]

sa = [country["iso2Code"] for country in countries if country["region"]["value"]=="South Asia"]
print(sa)

# for nation in sa:
#     country = requests.get(f"https://api.worldbank.org/v2/country/nation/",
#                             params = {"format":"json", "date":"2022:2025"})