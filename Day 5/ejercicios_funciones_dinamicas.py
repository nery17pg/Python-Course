"""EJERCICIO 1: Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de 
una lista son positivos, y False si al menos uno de los valores es negativo. 
Crea una lista llamada lista_numeros con valores positivos y negativos."""
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False 
    return True
    
lista_numeros = [1, -3, 5, 7, -2]


"""EJERCICIO 2: Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean 
mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma."""
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if (n>0) and (n<1000):
            suma = suma + n 
        else:
            pass
            
    return suma
    
lista_numeros = [100, 50, 89, -1, 10001]


"""EJERCICIO 3: Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva 
el resultado de dicha cuenta."""
def cantidad_pares(lista_numeros):
    pares = 0
    for n in lista_numeros:
        if n%2==0:
            pares+=1
    return pares
    
lista_numeros = [1, 50, 502, 755, 34]