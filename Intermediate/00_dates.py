### Dates ###

#De esta manera tengo que importar el modulo datetime, y despues entrar en datetime de nuevo y despues el método. De la forma de abajo no
# import datetime
# now = datetime.datetime.now()
# print(now)

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 1, 1)

print(year_2023)

from datetime import time #Con esta librería basicamente rellenamos nosotros los campos de hora. En datetime lo extrae directamente de la hora local

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date #Con esta librería basicamente rellenamos nosotros los campos de fecha. En datetime lo extrae directamente de la hora local y agrupa hora y fecha

#current_date = date(2025, 3, 31)
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)
    

