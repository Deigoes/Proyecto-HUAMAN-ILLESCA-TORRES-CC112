'''Crear una lista dinámica (usando listas en Python) y añadir elementos de forma interactiva.'''
# Se define una función que permitirá añadir elementos a una lista de manera interactiva
def ListaDinamica():
    # Se crea una lista vacía
    Lista = []
    # Se genera un bucle
    while True:
        # Se solicita al usuario que ingrese un elemento o escriba 'salir' para terminar
        elemento = input("Introduzca un elemento para añadir a la lista o 'salir' para finalizar: ")
        # Se verifica si el usuario ha escrito 'salir'
        if elemento == 'salir':
            break  # Se sale del bucle
        # Se añade el elemento a la lista
        Lista.append(elemento)
        print("Elemento añadido")  # Se confirma que el elemento fue agregado
    return Lista  # Se devuelve la lista final

# Se llama a la función ListaDinamica y se almacena el resultado en ListaFinal
ListaFinal = ListaDinamica()
# Se imprime la lista completa
print(f"Lista completa: {ListaFinal}")