#EJEMPLO BÁSICO
if 10 > 11:
    print("Es correcto")
else:
    print("No es correcto")


#EJEMPLO CON TRES MÉTODOS DE CONTROL DE FLUJO
mascota = 'perro'

if mascota == 'gato':
    print("Tienes un gato")
elif mascota == 'perro':
    print("Tienes un perro")
else:
    print("No sé qué animal sea")


#ANIDAR CONDICIONES IF
edad = 14
calificacion = 9

if edad < 18:
    print("Estás chamaquito")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Échale ganas")
else:
    print("Eres adulto ya")