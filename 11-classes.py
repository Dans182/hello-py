### Classes ###

#Sirve para que todo lo que esté dentro de determinada clase, responda a determinada lógica. Esté todo dentro del mismo contexto
#Es para identificar nuestro código dentro de un ámbito de actuación

class MyEmptyPerson: #Con las clases, lo correcto es definirlas, es en camel case y no en snake case. O sea, de esto "def my_person" pasamos a "class MyPerson"
    pass #es una palabra reservada de sistema para que (en este caso, si no escribo mas dentro de la clase) no me de error. 

print(MyEmptyPerson) #Puede llamarse sin paréntesis
print(MyEmptyPerson()) #o con paréntesis. De cualquier forma

class Person: #Clase Persona/ Objeto Persona
    def __init__(self): #Esto (__init__) es reservado del sistema para crear un constructor de clase. Esto da la capacidad de que esta clase reciba algún parámetro
        pass