"""EJERCICIO 1: Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
Controlar la complejidad es la esencia de la programación"""
frase = "Controlar la complejidad es la esencia de la programación"
resultado = frase[0:9]
print(resultado)


"""EJERCICIO 2: Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
Nunca confíes en un ordenador que no puedas lanzar por una ventana"""
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
r = frase[8::3]
print(r)


"""EJERCICIO 3: Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"""
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
r = frase[::-1]
print(r)