"""JUEGO: ELIGE EL PALITO"""

from random import shuffle

"""LISTA INICIAL"""
palitos = ['--', '----', '------', '--------'] 


"""MEZCLAR PALITOS"""
def mezclar(lista):
    shuffle(lista) #Mezclamos la lista cuando se nos mande
    return lista 


"""PEDIRLE AL USUARIO INTENTO"""
def probar_suerte():
    intento = '' #Se inicializa en strg porque lo que ingrese el usuario es una cadena

    while intento not in ['1', '2', '3', '4']: #Mientras el usuario NO ingrese un valor que sea igual a los de la lista de aquí, le seguirá pidiendo intento
        intento = input("Elige un número del 1 al 4: ") #Mensaje que le aparecerá al usuario y aquí se almacena la respuesta en intento

    return int(intento) #Aquí regresa el valor, pero ya lo convertimos a INT


"""COMPROBAR INTENTO"""
def comprobar_intento(lista, intento): #Tomamos los parámetros de lista (palitos) y el intento que ingresa el usuario
    if lista[intento-1] == '----': #Si el intento que ingrese el usuario es igual al de '----' va a lavar los platos. Se resta uno porque las listas inician en 0
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado") #En caso contrario, se salva 

    print(f"Te ha tocado {lista[intento-1]}") #Si no le toca lavar los platos, le aparecerá el palito que escogió al usuario


"""INTERACCIÓN ENTRE FUNCIONES"""
palitos_mezclados = mezclar(palitos) #En esta variable invocamos a la función 'mezclar' con la lista de 'palitos' como parámetro, que es lo que va a mezclar
seleccion = probar_suerte() #En esta variable se toma el valor que ingresa el usuario y por ello no hay parámetro, ya que solo se almacena el intento
comprobar_intento(palitos_mezclados, seleccion) #Llamamos a la función de 'comprobar_intento' con las variables anteriores como parámetros. 
#lista=palitos_mezclados & intento=seleccion 