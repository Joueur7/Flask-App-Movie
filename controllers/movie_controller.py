from flask import Blueprint, jsonify
from handlers.movie_handler import get_movie_handler

movies_controller = Blueprint('movies_controller', __name__)

@movies_controller.route('/v1/movie/<int:id>')
def get_movie(id):
    movie = get_movie_handler(id)
    return jsonify(movie)
