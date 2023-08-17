### Functions ###

def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number) #Aca la función se ejecuta pero no retorna ningún valor

sum_two_values(2,3)
sum_two_values("2","3") #concatena strings
sum_two_values(2.4,7.3)


def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number #Aca la función se ejecuta y retorna un valor

my_result = sum_two_values_with_return(8, 10)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Gaiteiro", "Daniel")

print_name(surname= "Gaiteiro", name= "Daniel") #reordené o cambié el orden de los parámetros de la función

def print_name_with_default(name, surname, alias= "Sin alias"): #establecer un valor por defecto en un parámetro
    print(f"{name} {surname} {alias}")

print_name_with_default("Daniel", "Gaiteiro")
print_name_with_default("Daniel", "Gaiteiro", "Dans182")

def print_texts(*text): #al indicar el asterisco, no le doy un numero de parámetros fijo, sino dinámico. Puedo pasarle cuantos quiera y los que quiera
    print(text)

print_texts("Hola")


def print_texts_2(*texts):
    for text in texts:
        print(text)

print_texts_2("Hola", "Cómo estás?", "Qué haces?")


def print_texts_3(*texts): #al indicar el asterisco, no le doy un numero de parámetros fijo, sino dinámico. Puedo pasarle cuantos quiera y los que quiera
    for text in texts:
        print(text.upper())

print_texts_3("Hola", "Cómo estás?", "Qué haces?")