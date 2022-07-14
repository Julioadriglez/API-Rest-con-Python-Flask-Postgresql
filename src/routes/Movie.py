from flask import Blueprint
from flask import jsonify
# Models

from models.MovieModel import MovieModel

# esto es lo que necesita el Blueprint para poder crearse
main = Blueprint('movie_blueprint', __name__)


@main.route('/')  # Ruta raiz
def get_movies():
    try:
        # se le manda la los resultados de la iteracion del for
        movies = MovieModel.get_movies()
        return jsonify(movies)  # convierte el archivo en formato .json
    except Exception as ex:
        # Regresa error cuando hay un error por parte del servidor
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        # Regresa error cuando hay un error por parte del servidor
        return jsonify({'message': str(ex)}), 500

        
