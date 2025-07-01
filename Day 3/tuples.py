my_tuple = (1,2,(10,20),4) #Declaración de tuple

my_tuple = list(my_tuple) #Ahora lo puse dentro de una lista

my_tuple = tuple(my_tuple) #Es de nuevo un tuple

print(type(my_tuple)) #Saber el tipo de variable

print(my_tuple[-2]) #Indice

print(my_tuple[2][0]) #Accedo al tuple dentro del tuple


#Se pueden asignar valores cuando tenemos la misma cantidad de elementos en el tuple y una variable (desempacar)
t = (1,2,3)
x,y,z = t
print(x,y,z)


#MÉTODOS DE TUPLES
t = (1,2,3,1)
#Con el método count podemos contar la cantidad de apariciones del elemento que estemos solicitando
print(t.count(1))
#Con el método index solicitamos saber el número de índice en el que está colocado el valor
print(t.index(2))