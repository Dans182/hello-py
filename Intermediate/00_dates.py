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

year_2024 = datetime(2024, 1, 1)

print(year_2024)

from datetime import time #Con esta librería basicamente rellenamos nosotros los campos de hora. En datetime lo extrae directamente de la hora local

current_time = time(21, 6, 0) #Inicializamos hora

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date #Con esta librería basicamente rellenamos nosotros los campos de fecha. En datetime lo extrae directamente de la hora local y agrupa hora y fecha

#current_date = date(2025, 3, 31) #Inicializamos fecha
current_date = date.today() #Aca lo inicializamos con la fecha actual

print(current_date.year)
print(current_date.month)
print(current_date.day)

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)

from datetime import timedelta

time_delta = timedelta()