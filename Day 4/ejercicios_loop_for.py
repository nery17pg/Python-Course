"""EJERCICIO 1: Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre."""
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase:
    print(f"Hola {nombre}")


"""EJERCICIO 2: Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena 
el resultado de la suma en una variable llamada suma_numeros:"""
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero


"""EJERCICIO 3: Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en 
las variables suma_pares y suma_impares respectivamente:"""
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if (numero%2==0):
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero