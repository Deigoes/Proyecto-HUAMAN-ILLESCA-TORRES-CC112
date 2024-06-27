'''Implementar una función recursiva para encontrar el máximo común divisor (MCD) de dos números.'''
#Se define la función recursiva para calcular el MCD de dos números 
def MCDRecur(a, b):
    #Se identifica el menor y mayor valor de los números 
    menor = min(a,b)
    mayor = max(a, b)
    #Si el mayor es divisible por el menor, el MCD será el menor número 
    if mayor%menor == 0:
        return menor
    #Se calcula el resto de la división del mayor con el menor
    resto = mayor%menor
    #Se llama a la función de forma recursiva con el menor y el resto
    return MCDRecur(menor, resto)
#Se definen dos números para ejemplo
num1 = 51
num2 = 123
#Se calcula el MCD de estos dos
resultado = MCDRecur(num1, num2)
#Se imprime el resultado obtenido
print(f"El MCD de {num1} y {num2} es: {resultado}")