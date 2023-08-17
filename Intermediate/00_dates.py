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

year_2023 = datetime(2023,1,1)

print(year_2023)


    

