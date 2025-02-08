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
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            fourty_man_roster = soup.find('div', 'players').find_all('table', 'roster__table')

            # unpack tables into positions
            pitchers = fourty_man_roster[0]
            catchers = fourty_man_roster[1]
            infielders = fourty_man_roster[2]
            outfielders = fourty_man_roster[3]

            result = {} # str(position) : [ str(player_names) ]

            # add player names to their respective list in result dict
            process_table(pitchers, result, "Pitchers")
            process_table(catchers, result, "Catchers")
            process_table(infielders, result, "Infielders")
            process_table(outfielders, result, "Outfielders")

            return f"<h1>{result}</h1>"
        else:
            return "<h1>Site Not Found</h1>" # invalid path
    except Exception as e:
        #    raise Exception(e) # lol
        return f"<h1>Error accessing site : {e}</h1>"
    
def process_table(table, res, position):

    res[position] = [] # create entry in dict

    if table:
        tbody = table.find('tbody').find_all('tr') # table -> tbody -> tr
        if tbody:
            for player in tbody:
                found_player = player.find('td', 'info').find('a') # td -> info -> a 
                res[position].append(found_player.string) # append name to list
