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

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# División

language_slice = language[1:3]
print(language_slice) #yt Cuenta de index 1 a 3 sin contar el 3

language_slice = language[1:]
print(language_slice) #ython Pilla todo a partir del index 1.

language_slice = language[-2]
print(language_slice) #imprime o. index 0 en la P. index -1 es el ultimo caracter. index -2 es el penúltimo

language_slice = language[0:6:2]
print(language_slice) #pto. va desde index 0 al 6, de dos en dos

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))