import requests

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"

headers = {
    "X-RapidAPI-Host": "coronavirus-monitor.p.rapidapi.com",
    "X-RapidAPI-Key": "927cd44cc4msh043741a9bfd6f2bp197515jsn66d951ec2b53"
}

response = requests.request("GET", url, headers=headers)

j = response.json()
for key, value in j["countries_stat"][0].items():
    print(key, value, sep="#########")
