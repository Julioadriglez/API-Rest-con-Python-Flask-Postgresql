from decouple import config # Objeto que nos permite sacar variables de entorno 

class Config:
    SECRET_KEY=config('SECRET_KEY')  # Lee la la llave de el archivo .env

class DevelopmenConfig(config):     # Se recibe config 
    DEBUG=True       # esto es para cuando se haga un cambio el servidor se refresque solo

config={  # Se crea un diccionario para regresar la llave de development con la llave de DevelopmentConfig
    'development': DevelopmenConfig
}