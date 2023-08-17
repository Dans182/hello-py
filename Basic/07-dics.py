### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_dict = {"Nombre":"Daniel", "Apellido": "Gaiteiro", "Edad":33, 1: "python"}

my_other_dict = {"Nombre":"Daniel",
                  "Apellido": "Gaiteiro", 
                  "Edad":33,
                  "Lenguajes": {"Javascript", "Python", "C++"},
                    1: 1.81
                }

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))
print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Dans"

print(my_dict["Calle"])
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Gaiteiro" in my_dict) #False
print("Apellido" in my_dict) #True Porque realmente la key y donde busca es en el Key, no en el valor


print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre", 1)) #Esto me sirve para crear un nuevo directorio, con unos keys pero sin los valores
print(my_new_dict)

my_new_dict_2 = dict.fromkeys(my_other_dict, ("Roberto")) #Esto me sirve para duplicar los keys de otro diccionario en uno nuevo y a mayores, estoy seteando el valor de todos esos keys con UN valor idéntico para todos.

my_values = my_new_dict_2.values()
print("Dict", my_new_dict_2)
print("Values", my_values)
print("list", list(my_new_dict_2))
print("Tuple", tuple(my_new_dict_2))
print("Set", set(my_new_dict_2))

print(type(my_values))