import re
import requests
import datetime
from datetime import datetime as dt

headers = {
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "a1ffcb01c1mshda56f268d598b8dp164008jsne22fe21b6101"
}


def get_football_leagues(country):
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    querystring = {"country": country, "current": "true"}
    return requests.request("GET", url, headers=headers, params=querystring).json()['response']


def get_all_fixtures(country):
    all_fixtures = []
    url_fixtures = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    for league in get_football_leagues(country):
        league_dict = {'league': league["league"]["name"], 'league_logo': league["league"]["logo"]}
        league_id = league['league']['id']
        query_fixtures = {"league": league_id, "season": int(datetime.date.today().year) - 1,
                          "from": dt.today().strftime('%Y-%m-%d'),
                          "to": (dt.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d')}
        response = requests.request("GET", url_fixtures, headers=headers, params=query_fixtures).json()['response']
        league_dict['fixtures'] = [
            {
                "date": get_date_format(item["fixture"]["timestamp"]),
                "venue": item["fixture"]["venue"]["name"],
                "city": item["fixture"]["venue"]["city"],
                "team_1": item["teams"]["home"]["name"],
                "team_1_logo": item["teams"]["home"]["logo"],
                "team_2": item["teams"]["away"]["name"],
                "team_2_logo": item["teams"]["away"]["logo"],
            }
            for item in response
        ]
        all_fixtures.append(league_dict)
        if len(all_fixtures) >= 20:
            return all_fixtures
    if not all_fixtures:  # Default Israel
        return get_all_fixtures("Israel")
    return all_fixtures


def get_date_format(timestamp):
    date_time_obj = datetime.datetime.fromtimestamp(timestamp)
    return f"{date_time_obj.day}/{date_time_obj.month}/{date_time_obj.year}"


def get_main_games(all_fixtures):
    main_games = []
    for league in all_fixtures:
        for fixture in league['fixtures']:
            main_games.append(fixture)
            if len(main_games) >= 3:
                return main_games
