"""EJERCICIO 1: Crea una función llamada cantidad_atributos que cuente la cantidad de parámetros que se entregan, 
y devuelva esa cantidad como resultado."""
def cantidad_atributos(**kwargs):
    total = 0
    
    for arg in kwargs:
        total += 1
    
    return total

cantidad_atributos(a=1,b=2,c=3,d=4,f=5,e=6)


"""EJERCICIO 2: Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos 
entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo."""
def lista_atributos(**kwargs):
    return list(kwargs.values())
    
lista_atributos(a='1',b='2',c='3')


"""EJERCICIO 3: Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos."""
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")