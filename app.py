import requests
from bs4 import BeautifulSoup

team_array = ['dbacks', 'cubs', 'redsox', 'athletics', 'braves', 'orioles', 'redsox', 'whitesox', 'reds', 'guardians', 'rockies', 'tigers', 'astros', 'royals', 'angels', 'dodgers', 'marlins', 'brewers', 'twins', 'mets', 'yankees', 'phillies', 'pirates', 'padres', 'giants', 'mariners', 'cardinals', 'rays', 'rangers', 'bluejays', 'nationals']



for team in team_array:

    url = f"https://www.mlb.com/{team}/roster/40-man"
    response = requests.get(url)
    #print(response)
    print(f"----------------------------- {team} -----------------------------")

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        fourty_man_roster = soup.find('div', 'players').find_all('table', 'roster__table')

        for roster in fourty_man_roster:
            players = roster.find('tbody').find_all('tr')
            for player in players:
                found_player = player.find('td', 'info').find('a')
                print(found_player.string)

    print(f"----------------------------- {team} -----------------------------")

    
    
