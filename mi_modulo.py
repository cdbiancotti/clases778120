class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def __str__(self):
        return f'Soy el alumno {self.nombre}'
        
    def imprimir(self):
        print(f"Nombre: {self.nombre} - Nota: {self.nota}")
        
    def resultado(self):
        if self.nota <= 5:
            print('Alumno desaprobado.')
            return
        print('Alumno aprobado.')         
        

edad = 25    


def suma(num1, num2):
    return num1 + num2
