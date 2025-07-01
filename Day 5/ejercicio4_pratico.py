"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró."""

def contar_primos(num): #El único argumento (num) es el límite hasta donde llegará
    primos = [2] #La lista inicia en 2 porque es el primer número primo
    i = 3 #El iterador se inicializa en 3 porque el primer número que se va a comprobar que es primo después del 2 es el 3

    if (num < 2): #num debe de ser mayor a 2, ya que si no es así regresará automáticamente False porque no hay primos menores que 2
        return 0
    
    while (i<=num): #Recorre los números desde 3 hasta num verificando si el número actual (i) es primo
        
        for n in range(3, i, 2): #El rango inicia en 3, hasta la posición actual y va de 2 en 2 porque ningún par es primo excepto el 2
            if (i%n==0): #Esta condición nos señala que el número actual no puede ser divisible por ninguno de los anteriores, ya que los números primos solo son divisible por sí mismos y el 1
                i +=2 #En caso de que no sea primo, pasa al siguiente número (no par)
                break #Sale automáticamente sin verificar más divisores

        else: #El else se ejecuta solo si el bucle for no se interrumpe con un break. Si el bucle for termina sin encontrar un divisor 
            #(es decir, si no se ejecuta el break), eso significa que i no tiene divisores y, por lo tanto, es un número primo.""" 
            primos.append(i) #Si el número (i) es primo, se agrega a la lista de primos
            i += 2 # y luego pasa al siguiente número impar

    print(primos) 
    return f"Total de números primos encontrados: {len(primos)}"

print(contar_primos(50))