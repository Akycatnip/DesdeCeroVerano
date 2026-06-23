# def saludar(nombre, mensaje="¡Hola!"):
#     print(f"{mensaje}, {nombre}!")
#
# saludar("Alice")# Salida: ¡Hola!, Alice!)
# saludar("Bob", "Buenos días")  # Salida: Buenos días, Bob!
# saludar("","q pasa")

#diccionarios
# def personas(*args, **kwargs):
#     """imprime los datos con(kwargs) o sin(args) etiquetas"""
#     print(args)
#     print(kwargs)
#
# personas("Marta", 42, anime ="One Piece", bias ="Nami")
# personas("Chris",33, anime= "One Piece")
# personas("Maicamen",27, anime = "Naruto", bias ="Trafalgar")
# personas("Su", 33, "rubia", música="newbie in kpop")

# def ateez(*args,**kwargs):
#     """miembros de Ateez"""
#     print(args)
#     print(kwargs)
# ateez("Seonghwa", 1998, posición="leader")
# ateez("Hongjoong", 1998)
# ateez("Yunho", 1999)
# ateez("Yeosang", 1999)
# ateez("San", 1999)
# ateez("Wooyoung", 1999)
# ateez("Jongho", 1999, "maknae")

# Define una función llamada es_par que tome un número entero como parámetro y devuelva True si el número es par
# y False si es impar. Invócala con diferentes números y muestra los resultados.

# def espar(numero):
#     """pa saber si es par o no"""
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
# print(espar(1))
# print(espar(442))
# print(espar(365))
# print(espar(488))
#
#
# Crea una función llamada factorial que calcule el factorial de un número entero no negativo.
# Utiliza un bucle para calcular el factorial y devuelve el resultado. Prueba la función con varios valores.
#
# def factorial(numero):
#     """es el resultado de multiplicar un número entero positivo
#      por todos los enteros positivos menores que él"""
#     if numero == 0:
#         return 1
#     else:
#         return numero * factorial(numero - 1)
# print(factorial(5))
# print(factorial(50))
#
# Define una función llamada fibonacci que genere una lista con los primeros n números de la secuencia de Fibonacci.
# La función debe tomar un parámetro n y devolver la lista correspondiente.
# Invoca la función con diferentes valores de n y muestra los resultados.
#
# def fibonacci(n):
#     lista = []
#
#     for i in range(n):
#         if i == 0:
#             lista.append(0)
#         elif i == 1:
#             lista.append(1)
#         else:
#             lista.append(lista[i - 1] + lista[i - 2])
#
#     return lista
#
# print(fibonacci(10))
#
#
# Crea una función llamada es_palindromo que verifique si una cadena de texto es un palíndromo
# (se lee igual de izquierda a derecha que de derecha a izquierda).
# La función debe ignorar espacios y mayúsculas/minúsculas. Prueba la función con varias cadenas
#
# def esPalindromo(palabra):
#     palabra = palabra.lower()
#     palabra = palabra.strip()
#     if palabra == palabra[::-1]:
#         return True
#     else:
#         return False
# print(esPalindromo("ananana"))
#
#
# Define una función llamada calcular_area_circulo que tome el radio de un círculo como parámetro
# y devuelva el área del círculo utilizando la fórmula área = π * radio^2.
# Utiliza la constante math.pi para obtener el valor de π.
# Invoca la función con diferentes radios y muestra los resultados.
# import math
# def calcular_area_circulo(radio):
#     area = math.pi*radio**2
#     return area
# print(calcular_area_circulo(5))
# print(calcular_area_circulo(10))
#
#
# Crea una función llamada contar_vocales que tome una cadena de texto como parámetro
# y devuelva el número de vocales presentes en la cadena. La función debe contar tanto vocales mayúsculas
# como minúsculas. Prueba la función con varias cadenas.
# def contar_vocales(texto):
#     vocales = ['a', 'e', 'i', 'o', 'u']
#     texto=texto.lower()
#     totalvocales=0
#     for vocal in vocales:
#             totalvocales += texto.count(vocal)
#     return totalvocales
# print(contar_vocales("ujervifowjfni2penfuo2b4eufoni2p34nhuo2bn fnieofh32iniewp4fg3ovrfegv"))
#
#
# Define una función llamada ordenar_lista que tome una lista de números como parámetro y
# devuelva una nueva lista con los números ordenados de menor a mayor. Utiliza el método de ordenación
# incorporado de Python. Invoca la función con diferentes listas y muestra los resultados.

# def ordenar_lista(lista):
#     """sorted ordena los números de menor a mayor"""
#     ordenada = sorted(lista)
#     return ordenada
# print(ordenar_lista([2,5,8,1,22,99]))
# print(ordenar_lista([1,-1,-2,0]))
#
#
# Crea un programa que muestre el menú con cinco opciones (del 1 al 5): sumar, restar, multiplicar,
# dividir, y salir. El usuario debe poder seleccionar una opción y proporcionar los números necesarios
# para realizar la operación. Muestra el resultado de la operación hasta que se seleccione
# la opción de salir.
# Evita el uso de variables globales y utiliza funciones para cada operación.
# Evita los errores en la medida de lo posible.

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplica")
    print("4. Divide")
    print("5. Salir")

    opcion = input("Elige la opción deseada: ")

    if opcion == "5":
        print("Saliendo...")
        break

    numeros = []

    while True:
        entrada = input("Dame un número o escribe 'fin' para terminar: ")

        if entrada == "fin":
            break

        numero = int(entrada)
        numeros.append(numero)

    if opcion == "1":
        def suma:




    elif opcion == "2":
        print("Resultado:", numeros[0]-numeros[1])

    elif opcion == "3":
        print("Resultado", numeros[0]*numeros[1])

    elif opcion == "4":
        print("Resultado:", numeros[0]/numeros[1])
