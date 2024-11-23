#1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(a, b):
    if a > b:
        return a
    else:
        return b

# Ejemplo de uso
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

print("El mayor es:", max(numero1, numero2))
