### Loops/Bucles/Ciclos ### 

# While 

my_condition = 0

while my_condition < 10:
    print(my_condition) #si la condicion nunca cambia, es un bucle infinito
    my_condition += 2
if my_condition == 10: #Y acá metes un if en el while. Y el else forma parte de la sintaxis del if y no del while. El elif no es compatible con el while.
    print("Mi condición es igual a 10")
else:
    print("Mi condición es mayor o igual a 10")

print("La ejecución continúa")

# while my_condition < 10:
#     print(my_condition)
#     my_condition += 2
# else: #Este else pertenece propiamente a la sintaxis del while, cosa que no es así en otros lenguajes. Es opcional
#     print("Mi condición es mayor o igual a 10")
#     print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        break

    print(my_condition)