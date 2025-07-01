#LOOP FOR BÁSICO
lista = ['a', 'b', 'c']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")


#OTRO EJEMPLO
lista2 = ['Namjoon', 'Seokjin', 'Yoongi', 'Hoseok', 'Jimin', 'Taehyung', 'Jungkook']
for miembro in lista2:
    if miembro.startswith('J'): #Método para revisar si inicia con tal letra
        print(miembro)
    else:
        print("Nombre que no comienza con J")


#EJEMPLO DE SUMA DE VALORES
#Explicación: En este caso al valor inicial de la variable mi_valor se le fueron sumando los siguientes valores, dando como resultado 15
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(f"Total: {mi_valor}") #Se ejecuta solo cuando termina de ejecutar el ciclo


#ITERANDO UNA PALABRA
palabra = 'python'
for letra in palabra:
    print(letra)

for letter in "bangtan": #Forma sencilla de iterar un string
    print(letter)


#ITERANDO LISTA QUE CONTENGAS LISTAS
for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)

for a, b in [[1,2], [3,4], [5,6]]: #La salida sería cada uno de los elementos
    print(a)
    print(b)
#Output: 1,2,3,4,5,6


#ITERANDO DICCIONARIOS
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}

for item in dic:
    print(item)

for item in dic.items(): #Nos permite verificar el item completo (método items())
    print(item)

for item in dic.values(): #values() es solo para ver los valores de los items
    print(item)

for c,d in dic.items(): #Solo los items sin los corchetes
    print(a,b)

    
"""Podemos iterar listas que contengan listas, listas simples y tuples, al igual que cadenas"""