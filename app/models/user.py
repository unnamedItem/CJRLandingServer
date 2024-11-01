from app import db

USER_ATTRIBUTES = [
    ('objectid', int),
    ('username', str),
    ('password', str),
]

class User(db.Model):
    __tablename__ = 'users'
    objectid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, **kwargs):
        self.objectid = kwargs.get('objectid')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')

    def to_dict(self):
        return {key: getattr(self, key) for key, _ in USER_ATTRIBUTES}
    
    def __str__(self) -> str:
        return self.username
    
    def __repr__(self) -> str:
        return '<User %r>' % self.username
    
    def __eq__(self, other) -> bool:
        return self.username == other.username
    
    def __ne__(self, other) -> bool:
        return self.username != other.username
    
    def __hash__(self) -> int:
        return hash(self.username)