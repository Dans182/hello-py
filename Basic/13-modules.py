### Modules ###

# Un modulo es esa librería, ese fichero donde tenemos código que queremos utilizar.
# Cada fichero se comporta como un módulo.

#my_function() no funciona, porque en este fichero no existe.

import module #Tengo que importar y posteriormente acceder
# from 10-functions import sum_two_values Esta importación no funciona, porque Python no reconoce que el nombre de un fichero empiece llamándose con un número.

module.sum(5, 3, 9)

# Aca importo TODO lo que hay en module en mi programa, pero eso muchas veces es innecesario. No hace falta importar todo si solo necesitamos
# una funcionalidad. Esto hace que mi programa se ralentice un poco mas
# Estoy exponiendo este módulo hacia afuera.
# Modulo tambien son librerías ya creadas por el propio sistema, el propio python pero que por defecto no tengamos acceso. Puede ser una librería creada por otra persona,
# que nos la bajemos por github y la instalamos en nuestro proyecto y lo usamos en nuestra app.

module.printValue("Hola, k ase?")

print("############################")
from module import sum # Acá importo funciones específicas del modulo, y no el módulo completo

sum(5, 3, 9)

module.printValue("Hola, k ase?")

import math

print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE #importo solo propiedades del módulo y la renombro

print(PI_VALUE)