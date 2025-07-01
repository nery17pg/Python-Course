#SE REPITEN MIENTRAS SE CUMPLA LA CONDICIÓN
#AGUAS CON LOS CICLOS INFINITOS

#EJEMPLO BÁSICO
monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    #monedas = monedas - 1 #Break
    monedas -= 1 #Igual a la cantidad que tenga menos 1, lo mismito que la línea de arriba, pero simplificado
else:
    print("No tengo más dinero")


#EJEMPLO DONDE EL ACTUAR DEL LOOP DEPENDE DEL USUARIO
respuesta = 's'

while respuesta == 's': #Este loop se romperá cuando el usuario ingrese algo distinto a 's'
    respuesta = input("¿Quieres seguir? (s/n)")
else:
    print("Gracias, mi estimado") #Salida cuando el usuario ingresa algo distinto


#PASS - NO HACE NADOTA
respuesta = 'sip'

while respuesta == 'sip':
    pass #Guarda el lugar para que yo pueda ejecutar mi código, es más como herramienta para programador
print("Holaaa")


#BREAK - INTERRUMPE Y SE SALE DEL LOOP
nombre = input("Ingrese su nombre: ")

for letra in nombre:
    if letra == 'r':
        break #Si ingreso "Federico", la output vendría siendo F-E-D-E, porque cuando detecta una 'r' dejará de ejecutar el código
    print(letra)


#CONTINUE - NO INTERRUMPLE EL LOOP, SE SALTA LA CONDICIÓN Y RETOMA EL CÓDIGO POSTERIOR A ESA CONDICIÓN
name = input("Ingrese su nombre: ")

for letra in name:
    if letra == 'r':
        continue #Si ingreso "Federico", la output vendría siendo F-E-D-E-I-C-O, porque cuando detecto una 'r', se la salta y luego sigue ejecutando el código
    print(letra)