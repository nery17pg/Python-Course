"""EJERCICIO 1: Imprime en pantalla frases como la siguiente:
'{nombre} se encuentra en el índice {indice}'
Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate()."""
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


"""EJERCICIO 2: Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() 
los índices de cada caracter del string "Python".
Llama a la lista obtenida con el nombre de variable lista_indices ."""
lista_indices = list(enumerate("Python"))
print(lista_indices)


"""EJERCICIO 3: Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:"""
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)