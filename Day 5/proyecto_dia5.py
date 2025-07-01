"""PROYECTO DÍA 5: 'EL AHORCADO'
Objetivo general: El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una seriede guiones que representa 
la cantidad de letras que tiene la palabra. El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la palabra oculta, 
el sistema le va a mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en la palabra oculta, pierde una vida."""

from random import choice

"""INICIO DEL JUEGO"""
print("¡Intenta adivinar la palabra secreta!\nSolo tendrás 8 intentos para adivinar la palabra.\n¿Lista? Vamos a ello.")

"""DIBUJO DEL AHORCADO"""
print(" _________\n/        |\n|        O\n|       /|\\\n|       / \\\n|\n============")

"""OPCIONES DE PALABRAS"""
opciones = ['literatura', 'nuclear', 'anoranza', 'sempiterno', 'cordillera', 'nostalgia', 'sabelotodo', 'efimero', 'paradigma', 'renacimiento', 
'misterioso', 'esplendido', 'vanguardista', 'melancolia', 'resiliencia', 'desenlace', 'contemplativo', 'abismal', 'transcendental', 'volatil',
'inefable', 'inmortalidad', 'temporalidad', 'incertidumbre', 'metafisico', 'conocimiento', 'entropia', 'revolucion', 'abstraccion', 'creatividad',
'dinamico', 'hermetico', 'sabiduria', 'existencial', 'tangibilidad', 'introspeccion', 'incomparable', 'hipotetico', 'inmutable', 'resistencia',
'universo', 'dilema', 'sostenibilidad', 'infinito', 'legado', 'conexion', 'inspiracion', 'efusivo', 'renovacion', 'desbordante', 'interrogante']
palabra = choice(opciones)

"""NÚMERO DE LETRAS Y GUIONES"""
num_letras = len(palabra)
print(f"Total de letras en la palabra: {num_letras}")
guiones = ["_"] * num_letras #Genera los guiones

"""VIDAS INICIALES"""
vidas = 8
incorrectas = [] #Lista para almacenar las letras incorrectas


"""FUNCIONES"""
def pedir_letra():
    """Pedir letra al usuario"""
    print('\n')
    letra = input("Ingrese una letra: ").lower() #Se pasa a minúscula para evitar diferencia o errores
    return letra


def validar_letra(letra):
    """Validar que lo que ingresa el usuario sea una letra"""
    if len(letra) == 1 and letra.isalpha(): #La primera condición se asegura que solo se ingrese una letra
        #isalpha() asegura que el carácter sea una letra (sin números ni carácteres especiales)
        return True
    else:
        return False


def letra_encontrada():
    "Busca si se encuentra la letra en la palabra y si no, la vuelve a pedir"
    while True: #Mientras la letra sea válida
        letra = pedir_letra()
        if validar_letra(letra):
            return letra #Devuelve el valor de la letr
        else:
            print("Carácter no válido. Recuerda que debe de ser una letra.") #En caso contrario, este será el mensaje para el usuario


def letra_no_encontrada(letra):
    """Notificar que la letra no se encuentra, agregar a la lista de incorrectas, descontar vida y mostrar estado del juego"""
    global vidas #Llamamos a la variable 'vidas', esta es global y se debe de acompañar con la palabra 'global' para que no se tome como local
    incorrectas.append(letra) #Agrega la letra incorrecta a la lista 
    vidas -= 1 #Resta una vida a las n vidas

    print(f"La letra '{letra}' no está en la palabra.")
    print(f"Letras incorrectas: {', '.join(incorrectas)}") #Manera en la que se mostrará la lista y se agregará
    print(f"Te quedan {vidas} vidas")

    if vidas == 0: #Si se cumple esto, pierde
        print("GAME OVER!")
        return False
    return True #Si no es así, devuelve True


def lugar_letra(letra):
    """Actualizar los guiones con la letra encontrada en la palabra"""
    letra_encontrada = False #Se inicializa en False para que cuando sea True se detenga el loop e indicamos que la letra no se ha encontrado

    for i, l in enumerate(palabra): #enumerate (índice, letra). El primero es la posición de la letra en la palabra y la segunda es la letra como tal
        if l == letra: #Si la letra actual en la palabra es igual a la letra que estamos buscando
            guiones[i] = letra  # Actualiza la posición de la letra en los guiones
            letra_encontrada = True #Cambia a True para que se detenga el loop

    return letra_encontrada 


"""INTERACCIÓN DE FUNCIONES PARA EL FUNCIONAMIENTO DEL JUEGO"""
while vidas > 0 and "_" in guiones: #Mientras le queden vidas y espacios disponibles...
    print(f"Palabra: {' '.join(guiones)}") #Imprime los guiones
    letra = letra_encontrada() #Pedir letra al usuario
    print('\n' + '*' * 20 + '\n') #Decoración

    if letra in palabra: #Si la letra se encuentra en la palabra
        lugar_letra(letra) #Se llama a la función para asignarle su lugar y también se manda el parámetro de 'letra' para que se ponga esa
    else: 
        if not letra_no_encontrada(letra): #En caso de no encontrarse, simplemente rompe el ciclo
            break

    if "_" not in guiones: #Si ya no quedan guiones en 'guiones', quiere decir que ganó
        print(f"¡Eso es todo! Has ganado, adivinaste la palabra secreta: {palabra}")
        break #Rompe el loop

if vidas == 0: #En el caso de ya no tener vidas, pierde y le anuncia la palabra correcta
    print(f"La palabra era: {palabra}")
    print("GAME OVER!")