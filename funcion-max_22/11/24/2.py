#2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

print("El mayor es:", max_de_tres(numero1, numero2, numero3))
