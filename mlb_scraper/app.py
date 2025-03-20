from flask import Flask, redirect, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

# home route
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method=="POST":
        team_name = request.form.get("team_name")
        if team_name:
            return redirect(f"/roster/{team_name}")
    return render_template("index.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

# json of players
@app.route("/roster/<team>")
def disp_roster(team):

    if not team:
        return redirect("/")

    try:
        url = f"https://www.mlb.com/{team}/roster/40-man"
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

            return jsonify(result)
        else:
            return jsonify({"error" : "Site Not Found"}), 404 # invalid path
    except Exception as e:
        #    raise Exception(e) # lol
        return jsonify({"error": str(e)}), 500
    
def process_table(table, res, position):

    res[position] = [] # create entry in dict

    
    tbody = table.find('tbody').find_all('tr') # table -> tbody -> tr
    for player in tbody:
        found_player = player.find('td', 'info').find('a') # td -> info -> a 
        res[position].append(found_player.string) # append name to list
