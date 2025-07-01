for numero in range(5): #Números del 0-4
    print(numero)

#Los dos parámetros de range nos indican desde donde inicia y hasta donde termina
for numero1 in range(1,5): #Números del 1-4
    print(numero1)

#El tercer parámetro indica el intervalo entre los números
for numero2 in range(20,30,2):
    print(numero2)

#Numeración del 1 al 100 en una lista y almacenando en variable
lista = list(range(1,101))
print(lista)