import xmltodict
import requests
from flatten_json import flatten

from app import db
from app.utils import config, db_logger

from app.models.game import Game, GAME_ATTRIBUTES



collection = config.get('bgg', 'collection')
collection_url = f"{config.get('bgg', 'api_url')}/collection/{collection}"

def get_collection_ids():
    response = requests.get(collection_url)
    if response.status_code == 200:
        data = xmltodict.parse(response.text)
        flat = list(map(lambda item: flatten(item), data['items']['item']))
        ids = list(map(lambda item: item['@objectid'], flat))
        return ids
    
def get_game(id):
    url = f"{config.get('bgg', 'api_url')}/boardgame/{id}?stats=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = xmltodict.parse(response.text)
        flat = flatten(data['boardgames']['boardgame'], separator='.')
        names = data['boardgames']['boardgame']['name']
        name = list(filter(lambda x: isinstance(x, dict) and x.get('@primary'), isinstance(names, list) and names or [names]))[0]['#text']
        
        def check_attr(attr, key, type):
            keys = key.split('.')
            if attr == key:
                return True
            elif type == str:
                return attr in keys and '#text' in keys
            elif key == '@objectid' and attr == 'objectid':
                return True
            return attr in keys
        
        def parse_attr(value, type):
            return type(value)

        def get_attr(attr, type):
            return parse_attr(', '.join([value for key, value in flat.items() if check_attr(attr, key, type)]), type)

        kwargs = {attr: get_attr(attr, type) for attr, type in GAME_ATTRIBUTES}
        game = Game(**kwargs)
        game.name = name
        return game
        

def load_bgg():
    db_logger.info(f'Getting games from BGG...')
    game_ids = get_collection_ids()
    added = 0
    for id in game_ids:
        already_exists = db.session.query(Game).filter_by(objectid=id).first()
        if not already_exists:
            game = get_game(id)
            db.session.add(game)
            added += 1
    db.session.commit()
    db_logger.info(f'Finished getting games from BGG...')
    db_logger.info(f'Added ({added}) games')
    return added

def update_bgg():
    db_logger.info(f'Updating games in BGG...')
    game_ids = get_collection_ids()
    updated = 0
    for id in game_ids:
        already_exists = db.session.query(Game).filter_by(objectid=id).first()
        if already_exists:
            game = get_game(id)
            db.session.merge(game)
            updated += 1
    db.session.commit()
    db_logger.info(f'Finished updating games in BGG...')
    db_logger.info(f'Updated ({updated}) games')
    return updated