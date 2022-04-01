import requests


def get_covid_stat(country):
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"
    headers = {"X-RapidAPI-Host": "coronavirus-monitor.p.rapidapi.com",
               "X-RapidAPI-Key": "927cd44cc4msh043741a9bfd6f2bp197515jsn66d951ec2b53"}
    response = requests.request("GET", url, headers=headers)
    for stat in response.json()['countries_stat']:
        if stat['country_name'] == country:
            return stat
    return response.json()['countries_stat'][21]  # Default - Israel
