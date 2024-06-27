'''Crear una función que cuente las vocales en una cadena.'''
# Se define una función que cuenta vocales en una cadena
def contaVocales(cadena):
    # Se define un string que contiene todas las vocales en minúsculas, mayúsculas y con tildes
    vocales = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    # Se inicializa un contador en 0
    contador = 0
    
    # Se recorre cada carácter de la cadena
    for caracter in cadena:
        # Si el carácter está en el string de vocales, se incrementa el contador
        if caracter in vocales:
            contador += 1
    
    # Se devuelve el total de vocales contadas
    return contador

# Se define una cadena para ejemplo
cadena = "HolA, ¿cÓmo estás?"

# Se calcula el número de vocales en la cadena
resultado = contaVocales(cadena)

# Se imprime el resultado obtenido
print(f"El número de vocales en la cadena es: {resultado}")