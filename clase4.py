'''
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.
'''

# texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

# listado = texto.split('&')
# listado[0] += '..'

# # v1
# # listado[0] = listado[0][0].upper() + listado[0][1:]
# # listado[1] = listado[1][0].upper() + listado[1][1:]
# # listado[2] = listado[2][0].upper() + listado[2][1:]
# # listado[3] = listado[3][0].upper() + listado[3][1:]

# # v2
# listado_final = []
# for oracion in listado:
#     # listado_final += (oracion[0].upper() + oracion[1:])
#     listado_final.append(oracion[0].upper() + oracion[1:])

# resultado = '.\n- '.join(listado_final)

# resultado += '.'

# print(resultado)

#################################################################################
#################################################################################

'''
1. Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
- En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''

num1 = float(input('Ingrese el primer valor'))
num2 = float(input('Ingrese el segundo valor'))

# condicion = True
# while condicion:
while True:
    opcion = input('Ingrese 1. Suma 2. Resta 3. Multiplicacion 4. Salir')
        
    if opcion == '1':
        print(num1 + num2)
    elif opcion == '2':
        print(num1 - num2)
    elif opcion == '3':
        print(num1 * num2)
    elif opcion == '4':
        print('Nos vemos la proxima...')
        break
        # condicion = False
    else:
        print('Opcion invalida')

# if opcion_elegida:

# elif condicion

# while condicion


# condicion
# - tipos de datos: logico, 0 - 1
# bool(cualquier cosa que le pasemos)
# bool(condicion)
# print(bool(0))
# print(bool(1))
# print(bool(15))
# print(bool(4.5))
# print(bool(-4.5))
# print(bool(' '))

# Falsy values
# print(bool(0))
# print(bool(''))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(set()))
# print(bool(None))

#################################################################################
#################################################################################

'''
Actividad: Crédito Bancario
Consigna:
Para aprobar un crédito, el cliente debe ser mayor de edad. 
Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y 
un ingreso mayor a 2500 dólares.  
En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. 
Si no cumple ninguna de las condiciones, no se aprueba el crédito

Datos iniciales
edad = 15
antigüedad = 10
ingreso = 1500
'''

# edad = 15 # input
# antiguedad = 10 # input
# ingreso = 1500 # input

# if edad > 17 and (antiguedad >=3 and ingreso > 2500 or ingreso >= 4000):
#     print('Credito aprobado')



# edad = 15 # input
# if edad > 17:
#     ingreso = 1500 # input
#     if ingreso >= 4000:
#         print('Credito aprobado')
#     else:
#         antiguedad = 10 # input
#         if antiguedad >=3 and ingreso > 2500:
#             print('Credito aprobado')




#################################################################################
#################################################################################
'''
Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado.
Importante: Para los años que no pertenezcan a ninguna generación, 
se deberá colocar: “No existe generación asociada”
1920-1945 Silenciosa
1946-1964 Baby Boomer
1965-1979 X
1980-2000 Y
2001-2010 Z
'''

# anio = int(input('Ingrese el anio de nacimineto: '))

# if 1920 <= anio <= 1945:
#     print('Silenciosa')
# elif 1946 <= anio < 1964:
#     print('Baby Boomer')
# elif 1965 <= anio <= 1979:
#     print('X')
# elif 1980 <= anio <= 2000:
#     print('Y')
# elif 2001 <= anio <= 2010:
#     print('Z')
# else:
#     print('No existe generación asociada')


#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################