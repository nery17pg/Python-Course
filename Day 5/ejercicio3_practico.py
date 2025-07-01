"""Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos veces consecutivas."""

def doble_cero(*args): #Puede recibir indeterminado número de argumentos
    cont = 0 #Inicializamos contador que será el índice para recorrer los elementos de args

    for cont in args: #Este bucle va a recorrer cada elemento de args
        if cont + 1 == len(args): #Comprueba la última posición. Si cont + 1 es igual a la longitud de args, 
            #quiere decir que estamos en el últimmo elemento de la lista
            return False
        elif args[cont] == 0 and args[cont + 1] == 0: #Comprobación de dos ceros consecutivos. Si la posición actual
            #y la posterior son igual a 0, será True
            return True
        else:
            cont += 1 #En caso que no sea ninguno de los dos casos, el contador sigue avanzando

    return False #Cuando el loop se complete, se sale del código y arroja False, demostrando que ninguna condición se cumplió

print(doble_cero(0,6,8,9,7,4,0,7,55,0)) #Caso prueba