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
print("################TRY/EXCEPT################")

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

print("################TRY/EXCEPT/ELSE################")

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    #Se ejecuta si se produce una expepción
    print("Se ha producido un error")
else:
    #Se ejecuta si no se produce una expepción
    print("La ejecución continúa correctamente") #Si se produce una excepción, el else no se ejecuta.
# El else en este caso se ejecuta, si las líneas del try se ejecutan correctamente y no redirecciona aun error.

print("################TRY/EXCEPT/ELSE/FINALLY################")

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    #Se ejecuta siempre, pase lo que pase.
    print("La ejecución continúa")
    #Aca se va por la excepción y ejecuta el finally.

#Si hay un try, tiene que haber un except. Opcionalmente puede haber un else y un finally


print("################EXCEPTIONS POR TIPO################")

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except TypeError: #Aca especifico que la excepción actuará cuando estamos con errores del tipo TypeError. Pero solo actuará en esa excepción
    print("Se ha producido un error")

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError: #Aca especifico que la excepción actuará cuando estamos con errores del tipo ValueError. En este caso rompe, porque el error es de Type y especifico que la excepción sea para las de Value
    print("Se ha producido un error")

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError: 
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")


print("################Captura de la información de la excepción################")
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error: #Aca tengo una variable que captura la información del error. Antes me decía el error, pero se rompía el código. Ahora tenemos la descripción del error, pero como variable y sin que se rompa la ejecución del programa
    print(error)
except TypeError as error:
    print(error)
except Exception as error: #Excepción genérica
    print(error)