from random import choice

#INICIALIZACIÓN DE VARIABLES
palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

#FUNCIONES
def elegir_palbra(lista_palabras):
    """Selecciona la palabra de manera aleatoria de la lista"""
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida)) #Longitud de las letras únicas

    return palabra_elegida, letras_unicas #Salida de la función


def pedir_letra():
    """Pedir letra al usuario"""
    letra_elegida = ''
    es_valida = False #Cualquier entrada no es válida hasta que tengamos una letra aquí
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'  

    while not es_valida: #"Mientras 'es_valida' no sea False"
        letra_elegida = input("Elige una letra: ") #Pedir letra al usuario
        if letra_elegida in abecedario and len(letra_elegida) == 1: #Comprobar que la letra ingresada se encuentre en el abecesario y solo sea una letra
            es_valida = True #Actualiza valor y sale del bucle
        else:
            print("No has elegido una letra correcta") #Sigue el bucle en caso de ser False

    return letra_elegida #Devuelve este valor para salida de la función


def mostrar_nuevo_tablero(palabra_elegida):
    """Mostrar guiones de manera actualizada por cada letra correcta"""
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l) #Va a agregarse la letra elegida en la lista_oculta
        else:
            lista_oculta.append('-') #Si no está, va a agregar un guión

    print(' '.join(lista_oculta)) #Cuando se termine de recorrer la palabra_elegida, se van a unir todos los carácteres resultantes


def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    """Revisar si la letra que puso el usuario está en la palabra y quitar vida en caso de no ser así"""
    fin = False #El juego no ha terminado

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1 #Aumenta el número de coincidencias, o mejor dicho, de aciertos
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra. Intenta con otra distinta")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1 #Se reduce 1 a las vidas actuales

    if vidas == 0:
        fin = perder() #Función posterior
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta) #Función posterior

    return vidas, fin, coincidencias #Devuelve estos valores al código


def perder():
    """Mostrar mensaje de que perdió al usuario y la palabra correcta"""
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)

    return True #Se devuelve True para que el juego deje de ejecutarse (revisar variable global)


def ganar(palabra_descubierta):
    """Mostrar al usuario la palabra final y una felicitación"""
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra!!!")

    return True #Se devuelve True para que el juego deje de ejecutarse (revisar variable global)


#UNIR FUNCIONES Y FUNCIONAMIENTO DEL JUEGO
palabra, letras_unicas = elegir_palbra(palabras) #Lo que nos devuelva esta variable se guarda en la 'palabra' y 'letras_unicas'

while not juego_terminado: #Mientras el juego no se haya terminado, entonces, "mientras no sea verdad que el juego se ha terminado"
    print('\n' + '*' * 20 + '\n') #Decoración
    mostrar_nuevo_tablero(palabra) #Mostrar los guiones (tablero)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado #Devuelve información de terminado