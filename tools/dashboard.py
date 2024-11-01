import sqlite3, json

DB_NAME = 'database.db'
DB_PATH = r'./instance/' + DB_NAME

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("SELECT * FROM games")

games = cursor.fetchall()

def dict_max_players(games, l=False):
    data = dict()
    for game in games:
        if game[9] not in data: data[int(game[9])]  = 0 if not l else []
        data [int(game[9])]+= 1 if not l else [game[1]]
    return data

def top_10(games):
    # games = [game for game in games if game[1] not in ["Republia", "Soccard: Fútbol con cartas", "Revelación", "Blockits", "Magus: Aura Mortis"]]
    _top_10 = sorted(games, key=lambda x: float(x[7]), reverse=True)[:10]
    return { game[1]: game[7] for game in _top_10 }

def overall_weight(games):
    return sum([float(game[6]) for game in games]) / len(games)

def total_games(games):
    return len(games)

def games_for_category(games, l=False):
    data = dict()
    for game in games:
        category = game[15].split(", ")
        for c in category:
            if c not in data: data[c]  = 0 if not l else []
            data[c]+= 1 if not l else [game[1]]
    return data

def games_for_mechanics(games, l=False):
    data = dict()
    for game in games:
        category = game[13].split(", ")
        for c in category:
            if c not in data: data[c]  = 0 if not l else []
            data[c]+= 1 if not l else [game[1]]
    return data

def games_for_difficulty(games, decimal=0, l=False):
    data = dict()
    for game in games:
        dificulty = f"%.{decimal}f" % float(game[6])
        if dificulty not in data: data[dificulty]  = 0 if not l else []
        data [dificulty]+= 1 if not l else [game[1]]
    return data

def sort_dict(data):
    return dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

def sort_dict_by_key(data):
    return dict(sorted(data.items(), key=lambda item: item[0]))

data = dict(
    total_games=total_games(games),
    top_10=top_10(games),
    max_players=sort_dict_by_key(dict_max_players(games, True)),
    overall_weight=overall_weight(games),
    games_for_category=sort_dict(games_for_category(games, True)),
    games_for_mechanics=sort_dict(games_for_mechanics(games, True)),
    games_for_difficulty=sort_dict(games_for_difficulty(games, 0, True))
)

with open('dashboard.json', 'w') as f:
    json.dump(data, f, indent=4)

cursor.close()
connection.close()

print("Operation done successfully")