from flask import Blueprint

from app import db
from app.models.game import Game

bp = Blueprint('games', __name__, url_prefix='/games')


class GamesHandler:
    @staticmethod
    @bp.route('/<int:id>')
    def get_game(id):
        game = db.session.query(Game).filter_by(objectid=id).first()
        if not game:
            return {'message': 'Game not found'}, 404
        return game.to_dict()

    @staticmethod
    @bp.route('/')
    def get_games():
        games = db.session.query(Game).order_by(Game.name).all()
        return [game.to_dict() for game in games]