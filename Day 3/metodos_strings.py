#upper(): Mayúsculas
texto = "Este es el texto de Nereyda"
resultado = texto[2].upper()
print(resultado)


#lower(): Minúsculas
texto = "Este es el texto de Nereyda"
resultado = texto.lower()
print(resultado)


#split(): Separa en elementos y los guarda en una lista. 
#También nos ayuda a contar la cantidad de palabras que contiene dicha lista/texto
texto = "Este es el texto de Nereyda"
resultado = texto.split("t") #Toma la t como separador
print(resultado)


#join(): Une los elementos de una lista
a = "Aprender"
b = "Python"
c = "es"
d = "chido"
e = " ".join([a,b,c,d]) #Aquí es donde se unen las variables anteriores
print(e)


#find(): Busca el elemento
texto = "Este es el texto de Nereyda"
resultado = texto.find("s")
print(resultado)


#replace(): Nos ayuda a reemplazar
texto = "Este es el texto de Nereyda"
resultado = texto.replace("Nereyda", "todos") #Primer parámetro es lo que vamos a reemplazar y el segundo con lo que reemplazamos
print(resultado)
#Reemplazar letras
texto = "Este es el texto de Nereyda"
resultado = texto.replace("e", "x")