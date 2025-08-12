
# Trabajando con variables podriamos guardar datos sueltos como los siguientes y mostrarlos
nombre = 'Juan'
edad = 26

print(nombre)
print(edad)

# Pero para crear mas cantidad con lo que sabemos tendrimos un monton de variables
# nombre y edad, ademas de que no se relacionan entre si mas que por algo que
# pongamos en el nombre de la variable

nombre1 = 'Juan'
edad1 = 26
nombre2 = 'Pepe'
edad2 = 21

print(nombre1)
print(edad1)
print(nombre2)
print(edad2)

# entonces podriamos usar diccionarios y agruparlos un poco mas
persona1 = {
    'nombre': 'Juan',
    'edad': 26
}
persona2 = {
    'nombre': 'Pepe',
    'edad': 21
}

print(persona1['nombre'])
print(persona1['edad'])
print(persona2['nombre'])
print(persona2['edad'])

# Pero si tiene mas datos o tenemos que crear varias personas mas serian un monton
# de lineas para cada persona. Y aca entra una clase (por lo menos un ejemplo
# simple y basico de mejora en relacion a todo lo que nos brindan las 56075)

class Persona:
    """
    Esta es una clase donde se agregan todos los datos
    respecto a una persona
    """
    def __init__(self, nombre, edad):
        # Todo lo que definamos en __init__ se corre
        # al crear una instancia de la clase
        self.nombre = nombre
        self.edad = edad

#El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.
#Link de Interes: https://ejemplos.net/que-significa-self-en-python/

#Creamos un objeto persona1 que es una instancia de la clase Persona
persona1 = Persona("Juan", 26)

#Vemos el tipo de objeto que es persona1
type(persona1)

# Y si queremos crear a Pepe solo hariamos lo siguiente
persona2 = Persona("pepe", 21)

# Para acceder a los datos cambia de como lo haciamos con dicc
print(persona1.nombre) #Le pedimos a persona1 su nombre
print(persona1.edad) #Le pedimos a persona1 su edad
print(persona2.nombre) #Le pedimos a p2 su nombre
print(persona2.edad) #Le pedimos a p2 su edad