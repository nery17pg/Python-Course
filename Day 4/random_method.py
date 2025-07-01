#LIBRERÍA DE RANDOM EN PYTHON

"""from random import randint
Con lo de arriba importamos método por método de la librería random de py"""

from random import * #Con el asterisco importamos absolutamente todo lo de la librería random

#Método randint: Lanza int
aleatorio = randint(1,50)
print(aleatorio)


#Método uniform: Lanza float
aleatorio2 = uniform(1,5)
print(aleatorio2)

aleatorio3 = round(uniform(1,5),1) #Float, pero con un solo decimal
print(aleatorio3)


#Método random: No usa parámetro y avienta un número random (puede ser int o float) entre 0-1
aleatorio4 = random()
print(aleatorio4)


#Método choice: Permite trabajar con una selección aleatoria dentro de los elementos de una lista o cualquier coleccionable
colores = ['azul', 'verde', 'negro', 'morado', 'blanco']

aleatorio5 = choice(colores)
print(aleatorio5)


#Método shuffle: Mezcla los elementos, funcional para juegos de cartas
numeros = list(range(5,50,5))

shuffle(numeros)
print(numeros)
#Shuffle no se puede almacenar en una lista, genera una modificación en el lugar y no se pueden utilizar en strings porque estos son inmutables