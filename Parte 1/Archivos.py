'''Escribir y leer datos desde un archivo de texto.'''
# Se crea una lista de cadenas de texto que se desee escribir en un archivo
texto = ["Inicio", "Medio", "Final"]

# Se abre (o se crea si no existe) un archivo llamado 'archivo.txt' en modo escritura ('w')
with open('archivo.txt', 'w') as archivo:
    # Se itera sobre cada línea de texto en la lista 'texto'
    for linea in texto:
        # Se escribe cada línea en el archivo, añadiendo un salto de línea al final
        archivo.write(linea + '\n')

# Se abre el archivo 'archivo.txt' en modo lectura ('r')
with open('archivo.txt', 'r') as archivo:
    # Se leen todas las líneas del archivo y se almacenan en la lista 'informacion'
    informacion = archivo.readlines()

# Se itera sobre cada línea de la lista 'informacion'
for linea in informacion:
    # Se imprime cada línea, eliminando los saltos de línea al final con strip()
    print(linea.strip())