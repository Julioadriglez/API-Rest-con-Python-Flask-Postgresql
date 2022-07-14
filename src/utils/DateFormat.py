import datetime    # Se importa para la configuración del formato de la fecha

class DateFormat():
    @classmethod
    def convert_date(self,date):
        return datetime.datetime.strftime(date, '%d/%m/%Y') # el formato a usar esta en este codigo el cual es dia, mes y años