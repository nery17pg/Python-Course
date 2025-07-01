"""EJERCICIO 1: Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado."""
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [numero**2 for numero in valores]


"""EJERCICIO 2: Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares."""
valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [num for num in valores if num%2==0]


"""EJERCICIO 3: Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista 
de valores de temperatura en grados Celsius."""
temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(grados-32)*(5/9) for grados in temperatura_fahrenheit]