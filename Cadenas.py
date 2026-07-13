# Crear un programa que lea por teclado una cadena y un carácter, e inserte el carácter entre cada letra de la cadena.
# # Ej: separar y , debería devolver s,e,p,a,r,a,r
# cadena = input("Dime la cadena\n")
# caracter = input("Dime el carácter\n")
# print(caracter.join(cadena))
#
# Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:
#
# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
# Dicha cadena con la primera letra de cada palabra en mayúsculas.
# Por ejemplo, si recibe república argentina debe devolver República Argentina.
# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.

# cadena = input("Cadena: \n")
# lista = cadena.split(" ")
# for each in lista:
#     print(each[0].upper(), end ="")#el end se usa para que no haya salto de línea

# for each in lista:
#     print (each.capitalize(), end =" ")
#
# for each in lista:
#     if each.startswith("a") or each.startswith("A"):
#         print (each,end=",")
# print()#salto de línea en consola

# Escribir funciones que dadas dos cadenas de caracteres:
#
# Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.
# Devuelva la que sea anterior en orden alfabético. Por ejemplo, si recibe kde y gnome debe devolver gnome.

# cad1=input("Cadena 1:")
# cad2=input("Cadena 2:")
# if cad2 in cad1:
# 	print ("cad2 es subcadena de cad1")
# else:
# 	print ("cad2 no es subcadena de cad1")
#
# print(cad1 if cad1<cad2 else cad2)#en este caso > ordena por orden alfabetico
#
# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por
# pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
# nombre = input("Ingrese su nombre: ")
# numero = int(input("Ingrese su numero: "))
#
# print((nombre + "\n") * int(numero))

#
# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla
# el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras
# mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera

# nombre = input("Ingrese su nombre: ")
# print(nombre.upper())
# print(nombre.lower())
# print(nombre.title())#como el capitalize pero en todas las primeras letras de la cadena
#
#
# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
# muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es
# el número de letras que tienen el nombre.
# nombre = input("Introduce tu nombre: ")
# print(f"El nombre {nombre.lower()} tiene {len(nombre)} letras")
#
#
# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código
# del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número
# de teléfono sin el prefijo y la extensión.
# numero = input("Introduce un numero: ")
# print(numero[4:-3])
#
# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla
# la frase invertida.
# frase = input("Ingrese una frase: ")
# print(frase[::-1])
#
# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre
# por pantalla la misma frase pero con la vocal introducida en mayúscula.
# frase = input("Ingrese una frase: ")
# vocal = input("Ingrese una vocal: ")
# print(frase.replace(vocal, vocal.upper()))

#
#
# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro
# correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

# email = input("Introduce tu correo electrónico: ")
# print(email[:email.find('@')] + '@ceu.es')
# #
#
# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre
# por pantalla el número de euros y el número de céntimos del precio introducido.
# precio = input("Introduce el precio del producto con dos decimales:  ")
# print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
#
#
# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por
# pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día
# o el mes se introduzcan con un solo carácter.
# fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
# dia = fecha[:fecha.find('/')]
# mesaño = fecha[fecha.find('/')+1:]
# mes = mesaño[:mesaño.find('/')]
# año = mesaño[mesaño.find('/')+1:]
# print('Día', dia)
# print('Mes', mes)
# print('Año', año)
# #
#
# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
# y muestre por pantalla cada uno de los productos en una línea distinta.
#
# cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
# print(cesta.replace(',', '\n'))
# #
#
# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por
# pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

# producto = input('Introduce el nombre del producto: ')
# precio = float(input('Introduce el precio unitario: '))
# unidades = int(input('Introduce el número de unidades: '))
# print('{producto}: {unidades:3d} unidades x {precio:09.2f}€ = {total:011.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
#
# En dame_numero.py crea una función que pida un número por teclado y lo devuelva.
# En caso de no introducir un número captura la excepción y muestra un mensaje de error hasta que
# se introduzca un número válido. Usa parámetros por defecto.
# def numeropati(numerodefecto=1):
#     """Pide un número y lo devuelve. Absurdo, lo sé"""
#     while True:
#         try:
#             numero = input("Dame el puto número\n")
#             if numero == '':
#                 return numerodefecto
#             valor = int(numero)
#             return valor
#         except ValueError:
#             print("Eso no es un número pare mío")
#
# print (numeropati(""))
#
# En dame_numero_entero.py crea una función que pida un número entero por teclado y lo devuelva.
# En caso de no introducir un número entero captura la excepción y muestra un mensaje de error hasta que
# se introduzca un número entero válido.
# def dame_numero_entero(numero_entero=1):
#     while True:
#         try:
#             numero=input("Ingrese un numero entero: ")
#             entero=int(numero)
#             return entero
#         except ValueError:
#             print("Ingrese un numero entero valido")
# print(dame_numero_entero())
# #
#
# En dame_entero_positivo.py crea una función que pida un número entero positivo por teclado y lo devuelva.
# En caso de no introducir un número entero positivo captura la excepción y muestra un mensaje de error hasta
# que se introduzca un número entero positivo válido.
# def entero_positivo(numero = 1):
#     while True:
#         try:
#             numero = input("Dime el numero entero y positivo nunca negativo\n")
#             comprueba=int(numero)
#             if comprueba>0:
#                 return comprueba
#         except ValueError:
#             print("El número tiene que ser entero y positivo\n")
#
# print(entero_positivo())

#
#
# En dame_positivo.py crea una función que pida un número positivo por teclado y lo devuelva.
# En caso de no introducir un número positivo captura la excepción y muestra un mensaje de error hasta que se
#
#
# def dame_positivo(numero = 1):
#     while True:
#         try:
#             numero = input("Dame positivo: \n")
#             positivo = int(numero)
#             if positivo >0:
#                 return positivo
#             else:
#                 print("El número es negativo")
#         except ValueError:
#             print("Ingrese un numero valido")
#
# print(dame_positivo())
#
#
# En divide.pycrea una función que devuelva la división de dos valores. Lanza/captura todos los errores posibles,
# incluída la falta de parámetros. Usa el código que se adjunta y analiza qué ocurre al comentar los distintos
# bloques de except.
#
# def divide_numeros(dividendo, divisor):
#     """
#     Devuelve la división de dos valores
#
#     :param dividendo: dividendo
#     :param divisor: divisor
#     :return: cociente de dos valores
#     """
#     try:
#         return dividendo / divisor
#     except ZeroDivisionError:
#         return "Error: División por cero no permitida."
#     except TypeError:
#         return "Error: Ambos valores deben ser números."
#     except Exception as e:
#         return f"Error inesperado: {e}"
#
# print(divide_numeros(2,3))
