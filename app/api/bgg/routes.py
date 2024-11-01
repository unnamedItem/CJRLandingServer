from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.bgg import load_bgg, update_bgg

bp = Blueprint('bgg', __name__, url_prefix='/bgg')

class BggHandler:
    @staticmethod
    @bp.route('/load', methods=['GET'])
    # @jwt_required()
    def load_bgg():
        added = load_bgg()
        return {'message': f'Added ({added}) Games'}
    
    @staticmethod
    @bp.route('/update', methods=['GET'])
    # @jwt_required()
    def update_bgg():
        updated = update_bgg()
        return {'message': f'Updated ({updated}) Games'}