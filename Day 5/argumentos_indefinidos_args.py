"""*args"""
"""Podemos definir funciones cuyo número de argumentos sea variable.
Nota: No es obligatorio usar args, python entiende con el puro asterisco y otra palabra,
sin embargo, se considera una buena práctica usar *args"""

#EJEMPLO DE USO DE *ARGS
def suma(*args):
    total = 0

    for arg in args: #Por cada argumento en argumentos
        total += arg #suma el valor de la derecha a la variable de la izquierda y asigna ese resultado a la variable de la izquierda

print(suma(5,6,7))


#FORMA MÁS SENCILLA DEL CÓDIGO ANTERIOR
def suma_simple(*args):
    return sum(args)

print(suma_simple(22,11,33,44))