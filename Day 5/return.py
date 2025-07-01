#FUNCIÓN APLICANDO RETURN
def multiplicar(num1, num2):
    total = num1*num2
    return total #Return solo devuelve el valor, no lo imprime

resultado = multiplicar(5, 10) #Los valores de return se recomienda almacenarlos en una variable
print(resultado)