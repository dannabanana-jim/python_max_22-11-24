#3 - Definir una función que calcule la longitud de una lista o una cadena dada.
#(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def longitud(elemento):
    """
    Calcula la longitud de una lista o cadena.

    Args:
        elemento (list o str): La lista o cadena cuya longitud se desea calcular.

    Returns:
        int: La longitud del elemento.
    """
    contador = 0
    for _ in elemento:  # Itera por cada elemento o carácter
        contador += 1
    return contador


cadena = input("Introduce una cadena: ")
print("La longitud de la cadena es:", longitud(cadena))

lista = input("Introduce elementos de una lista separados por comas: ").split(',')
print("La longitud de la lista es:", longitud(lista))



