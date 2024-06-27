print("--FACTORIAL DE UN NUMERO--")
n = int(input("Digite un numero entero positivo: "))

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(f"El factorial de {n} es: {factorial(n)}")