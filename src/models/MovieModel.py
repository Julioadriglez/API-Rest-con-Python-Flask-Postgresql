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
    
    @classmethod
    def get_movie(self, id): # Filtrar paelicula por
        try:
            connection = get_connection() # Para que me obtenga la conección
            
            with connection.cursor() as cursor: # Esta es la conección a la base de datos
                cursor.execute("SELECT id, title, duration, released FROM movie  WHERE id = %s", (id,)) # se hace la consulta mediante el id
                row = cursor.fetchone() 
                
                movie = None
                if row != None:
                    movie = Movie(row[0], row[1], row[2], row[3]) #Es para que me muestre los 4 datos cada iteracion del "for"
                    movie = movie.to_JSON() # La conneción la regresa en formato .json
                    
            connection.close() #para cerrar la coneccion
            return movie
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_movie(self, movie): # Insertar peliculas
        try:
            connection = get_connection() # Para que me obtenga la conección
            
            with connection.cursor() as cursor: # Esta es la conección a la base de datos
                cursor.execute("""INSERT INTO movie (id, title, duration, released) 
                                VALUES (%s, %s, %s, %s)""",(movie.id, movie.title, movie.duration, movie.released)) # Se envia la informacion a la DB
                affected_rows = cursor.rowcount # Saca cuantas filas a afectado y Filas que se afectan al hacer la inserción
                connection.commit() # Para confirmar los cambios que estoy haciendo
            connection.close() #para cerrar la coneccion
            return affected_rows # Regresamos las filas afectadas
        except Exception as ex:
            raise Exception(ex)