"""EJERCICIO 1: Muestra en pantalla frases como la del siguiente ejemplo:
La capital de Alemania es Berlín"""
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(capitales, paises))

for capital, pais in combinados:
    print(f"La capital de {pais} es {capital}")


"""EJERCICIO 2: Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que 
tú prefieras, dentro de la variable mi_zip."""
marcas = ['Nike', 'Adidas', 'Puma', 'Reebok']
productos = ['Zapatillas', 'Camiseta', 'Sudadera', 'Pantalones']

mi_zip = zip(marcas, productos)


"""EJERCICIO 3: Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés 
(en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:"""
espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espanol, portugues, ingles))
print(numeros)