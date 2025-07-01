#EJEMPLO BÁSICO EN COLECCIONES
menor = min(12, 89, 54, 74, 99)
mayor = max(12, 89, 54, 74, 99)

print(menor)
print(mayor)


#EJEMPLO EN LISTAS
lista = [12, 89, 54, 74, 99]

print(f"El menor es {min(lista)} y el mayor es {max(lista)}") #En frase fina


#EJEMPLO CON STRINGS: Ordenables alfabéticamente
nombres = ['Nery', 'Chava', 'Sandra', 'Salvador'] #Ejemplo en lista
print(min(nombres))

nombre = "Nery"  #Ejemplo en un solo string
print(min(nombre)) #La salida sería la 'N' porque es mayúscula, para que tome todo como igual es necesario cambiar a lower o upper

nom = "Nery"  #Ejemplo en un solo string
print(min(nom.lower()))

nombre1 = "nery"  #Ejemplo en un solo string
print(min(nombre1)) 


#EJEMPLO CON DICCIONARIOS
dic = {'c1':12, 'c2': 6}
print(min(dic)) #La salida es el item con el valor alfabético más pequeño

dic1 = {'c1':12, 'c2': 6}
print(min(dic1.values())) #En este ya imprime el valor más pequeño por el método values()