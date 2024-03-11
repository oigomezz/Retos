# Crea una función que sea capaz de detectar si existe un viernes 13
# en el mes y el año indicados.
# - La función recibirá el mes y el año y retornará verdadero o falso.
from datetime import date

def viernes_13(anio:int, mes:int):
    try:
        semana = date(anio,mes,13).weekday()
        return True if semana == 4 else False
    except Exception:
        return False

print(viernes_13(2023, 10))
print(viernes_13(2023, 3))
print(viernes_13(2023, 1))
print(viernes_13(2023, 13))
print(viernes_13(-2023, 1))
# print(viernes_13(2023, "1"))
print(viernes_13(2023, 0))