### Loops/Bucles/Ciclos ### 

## While ##

print("########### WHILE ###########")


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
        print("Se detiene la ejecución")
        break
    print(my_condition)



## For ##
print("########### BUCLÉS FOR ###########")

my_list = [35, 24, 63, 53, 30, 30, 18] #Guardan información de uno en uno de forma ordenada
my_tuple = (35, 1.77, "Daniel", "Gaiteiro", "Daniel", "Dans182") #Guardan elementos que no se pueden modificar
my_set = {"Daniel", "Dans182", 35} #Guardan elementos, y no se pueden repetir
my_dict = {"Nombre":"Daniel",
                  "Apellido": "Gaiteiro", 
                  "Edad":33,
                  "Lenguajes": {"Javascript", "Python", "C++"},
                    1: 1.81
                } #Guardan elementos de forma clave-valor

for element in my_list:
    print(element)

for element in my_tuple:
    print(element)

for element in my_set:
    print(element)

for element in my_dict: #imprime las keys, no los values
    print(element)
