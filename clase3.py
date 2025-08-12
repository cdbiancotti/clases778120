'''
Actividad: Expresiones anidadas
Consigna: Crear una variable que almacene si se cumplen todas las condiciones.
A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable 
que almacene si se cumplen todas las siguientes condiciones, encadenando 
operadores lógicos en una sola línea:

- NOMBRE sea diferente de cuatro asteriscos “****”
- EDAD sea mayor que 5 y a su vez menor que 20
- Que la longitud de NOMBRE sea mayor o igual a 4 pero a la vez menor que 8
- EDAD multiplicada por 3 sea mayor que 35

Desde un input conseguir las variables:
nombre = INPUT!!!
edad = INPUT!!!!
'''

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# resultado = nombre != "****" and 5 < edad < 20 and 4 <= len(nombre) < 8 and edad * 3 > 35

# print("Los datos cumplen las condiciones:", resultado)

######################################################################################
######################################################################################
######################################################################################
######################################################################################

'''
Actividad: Colecciones 1
Consigna:

Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:
gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista
Transforma el texto en:

Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.

Lo único prohibido es modificar directamente el texto
'''

# v1
# cadena = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
# cadena_nueva = cadena.split("&")
# # print(cadena_nueva)
# linea1 = cadena_nueva[0].capitalize()
# print(linea1 + "...")
# linea2 = cadena_nueva[1].capitalize()
# print("- " + linea2)
# linea3 = cadena_nueva[2].capitalize()
# print("- " + linea3)
# linea4 = cadena_nueva[3].capitalize()
# print("- " + linea4)

# v2
# texto_original="gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
# texto_limpio = texto_original.replace("&","\n")
# lineas = texto_limpio.split("\n")
# lineas_mayusculas = [linea.capitalize() for linea in lineas]
# texto_final = "\n".join(lineas_mayusculas)
# print(texto_final)

# v3
# frase = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
# frase1 = frase[0:22]
# frase1 = frase1.replace("&", "...")
# #- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
# frase2 = frase[22:79]
# frase2 = frase2.replace("&", ".")
# #- Dos pies le corrigió Troop.
# frase3 = frase[79:100]
# #frase2 = frase2.replace("&", ".")

# print(frase1.capitalize())
# print(frase2.capitalize())
# print(frase3.capitalize())

# v4
# texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
# frases = texto.split("&")
# resultado = "\n".join(frases)
# print(resultado)

# Mix

'''
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.
'''

texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

listado = texto.split('&')
listado[0] += '..'

listado[0] = listado[0][0].upper() + listado[0][1:]
listado[1] = listado[1][0].upper() + listado[1][1:]
listado[2] = listado[2][0].upper() + listado[2][1:]
listado[3] = listado[3][0].upper() + listado[3][1:]

resultado = '.\n- '.join(listado)

resultado += '.'

print(resultado)


######################################################################################
######################################################################################
######################################################################################
######################################################################################