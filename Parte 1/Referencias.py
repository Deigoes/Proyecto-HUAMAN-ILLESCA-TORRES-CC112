'''Explicar cómo funcionan las referencias en Python y crear una función que demuestre la mutabilidad de las listas.'''
# Se define una función para demostrar la mutabilidad de las listas
def Mutabilidad(lista):
    # Se define la variable listaMutada igual al parámetro (lista)
    listaMutada = lista
    # Se imprime listaMutada
    print("Lista original dentro de la función:", listaMutada)
    # Se modifica, agregando un nuevo elemento
    listaMutada.append("Mario")
    # Se imprime listaMutada modificada
    print("Lista modificada dentro de la función:", listaMutada)
# Se crea una lista a usar de ejemplo
listaOriginal = ["Renzo", "Juan", "Pedro"]
# Se imprime la lista original
print("Lista antes de llamar a la función:", listaOriginal)
# Se llama a la función 
Mutabilidad(listaOriginal)
# Se imprime la lista luego de ser modificada por la función 
print("Lista después de llamar a la función:", listaOriginal)