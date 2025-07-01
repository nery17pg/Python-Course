"""EJERCICIO 1: Remueve los caracteres a la izquierda de nuestro texto principal:
,  :  %  _  #
Utiliza el método lstrip(). Imprime el resultado en pantalla."""
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

resultado = texto.lstrip(",:%_#")

print(resultado)


"""EJERCICIO 2: Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando
el método insert():
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]"""
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 

frutas.insert(3, "naranja")


"""EJERCICIO 3: Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), 
utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:"""
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)