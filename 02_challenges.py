### Challenges  ###

"""
Reto #0: EL FAMOSO "FIZZ BUZZ”
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()

"""
Reto #1: ¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower(): #Este if evalua directamente si NO es un anagrama. Si estás ante una palabra idéntica
        return False, "No es un anagrama"
    return sorted(word_one.lower()) == sorted(word_two.lower()) #Acá si evalua directamente si es un anagrama.

print(is_anagram("Amor", "Roma"))