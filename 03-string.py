### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(my_string)
print(my_other_string)

print(my_string + " " + my_other_string)

my_new_line_string = 'Este es un String\ncon salto de línea'
print(my_new_line_string)

my_new_tab_string = '\tEste es un String con tabulación'
print(my_new_tab_string)

my_scape_string = '\\tEste es un String \nescapado'
print(my_scape_string)

# Formateo de cadenas de texto

name, surname, age = "Daniel", "Gaiteiro", 33

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es: " + name + " " + surname + " y mi edad es: " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")