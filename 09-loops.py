### Loops/Bucles/Ciclos ### 

# While 

my_condition = 0

while my_condition < 10:
    print(my_condition) #si la condicion nunca cambia, es un bucle infinito
    my_condition += 2
    #break
if my_condition == 10:
    print("Mi condición es igual a 10")
else:
    print("Mi condición es mayor o igual a 10")

    print("La ejecución continúa")

# while my_condition < 10:
#     print(my_condition)
#     my_condition += 2
#     #break
# else: #Este else pertenece propiamente a la sintaxis del while, cosa que no es así en otros lenguajes
#     print("Mi condición es mayor o igual a 10")

#     print("La ejecución continúa")