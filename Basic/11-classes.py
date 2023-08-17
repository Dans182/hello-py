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
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Propiedad Pública
        self.__name = name #Aca estoy definiendo esta variable como privada. Propiedad Privada

    def get_name (self):
        return self.__name #Hago un getter haciendo una función con retorno. De esta manera puedo acceder al nombre, pero no puedo modificarlo
    #Si quisiera modificarla, pues tendría que crear un setter

    def walk(self): #si no pongo el self, no puede acceder a fullname, porque fullname está guardado dentro de self
        print(f"{self.full_name} Está caminando")

my_person2 = Person2("Daniel", "Gaiteiro")
print(my_person2.full_name)
# print(my_person2.__name) #Al ser una variable privada, no me la muestra, no puedo acceder a ella. Tengo que definir un getter ahora
print("@@@@@@@@@@@@@@@@@@@@@@", my_person2.get_name())

my_person2.walk()

my_other_person = Person2("Pedro", "Perez", "Dans182")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Ricardo Rodríguez (El loco de los gatos)"
print(my_other_person.full_name)


#El constructor es para crear la instancia, para crear por PRIMERA VEZ ese objeto
#Posteriormente puedo acceder a mi clase, acceder a una propiedad que tenga mi clase e incluso la puedo modificar.
#Una vez creada la instancia/objeto, despuedo modificarla sin usar el constructor





#Programación Orientada a Objetos
#Crean sistema de clases y objetos

#Podemos crear una clase, que sería una plantilla, en la que definimos los atributos y métodos predeterminados de un objeto, y en base a dicha clase, crear objetos que son entidades que derivan de estas clases.

#Vivienda puede ser una clase, en la que definimos que debe tener paredes, suelo, techo, puertas y ventanas y cada casa que tenga dichos requisitos, será un objeto instanciado de la clase vivienda.
#Los objetos son ejemplos de las clases

my_other_person.full_name = 666 #Tipado debil. Puedo cambiarle el tipo de dato en cualquier momento
print(my_other_person.full_name)


# No se puede definir que el constructor fuera solo string. Porque el tipado es dinámico.