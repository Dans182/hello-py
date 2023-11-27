### Type Hints ###
my_string_variable = "My String Variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# Python es de tipado dinámico, el tipo de esta variable lo he cambiado en el curso del tiempo de ejecución

"""
Python 3.6+ tiene soporte para "type hints" opcionales.
Estos type hints son una nueva sintáxis, desde Python 3.6+, que permite declarar el tipo de una variable.
"""

my_typed_variable: str = "My typed string variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 8
print(my_typed_variable)
print(type(my_typed_variable))

# Aca igualmente el tipo de dato lo cambia, no obstante le especifico el tipo de dato. No ha cambiado absolutamente nada
# Aca lo que tiene es un tipado debil, le puedo decir que va a tener, pero no obligarle a tener un tipo de dato
# Al intuir el tipo de dato que le digo "que tiene/tendrá", al invocar la variable tendrá la posibilidad de acceder
# a los métodos nativos del tipo de dato

# En el tipado fuerte, tu no puedes cambiar el tipo de dato
# Python es de tipado dinámico y en estos ejemplos, el tipado es debil.
# Pero trabajar de esta manera, ayuda al editor y a la API, en este caso FastAPI que es con lo que trabajaré
# Nos ayuda a validar datos.