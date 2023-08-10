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
