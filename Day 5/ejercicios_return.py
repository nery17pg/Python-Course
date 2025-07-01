"""EJERCICIO 1: Crea una función llamada potencia que tome dos valores numéricos como argumentos. 
Deberá devolver el número que resulte de resolver una potencia"""
def potencia(n1, n2):
    resultado = n1**n2
    return resultado


"""EJERCICIO 2: Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), 
y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado."""
def usd_a_eur(dolares):
    resultado = dolares * 0.90
    return resultado
    
dolares = 15 


"""EJERCICIO 3: Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus 
caracteres y los devuelva de ese modo y en mayúsculas.
Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP". También, deberás crear una variable llamada palabra, 
que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada."""
def invertir_palabra(palabra):
    lista = list(palabra)
    lista.reverse()
    return ''.join(lista).upper()
    
palabra = "Python"