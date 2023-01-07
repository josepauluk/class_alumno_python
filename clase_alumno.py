'''En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nota: {self.nota}')

    def resultado(self):
        if self.nota >= 6:
            print('Aprobado')
        else:
            print('Desaprobado')

alumno = Alumno('José', 7)
alumno.imprimir()
alumno.resultado()