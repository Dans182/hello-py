### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

print(type(my_tuple))
print(type(my_other_tuple))

#Si escribimos solo paréntesis, es una tupla.
#Si escribimos tuple() es una tupla
#Si escribimos solo corchetes, es una lista
#Si escribimos list() es una lista

my_tuple = (35, 1.77, "Daniel", "Gaiteiro", "Daniel", "Dans182")
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Daniel"))
print(my_tuple.count("Gaiteiro"))
print(my_tuple.index("Daniel")) #Te dice el index de los elementos. en este caso me da solo el index de la primer coincidencia

#my_tuple[1] = 1.80 # arroja error. Porque las tuplas son inmutables

#Las tuplas son inmutables. Son constantes. No te permite agregar ni modificar datos.

my_other_tuple = (35, 60, 18)

print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

#Podemos "sumarlas" pero no modificar intrínsecamente estas.

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Car"
my_tuple.insert(1, "Azul")
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)