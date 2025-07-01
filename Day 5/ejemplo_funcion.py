precios_cafe = [('capuchino', 1.5), ('Expresso', 1.2), ('Americano', 1.9)] #Declaramos una lista de tuples

def cafe_mas_caro(lista_precios): 
    """Función para saber cuál es el café más caro"""
    #Inicializamos variblaes, una de int y otra de strg
    precio_mayor = 0
    cafe_caro = ''

    for cafe, precio in precios_cafe: #En este loop se van a recorrer tanto los valores de café como el del precio en la lista global
        if precio > precio_mayor: #Si el precio es mayor al que se tiene como precio mayor actual, este va a tomar su lugar
            precio_mayor = precio #Aquí sustituimos el valor actual más alto por el nuevo
            cafe_caro = cafe #Y aquí lo mismo, pero con el nombre del café
        else:
            pass #En caso que no se cumpla lo anterior, solo pasa al siguiente tuple

    return(cafe_caro, precio_mayor) #Regresa los valores finales 

cafe, precio = cafe_mas_caro(precios_cafe) #Declaramos las variables 'cafe' y 'precio' llamando a la función y tomando los valores de la lista global

print(f"El café más caro es {cafe}, cuyo precio es {precio}") #Imprimimos con mensaje literal