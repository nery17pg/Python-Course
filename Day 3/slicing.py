#Fragmentar
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)


#Toma desde el inicio
texto = "ABCDEFGHIJKLM"
fragmento = texto[:5] #Primer parámetro vacío: va desde el inicio
print(fragmento)


#Toma hasta el final
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:] #Segundo parámetro vacío: va hasta el final
print(fragmento)