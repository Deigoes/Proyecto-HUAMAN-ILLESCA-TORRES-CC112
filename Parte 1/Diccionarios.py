'''Escribir una función que ordene una lista de diccionarios por un valor específico.'''
# Se define una función que ordenará una lista de diccionarios por una clave específica
def ordenarLista(lista, clave):
    # Se utiliza sorted() para ordenar la lista de diccionarios
    # key=lambda diccionario: diccionario[clave] define el valor en que se ordene
    return sorted(lista, key=lambda diccionario: diccionario[clave])

# Se crea una lista de diccionarios para usar como ejemplo
listaDeDiccionarios = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'Ana', 'edad': 22},
    {'nombre': 'Pedro', 'edad': 30},
    {'nombre': 'Marta', 'edad': 20}
]

# Se ordena la lista de diccionarios por el valor 'edad'
listaOrdenada = ordenarLista(listaDeDiccionarios, 'edad')
# Se imprime la lista ordenada
print(listaOrdenada)

# Se ordena la misma lista de diccionarios por el valor 'nombre'
listaOrdenada = ordenarLista(listaDeDiccionarios, 'nombre')
# Se imprime la lista ordenada
print(listaOrdenada)