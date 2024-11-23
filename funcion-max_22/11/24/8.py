#8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado

def superposicion(lista1, lista2):
    """
    Verifica si dos listas tienen al menos un elemento en común.

    Args:
        lista1 (list): La primera lista.
        lista2 (list): La segunda lista.

    Returns:
        bool: True si hay al menos un elemento en común, False en caso contrario.
    """
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True  # Se encontró un elemento común
    return False  # No se encontraron elementos comunes

# Ejemplo de uso
lista1 = input("Introduce elementos de la primera lista separados por comas: ").split(',')
lista2 = input("Introduce elementos de la segunda lista separados por comas: ").split(',')

if superposicion(lista1, lista2):
    print("Las listas tienen al menos un elemento en común.")
else:
    print("Las listas no tienen elementos en común.")




