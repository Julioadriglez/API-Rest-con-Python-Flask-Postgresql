import psycopg2 
from  psycopg2 import DatabaseError # Para detectar los errores
from decouple import config  # para obtener las variables de entornocono el usuario, host, password y database
 

def get_connection(): # esta función es para hacer la conección con el servidor
    try:
        return psycopg2.connect(
            host = config(' PGSQL_HOST'),
            user = config('PGQL_USER'),
            password = config('PGQL_PASSWORD'),
            database = config('PGQL_DATABASE')
        )
    except DatabaseError as ex: # esto es por si falla levanta un error DatabaseError
        raise ex