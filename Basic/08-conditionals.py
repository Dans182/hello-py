### Conditionals ###

my_condition = False

if my_condition: #Es lo mismo que esto if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition: #Es lo mismo que esto if my_condition === True:
    print("Se ejecuta la condición del segundo if") #Entra por acá y nos lo da como bueno, aunque no sea ni True ni False, simplemente porque tiene un dato dentro

if my_condition == 10:
    print("Se ejecuta la condición del tercer if") 
elif my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20") 
elif my_condition == 25:
    print("Es igual a 25") 
else:
    print("Es menor o igual que 10")

print("La ejecución continua")



my_string = ""
if my_string:
    print("Mi cadena de texto no es vacia") #No se imprime. No se cumple. Lo da como False

my_string = "Mi cadena de Texto"
if my_string:
    print("Mi cadena de texto no es vacia") #Se imprime. Se cumple. Lo da como True

if my_string == "Mi cadena de Textoooooooo":
    print("Estas cadenas de texto coinciden") #No se imprime. No se cumple. Lo da como False

