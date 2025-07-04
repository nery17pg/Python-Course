"""EJERCICIO 1: Implementa la función randint() de la librería random que te permita obtener un 
número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio"""
from random import randint

aleatorio = randint(1,10)


"""EJERCICIO 2: Implementa la función random() de la librería random que te permita obtener un número 
decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio"""
from random import random

aleatorio = random()


"""EJERCICIO 3: Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista 
de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo."""
from random import choice

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)