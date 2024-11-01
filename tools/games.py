import sqlite3, json

DB_NAME = 'database.db'
DB_PATH = r'./instance/' + DB_NAME

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("SELECT * FROM games")

games = cursor.fetchall()

games_list = []
for game in games:
    games_list.append(dict(        
        age=game[12],
        average=game[7],
        averageweight=game[6],
        boardgamecategory=game[15],
        boardgamedesigner=game[16],
        boardgamemechanic=game[13],
        boardgamepublisher=game[17],
        boardgamesubdomain=game[14],
        description=game[3],
        image=game[4],
        maxplayers=game[9],
        maxplaytime=game[11],
        minplayers=game[8],
        minplaytime=game[10],
        name=game[1],
        objectid=game[0],
        thumbnail=game[5],
        yearpublished=game[2],
    ))

games_by_ale = json.loads(
    open('games_by_ale.json', 'r').read()
)

for game in games_by_ale:
    match: dict = next((x for x in games_list if x['objectid'] == game['objectid']), None)
    if match:
        match.update(game)

json.dump(games_list, open('games.json', 'w'), indent=4)

cursor.close()
