"""EJERCICIO 1: Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:"""
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
r = frase.upper()
print(r)


"""EJERCICIO 2: Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de
 listas/strings, y muestra en pantalla el resultado."""
lista_palabras = ["La","legibilidad","cuenta."]
e = " ".join(lista_palabras)
print(e)


"""EJERCICIO 3: Reemplaza en la siguiente frase:
"Si la implementación es difícil de explicar, puede que sea una mala idea."
los siguientes pares de palabras:
"difícil" --> "fácil"
"mala" --> "buena"
y muestra en pantalla la frase con ambas palabras modificadas."""
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil", "fácil").replace("mala", "buena")

print(resultado)