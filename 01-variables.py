# Variables

# por convención de py, recomiendan el uso de snake case
my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 8
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

print(type(print("Mi cadena de texto"))) # no es un tipo de dato, es una funcion de sistema, por eso el NoneType

# Concatenación de variables 
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

# Algunas funciones de sistema
print(len(my_string_variable))

# Variables en una sola línea
name, surname, alias, age = "Daniel", "Gaiteiro", "dans182", 33
print(name, surname, alias, age)

# Inputs
#name = input("What is your name: ")
#age = input("How old are you: ")
print(name)
print(age)

# Cambiemos su tipo
name = 35
age = "Daniel"
print(name)
print(age)
#python no tiene un tipado fuerte.

# Forzamos el tipo
address: str = "Mi dirección"
address = 32
print(type(address))