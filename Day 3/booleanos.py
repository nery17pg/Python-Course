#La declaración siempre inicia con mayúscula
var1 = True
var2 = False
print(type(var1))
print(var1)


#Comparación con operador lógico
numero = 5 > 2+3
print(type(numero))
print(numero)


numero1 = bool(5<6) #Es lo mismo que poner directamente la expresión
numero2 = bool() #Me lanza valor False


#Booleanos en listas
lista = [1,2,3,4]
control = 5 in lista
print(type(control))
print(control)