"""EJERCICIO 1: Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc."""
mi_lista = ['a', 2, 5.5, 'b', 'x']


"""EJERCICIO 2: Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
medios_transporte = ["avión", "auto", "barco", "bicicleta"]"""
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")


"""EJERCICIO 3: Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable
llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
1. manzana
2. banana
3. mango
4. cereza
5. sandía"""
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)