#ZIP: COMBINA DOS O MÁS LISTAS ENTRELAZANDO SUS ELEMENTOS EN TUPLES
#Nota: Zip llega al largo de la lista más corta
nombres = ['Namjoon', 'Jungkook', 'Yoongi']
edades = [30,27,31]
ciudades = ['Corea', 'Japón', 'China']

combinados = list(zip(nombres, edades, ciudades)) #Para poder juntarlos y que aparezcan, es necesario contenerlos en una lista
print(combinados)

#Con este loop junto todos los elementos de la lista según sus índices en una sola oración
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")