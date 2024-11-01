from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from app.api.games.routes import bp as games
from app.api.bgg.routes import bp as bgg
from app.api.auth.routes import bp as auth

api.register_blueprint(games)
api.register_blueprint(bgg)
api.register_blueprint(auth)