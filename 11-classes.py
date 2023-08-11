### Classes ###

#Sirve para que todo lo que esté dentro de determinada clase, responda a determinada lógica. Esté todo dentro del mismo contexto
#Es para identificar nuestro código dentro de un ámbito de actuación

class MyEmptyPerson: #Con las clases, lo correcto es definirlas, es en camel case y no en snake case. O sea, de esto "def my_person" pasamos a "class MyPerson"
    pass #es una palabra reservada de sistema para que (en este caso, si no escribo mas dentro de la clase) no me de error. 

print(MyEmptyPerson) #Puede llamarse sin paréntesis
print(MyEmptyPerson()) #o con paréntesis. De cualquier forma

#class Person: #Clase Persona/ Objeto Persona
#    def __init__(self, name, surname): #Esto (__init__) es reservado del sistema para crear un constructor de clase. Esto da la capacidad de que esta clase reciba algún parámetro. Siempre se llama self
        #Este def, no es propiamente una función, en este caso con el __init__ estamos haciendo un constructor de clase
#        pass


#No está bien tener un fichero donde mezclemos funciones con clases. Lo correcto sería que tuviera un fichero que se llamara "Person" y dentro tengo la class Person y allí tengo sus métodos.

print("###################################################################")

class Person:
    def __init__(self, name, surname): #El self es obligatorio, si queremos crear una clase que tenga un constructor, tenemos que pasar el self. Si estamos dentro de persona, se refiere a el mismo, a la clase Persona
        self.name = name #el primer "name" es el parámetro, el segundo name es la variable 
        self.surnameeee = surname #el primer "surname" es el parámetro, el segundo surname es la variable. Aca igualo

my_person = Person("Daniel", "Gaiteiro")

print(my_person.name)
print(my_person.surnameeee) 

print(f"{my_person.name} {my_person.surnameeee}")

# class Person:
#     def __init__(self):
#         self.name = "Daniel"
#         self.surnameeee = "Gaiteiro"  #Acá estoy definiendo el nombre y apellido dentro del constructor

#Name y surname son PROPIEDADES de la clase

print("###################################################################")


class Person2:
    def __init__(self, name, surname):
        self.full_name = f"{my_person.name} {my_person.surnameeee}"

    def walk(self): #si no pongo el self, no puede acceder a fullname, porque fullname está guardado dentro de self
        print(f"{self.full_name} Está caminando")

my_person2 = Person2("Daniel", "Gaiteiro")
print(my_person2.full_name)

my_person2.walk()