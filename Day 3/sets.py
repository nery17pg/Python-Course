my_set = set([1,2,3,4,5]) #Declaración del set (Forma 1)
print(type(my_set))
print(my_set)


another_set = {1,2,3} #Segunda opción de declaración
print(type(another_set))
print(another_set)


my_set2 = set([1,2,3,4,4,5,6,6,7,7,8])
print(my_set2) #La salida solo me mostrará elementos únicos, ya que py elimina los repetidos


#Unión de sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) #Con el método union juntamos a s1 y s2 en otro set, llamado s3
print(s3) #Solo tendremos 5 elementos porque py elimina repetidos


#Métodos de sets
s1 = {1,2,3}
s1.add(4) #Este método add añade un elemento al set
s1.remove(3) #Este método remove elimina el número 3
s1.discard(6) #La diferencia con remove es que si le pido que remueva un elemento que no está, no me lanza error
s1.pop() #El método elimina el número que quiere, uno random
sorteo = s1.pop()
s1.clear #Este método clear vacía nuestro set
print(s1)
print(sorteo) #Me saldrá el número random que quitó pop