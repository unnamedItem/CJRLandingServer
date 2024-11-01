from app import db

GAME_ATTRIBUTES = [
    ('objectid', int),
    ('name', str),
    ('description', str),
    ('yearpublished', int),
    ('minplayers', int),
    ('maxplayers', int),
    ('minplaytime', int),
    ('maxplaytime', int),
    ('age', int),
    ('thumbnail', str),
    ('image', str),
    ('averageweight', float),
    ('average', float),
    ('boardgamemechanic', str),
    ('boardgamesubdomain', str),
    ('boardgamecategory', str),
    ('boardgamedesigner', str),
    ('boardgamepublisher', str),
]

class Game(db.Model):
    __tablename__ = 'games'
    objectid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    yearpublished = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))
    averageweight = db.Column(db.Float)
    average = db.Column(db.Float)
    minplayers = db.Column(db.Integer)
    maxplayers = db.Column(db.Integer)
    minplaytime = db.Column(db.Integer)
    maxplaytime = db.Column(db.Integer)
    age = db.Column(db.Integer)
    boardgamemechanic = db.Column(db.String(255))
    boardgamesubdomain = db.Column(db.String(255))
    boardgamecategory = db.Column(db.String(255))
    boardgamedesigner = db.Column(db.String(255))
    boardgamepublisher = db.Column(db.String(255))

    def __init__(self, **kwargs):
        self.objectid = kwargs.get('objectid')
        self.name = kwargs.get('name')
        self.yearpublished = kwargs.get('yearpublished')
        self.description = kwargs.get('description')
        self.image = kwargs.get('image')
        self.thumbnail = kwargs.get('thumbnail')
        self.averageweight = kwargs.get('averageweight')
        self.average = kwargs.get('average')
        self.minplayers = kwargs.get('minplayers')
        self.maxplayers = kwargs.get('maxplayers')
        self.minplaytime = kwargs.get('minplaytime')
        self.maxplaytime = kwargs.get('maxplaytime')
        self.age = kwargs.get('age')
        self.boardgamemechanic = kwargs.get('boardgamemechanic')
        self.boardgamesubdomain = kwargs.get('boardgamesubdomain')
        self.boardgamecategory = kwargs.get('boardgamecategory')
        self.boardgamedesigner = kwargs.get('boardgamedesigner')
        self.boardgamepublisher = kwargs.get('boardgamepublisher')

    def __repr__(self) -> str:
        return '<Game %r>' % self.name
    
    def __str__(self) -> str:
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, other) -> bool:
        return self.name == other.name
    
    def __ne__(self, other) -> bool:
        return self.name != other.name
    
    def to_dict(self):
        return {key: getattr(self, key) for key, _ in GAME_ATTRIBUTES}
