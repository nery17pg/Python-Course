"""EJERCICIO 1: Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:"""
from random import randint

def lanzar_dados():
    n1 = randint(1,6)
    n2 = randint(1,6)
    return n1, n2


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    
    if (suma_dados<=6):
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif (suma_dados>6) and (suma_dados<10):
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
        

n1,n2 = lanzar_dados()

resultado = evaluar_jugada(n1, n2)


"""EJERCICIO 2: Crea una función llamada reducir_lista() que tome una lista como argumento (crea también 
la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) 
y eliminando el valor más alto. El orden de los elementos puede modificarse.
    Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio
 de los valores de la misma. Debe devolver el resultado, sin imprimirlo."""
def reducir_lista(lista_numeros):
    lista_sin_duplicados = []
    
    for numero in lista_numeros:
        if numero not in lista_sin_duplicados:
            lista_sin_duplicados.append(numero)
    
    max_num = lista_sin_duplicados[0] 
    for numero in lista_sin_duplicados:
        if numero > max_num:
            max_num = numero
    
    lista_sin_duplicados.remove(max_num)
    
    return lista_sin_duplicados
    
    
def promedio(lista_numeros):
    suma = 0
    
    if len(lista_numeros) == 0:
        return 0  
    
    for num in lista_numeros:
        suma+=num
        
    promedio = suma / len(lista_numeros)
    return promedio
    
lista_numeros = [1,2,15,7,2]
lista_reducida = reducir_lista(lista_numeros)

resultado_promedio = promedio(lista_reducida)


"""EJERCICIO 3: Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder 
devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. 
El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
   - Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
   - Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta."""
from random import choice

def lanzar_moneda():
    opciones = ['Cara', 'Cruz']
    elegido = choice(opciones)
    return elegido
    

def probar_suerte(resultado, lista_numeros):
    if (resultado == 'Cara'):
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros
        
        
lista_numeros = [1, 15, 89, -100, 65]
elegido = lanzar_moneda()
probar_suerte(elegido, lista_numeros)