#Pedir n posición en índice
mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)


#Buscar la posición de un carácter en el string
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("n")
print(resultado)


#Buscar la posición de un carácter en el string, pero en este caso nos arrojará
#la primera posición donde encuentre la letra
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a")
print(resultado)


#Buscar la posición donde empieza la palabra que buscamos
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("prueba")
print(resultado)


#El segundo parámetro nos ayuda a definir desde dónde va a buscar
#El tercer parámetro nos ayuda a definir hasta dónde (límite) queremos que busque
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a", 5, 10)
print(resultado)


#rindex busca de derecha a izquierda
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a")
print(resultado)