"""EJERCICIO 1: Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
nombre: Karen
apellido: Jurgens
edad: 35
ocupacion: Periodista"""
mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion':'Periodista'}


"""EJERCICIO 2: Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario."""
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])


"""EJERCICIO 3: Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), 
y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
nombre: Karen
apellido: Jurgens
edad: 36
ocupacion: Editora
pais: Colombia"""
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia' 