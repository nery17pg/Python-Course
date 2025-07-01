"""KWARGS TRABAJAN CON DICCIONARIOS, ENTONCES TRANSFORMA LOS VALORES A DICCIONARIOS"""

#EXPLICACIÓN CONCEPTUAL
def suma(**kwargs):
    print(type(kwargs))

suma(x=3, y=5, z=2)


#USO PRÁCTICO DE KWARGS
def suma(**kwargs):
    """Suma y clave con valor"""
    total = 0 #Inicializamos el total

    for clave, valor in kwargs.items(): #Seleccionamos los elementos del kwarg
        print(f"{clave} = {valor}") #Imprimimos de esta forma los valores
        total += valor #Los valores de cada item se van a sumar al total

    return total

print(suma(x=3, y=5, z=2)) #Estos valores se toman para el diccionario


#IMPLEMENTACIÓN DE ARGUMENTOS, *ARGS Y **KWARGS EN UNA SOLA FUNCIÓN
def test(num1, num2, *args, **kwargs): #Jerarquía para argumentos
    """Imprimimos todos los valores sin importar el tipo de argumentos"""
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
 
    #Mostramos los argumentos de *args
    for arg in args:
        print(f"arg = {arg}")

    #Mostramos los valores del diccionario
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

#Declaramos args como lista y kwargs como diccionario
args = [100, 200, 300, 400]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

test(17, 27, *args, **kwargs) #Llamamos a la función con el orden de los parámetros respetando su jerarquía