"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
1- Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
2- Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
3- Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio."""

def devolver_distintos(a,b,c):
    #Inicialización de variables
    resultado = a+b+c
    lista = [a,b,c]

    print(f"Resultado de la suma: {resultado}")

    if (resultado>15): #Primer caso
        return f"Valor máximo: {max(lista)}"
    elif (resultado<10): #Segundo caso
        return f"Valor mínimo: {min(lista)}"
    else: #Tercer caso
        return f"Valor intermedio: {sorted(lista)[1]}"

print(devolver_distintos(20,5,7)) #Parámetros