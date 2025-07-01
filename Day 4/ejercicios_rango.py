"""EJERCICIO 1: Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista."""
mi_lista = list(range(2500,2586))


"""EJERCICIO 2: Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 
3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista."""
mi_lista = list(range(3,301,3))


"""EJERCICIO 3: Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado 
en una variable llamada suma_cuadrados."""
suma_cuadrados = 0

numeros = range(1,16)

for numero in numeros:
    cuadrado = numero*numero
    suma_cuadrados = suma_cuadrados + cuadrado