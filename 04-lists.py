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