"""EJERCICIO 1: Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, 
y que retorne la suma de sus valores al cuadrado."""
def suma_cuadrados(*args):
    total = 0
    
    for arg in args:
        n = arg**2
        total += n
        
    return total
        
suma_cuadrados(1,2,3)


"""EJERCICIO 2: Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus 
valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- 
como positivos)."""
def suma_absolutos(*args):
    total = 0
    
    for n in args:
        if(n<0):
            n = -n #Aquí se vuelve positivo el número en caso de ser negativo
        total += n
    
    return total


"""EJERCICIO 3: Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida 
de números."""
def numeros_persona(nombre, *args):
    suma_numeros = 0
    
    for n in args:
        suma_numeros += n
    
    return f"{nombre}, la suma de tus números es {suma_numeros}"
    
numeros_persona('Namjoon', 1, 2, 3, 5)