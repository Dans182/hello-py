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