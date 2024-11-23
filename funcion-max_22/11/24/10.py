#10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
#Ejemplo: procedimiento([4, 9, 7]) 

def procedimiento(lista):
    """
    Imprime un histograma en la pantalla, donde cada número de la lista se representa
    por una secuencia de asteriscos '*' correspondientes a su valor.

    Args:
        lista (list): Una lista de números enteros.
    """
    for numero in lista:
        # Imprime una línea de asteriscos según el valor del número
        print('*' * numero)


numeros = [4, 9, 7]
procedimiento(numeros)




