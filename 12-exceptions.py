### Exception Handling ###
# Manejo de errores #

# try
# except
# else
# finally

number_one = 5
number_two = 1
number_two = "1" #Aca el programa me daría error, porque no se puede llevar a cabo esta suma, y se rompería la ejecución del programa

#print(number_one + number_two)

#Un if/else no es sustituible o se puede considerar un try/catch (en Python es Try/Except)

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")