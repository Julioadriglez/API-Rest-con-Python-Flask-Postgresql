from utils.DateFormat import DateFormat # importamos la clase DateFormat para pasar el formato de la fecha
class Movie():
    def __init__(self, id, title=None, duration=None, release=None) -> None:  # __init__ es el constructor de la clase
        self.id=id   # Son atributos de clase
        self.title=title
        self.duration=duration
        self.released=release
        
    def to_JSON(self): # para la converción de los datos a .json
        return{
            'id' : self.id,
            'title' : self.title,
            'duration' : self.duration,
            'released' : DateFormat.convert_date(self.released) # resive el valor del la fecha con el formato dia, mes y año
        }
    
           
