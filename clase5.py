'''
Actividad: Función año bisiesto

Realizar una función llamada año_bisiesto:
- Recibirá un año por parámetro
- Imprimirá “El año <numero> es bisiesto” si el año es bisiesto
- Imprimirá “El año <numero> no es bisiesto” si el año no es bisiesto
- Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

Información a tener en cuenta:
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, 
aunque los múltiplos de 400 sí. 
Estos son algunos ejemplos de posibles respuestas: 
2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
'''


# def anio_bisiesto(anio: str = None):
    
#     valores_numericos: str = '0123456789'
#     anio_ingresado_string = str(anio)
    
#     #
    
#     # anio_ingresado_string.isdecimal()
    
#     #
#     for caracter in anio_ingresado_string:
#         if caracter not in valores_numericos:
#             print('Ingresa un valor numerico')
#             return

#     anio_entero = int(anio_ingresado_string)
    
#     if anio_entero % 4 == 0 and (anio_entero % 100 != 0 or anio_entero % 400 == 0):
#         print(f'El anio {anio_entero} es bisiesto')
#         return
    
#     print(f'El anio {anio_entero} no es bisiesto')
    
# anio_bisiesto(2012)
# anio_bisiesto(2010)
# anio_bisiesto(2000)
# anio_bisiesto(1900)
# anio_bisiesto('2012')
# anio_bisiesto('2asd')
# anio_bisiesto('2.64')


'''
Actividad: ¡Funciones!
Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.
'''



'''
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.
'''



'''
Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
- Si el primer número es mayor que el segundo, debe devolver 1.
- Si el primer número es menor que el segundo, debe devolver -1.
- Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
'''



'''
Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:

🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24
'''


'''
Realiza una función llamada recortar() que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 

La función tendrá que cumplir lo siguiente:
- Devolver el límite inferior si el número es menor que éste
- Devolver el límite superior si el número es mayor que éste.
- Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10
'''



#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################


'''
Unidad 5: Funciones en Python
Repaso/consultas de la clase práctica en vivo anterior
Repaso: Funciones
Consigna:

Si las variables creadas en una función, solo existen dentro de esa función ¿Cómo explicarías esto?
'''

# variable_test = 10 
# def test(): 
#     # global variable_test
#     print(variable_test) 

# test()

'''
Contesta mediante el chat de Zoom
Duración: 5 minutos
'''



'''
Actividad: ¿Verdadero o falso?
'''

# def suma(num1, num2):
#     return num1 + num2

# r = suma(7, 5)

'''
Consigna: ¿Qué ocurriría si lo hiciéramos al revés?

r = suma(5, 7)

¿Verdadero o falso? Contesta mediante el chat de Zoom
Duración: 5 minutos
'''

# def resta(num1, num2):
#     return num1 - num2

# r1 = resta(7, 5)
# r2 = resta(num2=5, num1=7)
# r3 = resta(5, 7)
# print(r1)
# print(r2)
# print(r3)


# def funcion(var1, var2, var3, var4, var5):
#     ...
    
# funcion(1, 2, 3, var4=4, var5=5)
# funcion(1, 2, 3, var2=37, var5=5)

'''
Actividad: Welcome
Consigna: Escribir una función a la que se le pase una cadena del nombre 
de una ciudad y muestre por pantalla el saludo ¡hola bienvenidx a !.

Duración: 10 minutos
'''

# def bienvenida(ciudad):
#     print(f'¡hola bienvenidx a {ciudad}!')
    
# bienvenida('Rosario')

'''
Actividad: Media
Consigna: Escribir una función que reciba una muestra de números en una lista y devuelva su media.

Duración: 10 minutos
'''



'''
Actividad: es_multiplo
Consigna: Crea un programa que le pida dos números enteros al usuario y diga por consola, 
si alguno de ellos es múltiplo del otro. 
La función debe llamarse es_multiplo(). 
Duración: 10 minutos
'''

# def es_multiplo(num1, num2):
#     if num1 % num2 == 0:
#         print(f'{num1} es multiplo de {num2}')
#     elif num2 % num1 == 0:
#         print(f'{num2} es multiplo de {num1}')
#     else:
#          print('No son multiplos entre si...')
    
    
# var1 = int(input('Ingrese un numero: '))
# var2 = int(input('Ingrese otro numero: '))

# es_multiplo(var1, var2)


'''
Repaso: Argumentos y parámetros
Consigna:

¿Cuál es la diferencia entre los parámetros y argumentos?

Contesta mediante el chat de Zoom
Duración: 5 minutos
'''



'''
Repaso: Argumentos y parámetros
Consigna: 
¿Es posible que de alguna forma le digamos a Python cuándo queremos 
pasar un argumento por referencia o por valor?

Contesta mediante el chat de Zoom
Duración: 5 minutos
'''



'''
Actividad: Conversiones tipos de datos
Consigna: Pasaremos de milímetros a metros según el parámetro de la función.
Realiza una función que, dependiendo de los parámetros que reciba, convierta a milímetros o a metros.

1- Si recibe un argumento, supone que son milímetros y convierte a metros, centímetros y milímetros.
2- Si recibe 3 argumentos, supone que son metros, centímetros y milímetros y los convierte a milímetros.

Duración: 15 minutos
'''
# def conversor(*param):
#     ...

# def conversor(param1, param2 = None, param3 = None):
    
#     if param2 is not None and param3 is not None:
#         # resolver el punto 2
#         mm = param1 * 1000 + param2 * 10 + param3
#         print(f'Cantidad de Milimtetros: {mm}')
#     elif param2 or param3:
#         print(
#             'Falta o sobre uno de los 3 valores a pasar'
#             ', se requiere un valor para `milímetros a metros'
#             ', centímetros y milímetros` y 3 valores para `metros'
#             ', centímetros y milímetros a milímetros`'
#         )
#     else:
#         # resolver el punto 1
#         mts = param1 // 1000
#         mm = param1 % 1000
#         cm = mm // 10
#         mm = mm % 10
#         print(f'Cantidad de Metros: {mts} - Centimetros: {cm}, Milimtetros: {mm}')


# conversor(3456)
# conversor(3456,1)
# conversor(4,1212,123)
# conversor(0,0,0)
# conversor(0,0,123)
# conversor(4,0,0)
# conversor(0,1212,0)
# conversor(0,1212,123)
# conversor(4,0,123)
# conversor(4,1212,0)

#############################################################################################
#############################################################################################


# def conversor(param1, param2 = None, param3 = None):
    
#     if param2 is not None and param3 is not None:
#         # resolver el punto 2
#         mm = param1 * 1000 + param2 * 10 + param3
#         print(f'Cantidad de Milimtetros: {mm}')
#     elif param2 or param3:
#         print(
#             'Falta o sobre uno de los 3 valores a pasar'
#             ', se requiere un valor para `milímetros a metros'
#             ', centímetros y milímetros` y 3 valores para `metros'
#             ', centímetros y milímetros a milímetros`'
#         )
#     else:
#         # resolver el punto 1
#         mts = param1 // 1000
#         mm = param1 % 1000
#         cm = mm // 10
#         mm = mm % 10
#         print(f'Cantidad de Metros: {mts} - Centimetros: {cm}, Milimtetros: {mm}')


# dato_ingresado = input('Ingrese `mm` o `mts, cm y mm` separados por un espacio para hacer la conversion: ')
# listado_de_datos = dato_ingresado.split()

# try:
#     if len(listado_de_datos) == 1:
#         conversor(int(listado_de_datos[0]))
#     elif len(listado_de_datos) == 3:
#         conversor(int(listado_de_datos[0]), int(listado_de_datos[1]), int(listado_de_datos[2]))
# except ValueError:
#     print('Ingresaste un valor incorrecto para las conversiones.')
# except Exception as error:
#     print(f'Hubo un error en la ejecucion de la conversion. Tipo de error: {type(error).__name__}')

#############################################################################################
#############################################################################################
#############################################################################################

'''
EXTRA

Pasar el ejemplo de la calculadora de la clase 4 a una implementacion con funciones
'''

