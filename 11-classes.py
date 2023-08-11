### Classes ###

#Sirve para que todo lo que esté dentro de determinada clase, responda a determinada lógica. Esté todo dentro del mismo contexto
#Es para identificar nuestro código dentro de un ámbito de actuación

class MyEmptyPerson: #Con las clases, lo correcto es definirlas, es en camel case y no en snake case. O sea, de esto "def my_person" pasamos a "class MyPerson"
    pass #es una palabra reservada de sistema para que (en este caso, si no escribo mas dentro de la clase) no me de error. 

print(MyEmptyPerson) #Puede llamarse sin paréntesis
print(MyEmptyPerson()) #o con paréntesis. De cualquier forma

class Person: #Clase Persona/ Objeto Persona
    def __init__(self, name, surname): #Esto (__init__) es reservado del sistema para crear un constructor de clase. Esto da la capacidad de que esta clase reciba algún parámetro. Siempre se llama self
        #Este def, no es propiamente una función, en este caso con el __init__ estamos haciendo un constructor de clase
        pass


#No está bien tener un fichero donde mezclemos funciones con clases. Lo correcto sería que tuviera un fichero que se llamara "Person" y dentro tengo la class Person y allí tengo sus métodos.

print("###################################################################")
my_person = Person("Daniel", "Gaiteiro")

print(my_person)