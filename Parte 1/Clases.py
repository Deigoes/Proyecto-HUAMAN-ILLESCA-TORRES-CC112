'''Definir una clase Persona con atributos nombre y edad, y un método para mostrar estos datos.'''
# Se define la clase Persona
class Persona:
    # El método _init_ es el constructor de la clase y se llama al crear una nueva instancia
    def _init_(self, nombre, edad):
        # Se asigna los parámetros nombre y edad a los atributos de instancia
        self.nombre = nombre
        self.edad = edad

    # Se define un método para mostrar los datos de la persona
    def mostrarDatos(self):
        # Se imprimen los datos de la persona en formato Nombre: nombre, Edad: edad
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

# Se crea una instancia de la clase Persona como ejemplo
persona1 = Persona('Romina', 13)
# Se llama al método mostrarDatos para mostrar los datos de persona1
persona1.mostrarDatos()

# Se crea otra instancia de la clase Persona como segundo ejemplo
persona2 = Persona('Adrian', 18)
# Se llama al método mostrarDatos para mostrar los datos de persona2
persona2.mostrarDatos()