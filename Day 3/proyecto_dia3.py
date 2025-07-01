"""Vas a crear un programa que primero le pida al usuario que ingrese un texto. Nuestro código va a procesar esa 
información para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:"""

texto = input("Ingrese el texto que desee (artículo, cuento, poema, frase, párrafo, etc.): ").lower()
l1 = input("Ingrese la primera letra: ").lower()
l2 = input("Ingrese la segunda letra: ").lower()
l3 = input("Ingrese la tercera letra: ").lower()
#Eliminar signos de puntuación para que no los tome como letras en el resto del análisis
texto = texto.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")

"""Primero: ¿cuántas veces aparece cada una de las letras que eligió?"""
lista = [l1,l2,l3]

ap1 = texto.count(l1)
ap2 = texto.count(l2)
ap3 = texto.count(l3)

print("\n")
print("CANTIDAD DE LETRAS")
print(f"La letra '{l1}' aparece {ap1} veces en el texto.")
print(f"La letra '{l2}' aparece {ap2} veces en el texto.")
print(f"La letra '{l3}' aparece {ap3} veces en el texto.")


"""Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto."""
palabras = texto.split()
num_palabras = len(palabras)
print("\n")
print("CANTIDAD DE PALABRAS")
print(f"En el texto hay un total de {num_palabras} palabras.")


"""Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última."""
primera_letra = texto[0]
ultima_letra = texto[-1]
print("\n")
print("PRIMERA Y ÚLTIMA LETRA")
print(f"La primera letra del texto es '{primera_letra}'.")
print(f"La última letra del texto es '{ultima_letra}'.")


"""Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras."""
palabras.reverse()
texto_invertido = " ".join(palabras)
print("\n")
print("TEXTO INVERTIDO")
print(f"El texto invertido quedaría así: {texto_invertido}")


"""Quinto: el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto."""
esta_texto = "Python".lower() in palabras
dic = {
        True:"La palabra 'Python' sí se encuentra dentro del texto.", 
        False:"La palabra 'Python' no se encuentra dentro del texto."
    }
print("\n")
print("BUSCANDO PALABRA")
print(dic[esta_texto])