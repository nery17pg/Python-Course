"""PLANTEAMIENTO: La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones."""

#Ingreso de datos
nombre = input("Ingresa tu nombre: ")
ventas_totales = input("Ingresa cuánto has vendido este mes: ")

#Conversión
ventas_totales = float(ventas_totales)

#Calcular
comisiones = (ventas_totales*13)/100
#comisiones = round((ventas_totales*13)/100,2)

#Redondeo
comision = round(comisiones,2)

#Salida
print(f"Hola, {nombre}. Tus comisiones de este mes son de ${comision}")
