### Lists ###

my_list = list() #una lista es una estructura. Una forma de estructurar datos. Es lo mismo a un array o arreglo
# No es lo mismo una lista que un arreglo como tal. Un arreglo tiene "menos operaciones" con las listas podemos hacer mas cosas.
# Un vector es mas un array

my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Daniel", "Gaiteiro"]
print(my_other_list)

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#print(my_other_list[-5]) #Aca peta, porque no existe ese index
#print(my_other_list[4]) #IndexError igual

print(my_other_list.count("Daniel"))

# El count cuenta ocurrencias dentro de la misma lista. 
# El len se usa para contar los elementos de una lista

age, height, name, surname = my_other_list
print(name)

age, height, name, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3],
print(name)

print(my_list + my_other_list)

# Funciones de las listas

my_other_list.append("Dans182") # agrega nuevo elemento al final
print(my_other_list)

my_other_list.insert(1, "Rojo") # agrega un elemento en un index que yo especifique
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul") # elimino un elemento que yo especifique
print(my_other_list)

my_list.remove(30) # elimino el primer elemento que coincida con lo que yo le especifique
print(my_list)

print(my_list.pop()) # elimina el ultimo elemento
my_list.pop()
print(my_list)

my_pop_element = my_list.pop(2) # elimino el index del elemento que quiero desacoplar
print(my_list)
print(my_pop_element)

print(my_list)
print(type(my_list)) #Cambio el tipo. Antes era una lista y ahora un string. Esa es la propiedad de python. Tipado dinámico

del my_list[2] # Asi tambien borro pero index en concreto
print(my_list)

my_new_list = my_list.copy()

my_list.clear() # Asi borro la lista en su totalidad (el contenido)
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"

print(my_list)

my_list = ["Hola Python"] # así si sería una lista.
my_list = list("Hola Python")

