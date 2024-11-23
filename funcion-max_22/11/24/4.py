#4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def es_vocal(caracter):
    """
    Verifica si un carácter es una vocal.

    Args:
        caracter (str): El carácter a verificar. Debe ser una sola letra.

    Returns:
        bool: True si el carácter es una vocal, False en caso contrario.
    """
    # Convertimos a minúscula para ignorar mayúsculas y comparamos con las vocales
    return caracter.lower() in 'aeiou'

# Ejemplo de uso
caracter = input("Introduce un carácter: ")

if len(caracter) == 1:  # Verifica que sea un único carácter
    print("¿Es vocal?:", es_vocal(caracter))
else:
    print("Por favor, introduce solo un carácter.")
