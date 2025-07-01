#MÉTODOS BÁSICOS DE LISTAS
lista = ['g', 'o', 'b', 'm', 'c']
lista.sort()  #Reordena los elementos, pero este método no se puede asignar a una variable (noneType)
lista.reverse()  #Nos da vuelta el orden, al revés
print(lista)


mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

resultado = len(mi_lista)
lista_nueva = ['hola', 55, 6.1]
mi_lista3[0] = 'alfa'

mi_lista3.append('g')  #Se agrega un elemento al final
mi_lista3.pop()  #Elimina un elemento, si se deja vacío elimina el último
eliminado = mi_lista.pop(0)  #Aquí se almacena el elemento popeado

print(mi_lista3)
print(eliminado)