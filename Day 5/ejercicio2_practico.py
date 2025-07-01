"""Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver: 
['d','e','i','n','o','r','t']"""

def letras_unicas(palabra):
    mi_set = set(palabra) #Convertimos la palabra a un set, ya que los sets nos permiten los valores duplicados

    letras_ordenadas = sorted(mi_set) #Ordenamos las letras por orden alfabético

    return(letras_ordenadas) #Regresamos el valor


print(letras_unicas("entretenido")) #Imprimimos