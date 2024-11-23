#5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
#  Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(lista):
    """
    Suma todos los números en una lista.

    Args:
        lista (list): Una lista de números.

    Returns:
        int o float: La suma de todos los números en la lista.
    """
    total = 0
    for numero in lista:
        total += numero
    return total

def multip(lista):
    """
    Multiplica todos los números en una lista.

    Args:
        lista (list): Una lista de números.

    Returns:
        int o float: El producto de todos los números en la lista.
    """
    total = 1
    for numero in lista:
        total *= numero
    return total


numeros = [1, 2, 3, 4]
print("La suma de los números es:", sum(numeros))  # Debería imprimir 10
print("El producto de los números es:", multip(numeros))  # Debería imprimir 24








