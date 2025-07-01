"""PROYECTO 4: El programa le va a preguntar al usuario su nombre, y luego le va a decir algo así como “Bueno, Juan, he pensado un
número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número”."""

from random import *

player = input("Tu nombre: ") #Nombre del usuario

print(f"¡Hola, {player}!\nHe pensado un número entre 1 y 100, pero solo tendrás 8 intentos para adivinar el número.\n¡Ponte pilas!") #Bienvenida

#Inicializamos variables como buena práctica
i = 0
numero = 0
numero_random = randint(1,100) #Generación de número random entre 1-100

for i in range(1,9): #Ciclo para limitar la cantidad de intentos a 8
    numero = int(input("Ingresa el número: ")) #Pedir el número al usuario y pasarlo a entero
    #Casos posibles
    if (numero < 1) or (numero > 100):
        print("Este número no está permitido.\nIntenta de nuevo")
    elif numero < numero_random:
        print("Chale, tu respuesta es incorrecta. El número que elegiste es menor al número secreto.\n¡Tú puedes! Intenta de nuevo")
    elif numero > numero_random:
        print("Tu respuesta es incorrecta. El número que elegiste es mayor al número secreto.\n¡Vamos! Intenta de nuevo")
    else:
        print("¡Felicidades, lo diste todo! Adivinaste el número")
        print(f"Número de intentos: {i}")
        break #Rompe el ciclo en caso de que adivine el número

#Al terminar los 8 intentos pasa directamente a esta condición y se despide del jugador
if numero != numero_random:
    print(f"Que triste es decirnos adiós, pero tus intentos se han acabado :(\nEl número secreto era {numero_random}\n¡Hasta pronto, vaquero {player}!")