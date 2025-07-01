#Conversión implícita
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))


#Conversión explícita
num1 = 5.8
print(num1)
print(type(num1))

new_num1 = int(num1)
print(new_num1)
print(type(new_num1))


#Convertimos el tipo de dato str en int
edad = input("Dime tu edad: ")
print(type(edad))

edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad
print(nueva_edad)
#print("Tu nueva edad va a ser: " + nueva_edad) #Marca error por error de concatenación
