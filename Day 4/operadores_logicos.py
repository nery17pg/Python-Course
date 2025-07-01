#AND
my_bool = (4 < 5) and (5 > 6) #Las dos comparaciones se deben de cumplir
print(my_bool)

my_bool2 = (5 == 5) and ('perro'=='perro')
print(my_bool2)


#OR
my_bool3 = (1 == 10) or (3 == 30) #Al menos una de las dos comparaciones se debe de cumplir
print(my_bool3)

texto = "namjoon te amo mucho"
my_bool4 = ('te' in texto) or ('amo' in texto)
print(my_bool4)


#NOT
booleanito = not 'a' == 'a' #Doble comparación, "si no es verdad"
print(booleanito) #Output será False, porque 'a' es igual a 'a'

booleanito2 = not ('a' != 'a') #Dobles negaciones
print(booleanito2) #Output será True