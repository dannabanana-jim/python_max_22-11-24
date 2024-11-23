#6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" 
#debería devolver la cadena "odnaborp yotse"


def inversa(cadena):
    """
    Invierte el orden de los caracteres en una cadena.

    Args:
        cadena (str): La cadena a invertir.

    Returns:
        str: La cadena invertida.
    """
    invertida = ""
    for caracter in cadena:
        invertida = caracter + invertida  # Añade cada carácter al inicio de la nueva cadena
    return invertida


cadena = input("Introduce una cadena: ")
print("La cadena invertida es:", inversa(cadena))


