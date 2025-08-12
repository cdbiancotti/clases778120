'''
Unidad 7: Programación Orientada a Objetos II y Herencias
Repaso/consultas de la clase práctica en vivo anterior
Actividad: Trabajando con DrawIO

'''
'''

Repaso: Relación entre clases
Consigna:

¿Cómo explicarías los últimos print? ¿Qué se representa en el código de la siguiente slide?

Contesta mediante el chat de Zoom

Duración: 5 minutos
'''
'''

Repaso: Para pensar…
Consigna:

¿Qué creen que ocurre en este caso? Pista Atención a los

Contesta mediante el chat de Zoom.

Duración: 5 minutos
'''

'''
Crear una clase llamada Alumno, que posea como atributos de instancia el nombre y la nota del estudiante.
Como métodos propios de la clase, se deberán definir correspondientemente el constructor, 
el método imprimir y resultado.
Aclaración: Tanto los atributos como métodos, son de tipo públicos.
- El método imprimir, deberá mostrar por pantalla el nombre y la nota del estudiante.
 
- El método resultado, evalúa la nota correspondiente del estudiante. 
  Si el estudiante saca 5 o menos puntos desaprueba la materia, más de 5 puntos aprueba. 
  Tip: Para la realización de este apartado, es necesario trabajar con estructuras condicionales.


- Se deberá instanciar, al menos, dos objetos pertenecientes a la clase Alumno.
'''

# class Alumno:
    
#     def guardado_de_informacion(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota


# alumno1 = Alumno()

# alumno1.guardado_de_informacion('Pepe', 5) # guardado_de_informacion(alumno1, 'Pepe', 5)

# print(alumno1.nombre)


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


alumno1 = Alumno('Pepe', 5)
alumno2 = Alumno('Ricardo', 8)


print(alumno1.nombre)
alumno1.imprimir()
alumno1.resultado()

alumno1.__str__()

alumno2.imprimir()
alumno2.resultado()

listado_de_alumnos = [alumno1, alumno2]

for alumno in listado_de_alumnos:
    print(alumno)
    # alumno.imprimir()
    
    
str(alumno1)


'''

Ejemplo en vivo: Herencia
Consigna: Vamos a definir una clase padre Animal que tendrá todos los atributos y métodos genéricos que los animales pueden tener.

Repaso: Herencia múltiple
Consigna: ¿Qué diferencias se pueden detectar?

Contesta mediante el chat de Zoom

Duración: 5 minutos
'''
'''

Actividad: Herencia múltiple
Consigna: Crea una herencia múltiple, trabajando con Mamífero, Cetáceo, AnimalMarino.

Duración: 20 minutos
'''


HOLA SOY UNA PRUEBA PARA LA CLASE