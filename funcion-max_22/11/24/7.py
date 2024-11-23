#7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
#  ejemplo: es_palindromo ("radar") tendría que devolver True

def es_palindromo(cadena):
    """
    Verifica si una cadena es un palíndromo.

    Args:
        cadena (str): La cadena a verificar.

    Returns:
        bool: True si la cadena es un palíndromo, False en caso contrario.
    """
    # Eliminamos espacios y convertimos a minúsculas para comparación
    cadena = cadena.replace(" ", "").lower()
    # Comparamos la cadena con su versión invertida
    return cadena == cadena[::-1]


cadena = input("Introduce una palabra o frase: ")
if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")




