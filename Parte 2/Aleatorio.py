'''Desarrollar un juego en el que el programa elija un número aleatorio y el usuario intente adivinarlo.'''
# Se agrega la librería random para generar números aleatorios
import random

# Se define la función del juego
def juegoBuscaNumero():
    # Se elige un número aleatorio entre 1 y 100
    numeroSecreto = random.randint(1, 100)
    # Se define el número de intentos permitidos
    intentos = 5
    
    # Se imprimen mensajes de bienvenida e instrucciones
    print("¡Bienvenido al juego de busca numero!")
    print("Se ha elegido un número entre 1 y 100. ¡Intenta adivinarlo!")
    print("Tienes 5 intentos para encontrarlo.")
    
    # Se crea el bucle principal del juego
    while True:
        # Se solicita al usuario que introduzca su suposición
        numero = input("Introduce tu suposición: ")

        # Se verifica si la entrada es un número
        if numero.isdigit():
            # Se convierte la entrada a un entero
            numero = int(numero)
            # Se reduce el número de intentos restantes
            intentos = intentos - 1
            
            # Se verifica si aún quedan intentos
            if intentos > 0:
                
                # Se compara la suposición del usuario con el número secreto
                if numero < numeroSecreto:
                    print("Demasiado bajo. Intenta de nuevo.")
                    print(f"Te quedan {intentos} intentos.")
                elif numero > numeroSecreto:
                    print("Demasiado alto. Intenta de nuevo.")
                    print(f"Te quedan {intentos} intentos.")
                else:
                    # Si el usuario adivina el número, se imprime un mensaje de felicitación y se sale del bucle
                    print(f"¡Felicidades! Adivinaste el número en {5 - intentos} intentos.")
                    break
                
            else:
                # Si el usuario se queda sin intentos, se imprime un mensaje notificándolo junto con el número secreto
                print("¡Ups! Te has quedado sin intentos. ¡Suerte para la próxima!")
                print(f"El número secreto era {numeroSecreto}.")
                break
                
        else:
            # Si la entrada no es válida, se solicita un número válido
            print("Por favor, introduce un número válido.")

# Se llama a la función para iniciar el juego
juegoBuscaNumero()