#ENUMERATE: BUSCAR EL ÍNDICE EN UN LOOP
lista = ['a', 'b', 'c']

for item in enumerate(lista):
    print(item)
    #La salida es una serie de tuples donde se imprimirá el número del índice y el item

for indice, item in enumerate(lista):
    print(indice, item)
    #Salida sin tuples, solo los elementos

for indice, item in enumerate(range(50,55)): #Con range
    print(indice, item)

#EJEMPLO SIN CICLO
lista2 = ['ella', 'él', 'elle']

my_tuples = list(enumerate(lista2))
print(my_tuples)
print(my_tuples[1][0]) #De esta manera extraemos