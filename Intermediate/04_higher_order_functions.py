### Higher order Functions ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, a_function):
    return a_function(first_value + second_value)

#Aca lo que ocurre es que tenemos una función que es capaz de ejecutar otras funciones. Paso a_function como parámetro y despues la retorno, ahí demostrando que es
#una función al meter parámetros entre paréntesis
#y al hacer el print, queda demostrado que meto dos parámetros que son variables y una función.

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

#Y esto es lo que son las funciones de orden superior.


### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add
#Aca sum ten lo que hace es retornar una funcion

add_closure = sum_ten()
print(add_closure(5))
#El concepto de closure se puede entender como una funcion, que define otra funcion y retorna es una función
#No retorna un valor ni un calculo. Retorna una funcion

