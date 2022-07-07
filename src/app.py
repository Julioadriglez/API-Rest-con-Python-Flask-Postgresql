from flask import Flask
from config import config # Se importa diccionario del archivo config

# Rutas
from routes import Movie # se importa el archivo movie y para que lo reconosca como un paquete de crea el archivo __init__.py en la carpeta donde esta el archivo Movie.py

app = Flask(__name__)

def page_not_fount(error):  # Para las paginas no encontradas mostrara este texto
    return "<hi>Not found page</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

# Blueprints   para asignar las  rutas
    app.register_blueprint(Movie.main, url_prefix='/api/movies') # cuando escriba esta direccion lo que va hacer es mandarme a la direccion raiz


    # Manejadores de error
    app.register_error_handler(404, page_not_fount) # le decimos al manejador de error que cuando sea el codigo 404  utilice la funcion page_not_fount
    app.run()
