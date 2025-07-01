dic = {1:'a', 2:'b'}
print(dic)

dic[3] = 'c'  #Se modifica el diccionario agregando valores
print(dic)

dic[2] = '8'  #Se sobreescribe
print(dic)

print(dic.keys())  #Nos trae todas las llaves que tiene
print(dic.values())  #Nos imprime todos los valores
print(dic.items())  #Nos trae todos los elementos del diccionario

dic = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dic['c2'][1].upper())  #La salida es la letra E myúscula

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c3']['s2'])  #Imprime lo del diccionario de la clave c2 y el índice 1 dentro de ese diccionario


cliente = {'nombre':'Nereyda', 'apellido':'Villalobos', 'peso':88, 'talla':1.55}
consulta = (cliente['apellido'])
print(consulta)

diccionario = {'c1':'valor1', 'c2':'valor1'}
print(diccionario)

resultado = diccionario['c1']  #Se invoca una clave
print(resultado)