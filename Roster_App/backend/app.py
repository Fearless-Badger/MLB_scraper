from flask import Flask
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/roster/<team>")
def disp_roster(team):
    
    url = f"https://www.mlb.com/{team}/roster/40-man"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        fourty_man_roster = soup.find('div', 'players').find_all('table', 'roster__table')
        team_roster = []
        for roster in fourty_man_roster:
            players = roster.find('tbody').find_all('tr')
            for player in players:
                found_player = player.find('td', 'info').find('a')
                team_roster.append(found_player.string)
        return f"<h1>{team_roster}</h1>"