#9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(n, caracter):
    """
    Genera una cadena compuesta por un carácter repetido n veces.

    Args:
        n (int): El número de veces que se repetirá el carácter.
        caracter (str): El carácter a repetir.

    Returns:
        str: Una cadena con el carácter repetido n veces.
    """
    resultado = ""
    for _ in range(n):  # Repite n veces
        resultado += caracter
    return resultado


n = int(input("Introduce un número entero (n): "))
caracter = input("Introduce un carácter: ")

if len(caracter) == 1:  # Verifica que sea un único carácter
    print("Resultado:", generar_n_caracteres(n, caracter))
else:
    print("Por favor, introduce solo un carácter.")






