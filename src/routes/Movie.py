from email import message
from flask import Blueprint, jsonify

main= Blueprint('movie-blueprint', __name__) #esto es lo que necesita el Blueprint para poder crearse

@main.route('/') # Ruta raiz
def get_movies():
    return jsonify({'message': "prueba"})