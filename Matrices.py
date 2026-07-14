# # matriz = [[1,2],
# #           [3,4]]
# # for i in range(len(matriz)):
# #     print(matriz[i][-1])
# m1 = [[1,2,3],
#       [4,5,6],
#       [7,8,9]]
# m2 = [[1,2,3],
#       [4,5,6],
#       [7,8,9]]
# resultado = [[m1[i][j] + m2[i][j] for j in range(3)] for i in range(3)]
#
# print(resultado)
#
# # Crea una aplicación que realice operaciones básicas de matrices en python.
# #
# # Una matriz puede:
# #
# # Sumarse: ambas tienen que tener las mismas dimensiones (a x b, axb)
# # Restarse: ambas tienen que tener las mismas dimensiones (axb, axb)
# # Multiplicarse: tienen que coincidir  las dimensiones  centrales (axb, bxc)
# # ...
# # Requisitos de la aplicación:
# #
# # Crea una clase Matriz de enteros.
# # Lanza la excepción MatrizError en caso de ser necesario.
# # Diseña una estructura donde almacenar las matrices resultantes. Podrán mostrarse y reutilizarse.
# # Usa la clase utiles/menu para las siguientes opciones:
# # Crear una matriz:
# # De números aleatorios
# # De 0
# # De números desde teclado
# # Matriz negativa
# # Sumar dos matrices
# # Restar dos matrices
# # Trasponer matriz
#
# def crear_matriz():
#     tamano = int(input("Introduce el tamaño de la matriz: "))
#     matriz = []
#
#     for i in range(tamano):
#         fila = input(f"Introduce los números de la fila {i + 1}, separados por espacios: ")
#         fila = [int(numero) for numero in fila.split()]
#         matriz.append(fila)
#
#     return matriz
#
#
# m1 = crear_matriz()
# print(m1)

#DICCIONARIOS

import random

def crear_salarios_aleatorios(n):
    salarios = {}

    for i in range(1, n + 1):
        salarios[f"empleado{i}"] = random.randint(1000, 3000)

    return salarios


def suma_salarios(salarios):
    suma = 0

    for salario in salarios.values():
        suma += salario

    return suma


# Diccionario inicial con 5 salarios aleatorios
salarios = crear_salarios_aleatorios(5)

print(salarios)
print("Suma de salarios:", suma_salarios(salarios))
