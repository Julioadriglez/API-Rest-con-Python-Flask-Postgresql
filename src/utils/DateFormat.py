import datetime    # Se importa para la configuración del formato de la fecha

class DateFormat():
    
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')