# # Ejercicio 19
# # Crea una función que reciba un nombre y lo salude.
# def saludar(nombre):
#     print(f"Hola, {nombre}.")
#
# saludar("Chris")
#
# #Ejercicio 20
# # Crea una función que reciba dos números y devuelva su suma.
#
# def sumar(a,b):
#     print(a+b)
#
# sumar(8,5)
#
# Ejercicio 21
# # Crea una función que reciba un número y devuelva True si es par y False si es impar.
# def esPar(numero):
#    if numero % 2 == 0:
#        return True
#    else:
#        return False
#
# print(esPar(88))
# print(esPar(77))

# Ejercicio 22
# # Crea una función que reciba una lista y devuelva el número más grande.
# def masGrande (lista):
#     return(max(lista))
#
# print(masGrande([1,2,3,4,5]))

# Crea un programa que:
# 1.
# Pida 5 números.
# 2.
# Los guarde en una lista.
# 3.
# Muestre:
# La suma total.
# # El número mayor.
# # Cuántos son pares.
#
# numero1 = int(input("Dame el numero 1\n"))
# numero2 = int(input("Dame el numero 2\n"))
# numero3 = int(input("Dame el numero 3\n"))
# numero4 = int(input("Dame el numero 4\n"))
# numero5 = int(input("Dame el numero 5\n"))
#
# lista = [numero1, numero2, numero3, numero4, numero5]
#
#  def sumar(lista):
#     return sum(lista)
#  print(sumar(lista))
#
#  def mayor(lista):
#      return max(lista)
# print(mayor(lista))
#
# def esPar(lista):
#     pares = []
#     for each in lista:
#         if each % 2 == 0:
#             pares.append(each)
#     return pares
#
# print(esPar(lista))

#Calcular la media
# lista = []
#
# while True:
#     entrada = input("Dame un número o escribe fin para terminar: ")
#
#     if entrada.lower() == "fin":
#         break
#
#     numero = int(entrada)
#     lista.append(numero)
#
# def sumar(lista):
#     return sum(lista)
# print(sumar(lista))
#
# def contar(lista):
#     return len(lista)
# print(contar(lista))
#
# def media(lista):
#     return sumar(lista) / contar(lista)
#
# print(media(lista))


#Invertir una cadena
# cadena = input ("Dime la cadena\n")
# cadenaInvertida = cadena[::-1]
# print(cadenaInvertida)