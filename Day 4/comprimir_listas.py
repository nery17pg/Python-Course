#MANERA DINÁMICA DE CONSTRUIR LISTAS

#EJEMPLOS ANTES DE APLICAR LA COMPRESIÓN DE LISTAS
palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)


#EJEMPLO DESPUÉS DE APLICAR LA COMPRESIÓN DE LISTAS
palabra = 'python'
lista = [letra for letra in palabra] #"Una letra por cada letra que haya en palabra"
print(lista)

#Ejemplo: Lo mismo que lo anterior, pero nos ahorramos la declaración de una palabra en un línea adicional
lista = [letra for letra in 'java'] #"Una letra por cada letra que haya en 'java'"
print(lista)

#Ejemplo: Valores numéricos
lista = [n for n in range(0,21,2)]
print(lista)

#Ejemplo modificando la lista anterior, ya que se dividen entre 2
lista = [n/2 for n in range(0,21,2)]
print(lista)

#Ejemplo donde solo van a entrar los valores que multiplicados por dos sean mayor a 10
lista = [n for n in range(0,21,2) if n*2>10]
print(lista)

#Ejemplo donde en el caso de los valores que no cumplan la condición, aparecerá la palabra 'no'
"""Nota: Aquí la condición la movemos al inicio o mejor dicho, en medio de la variable y el ciclo"""
lista = [n if n*2>10 else 'no' for n in range(0,21,2)]
print(lista)


#EJEMPLO DE LA VIDA REAL
pies = [10, 20, 30, 40, 50]
metros = [p/3.281 for p in pies]

print(metros)