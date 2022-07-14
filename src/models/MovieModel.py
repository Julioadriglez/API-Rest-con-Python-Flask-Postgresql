from database.db import get_connection
from .entities.Movie import Movie

class MovieModel():
    
    @classmethod
    def get_movies(self):
        try:
            connection = get_connection() # Para que me obtenga la conección
            movies = []
            
            with connection.cursor() as cursor: # Esta es la conección a la base de datos
                cursor.execute("SELECT id, title, duration, released FROM movie ORDER BY title ASC") # se hace la consulta directamente de forma acendente
                resultset = cursor.fetchall() 
                
                for row in resultset:
                    movie = Movie(row[0], row[1], row[2], row[3]) #Es para que me muestre los 4 datos cada iteracion del "for"
                    movies.append(movie.to_JSON()) # La conneción la regresa en formato .json
                    
            connection.close() #para cerrar la coneccion
            return movies
        except Exception as ex:
            raise Exception(ex)
        