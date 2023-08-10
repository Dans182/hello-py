### Sets ### 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

# Listas []
# Tuplas ()
# Sets {}
# Diccionarios {}

my_other_set = {"Daniel", "Dans182", 35}
print(type(my_other_set)) #Ahora es un set

print(len(my_other_set))

print(my_other_set)
# print(my_other_set[0]) #devuelve error

my_other_set.add("Gaiteiro")
print(my_other_set) #Un set NO es una estructura ordenada. Por eso no podemos entrar a elementos en específico

my_other_set.add("Gaiteiro")
print(my_other_set) #Un set NO acepta repetidos

print("Dans182" in my_other_set) 
print("Dans183" in my_other_set) 

my_other_set.remove("Gaiteiro")
print(my_other_set) 

my_other_set.clear()
print(my_other_set) 
print(len(my_other_set)) 

del my_other_set
#print(my_other_set) #name 'my_other_set' is not defined

my_set = {"Daniel", "Gaiteiro", 33}
my_list = list(my_set) #esta operación en concreto no se recomienda, porque con cada ejecución, el set nace en un orden distinto
print(my_list)
print(my_list[1])

my_other_set = {"Kotlin", "Python", "JavaScript"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set).union(my_set).union({"Java", "C++"}))
print(my_new_set.difference(my_set)) #aca saco la diferencia. Saco los elementos de my_set de my_new_set
