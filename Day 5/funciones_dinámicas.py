#EJEMPLO BÁSICO
def chequear_3_cifras(numero):
    """Revisa si un número en particular está dentro del rango asignado"""
    return numero in range(100,1000)

suma = 586 + 402

resultado = chequear_3_cifras(suma)
print(resultado)


#EJEMPLO CON LOOP Y CONDICIONALES
def chequear1_3_cifras(lista):
    """Revisa si los elementos de una lista están dentro del rango asignado"""
    for n in lista:
        if n in range(100,1000):
            return True #Return: Termina con el loop y sale de la función
        else:
            pass #Pase para que se siga haciendo el ciclo

resultado = chequear1_3_cifras([55,99,6000])
print(resultado)


#EJEMPLO EN CASO DE NO CUMPLIR
def chequear2_3_cifras(lista):
    """Revisa si los elementos de una lista están dentro del rango asignado.
    Si ninguno de los elementos de la lista cumple, se sale y arroja 'False'"""
    for n in lista:
        if n in range(100,1000):
            return True #Return: Termina con el loop y sale de la función
        else:
            pass #Pase para que se siga haciendo el ciclo
    
    return False #Se sale al no encontrar los elementos de la lista en el rango

resultado = chequear2_3_cifras([55,99,6000])
print(resultado)


#EJEMPLO DE GUARDAR ELEMENTOS EN UNA LISTA EN CASO DE CUMPLIRSE LA CONDICIÓN
def chequear3_3_cifras(lista):
    """Revisa si los elementos de una lista están dentro del rango asignado.
    En caso de que algunos cumplan la condición, se almacenarán en una lista que
    después será mostrada"""
    lista_3_cifras = [] #Declaramos la lista que va a contener los resultados
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n) #Agregamos a la lista los elementos que sí cumplan con la condición
        else:
            pass #Pase para que se siga haciendo el ciclo
    
    return lista_3_cifras #Muestra la lista con los elementos

resultado = chequear3_3_cifras([505,999,6000])
print(resultado)