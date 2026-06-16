# #Crea una variable con tu nombre y otra con tu edad. Muestra ambas por pantalla.
# nombre = "Marta"
# edad = 42
# print("Mi nombre es:",nombre, "y tengo", edad ,"años")
#
# #Pide al usuario su nombre mediante input() y salúdalo
#
# tuNombre= input("Cómo te llamas?\n")
# print("Hola",tuNombre,"!")
#
# #Pide dos números y muestra su suma.
#
# numero1=int (input("Dame el primer número.\n"))
# numero2=int (input("Dame el segundo número.\n"))
# suma = print("La suma de los dos es: ",(numero1+numero2))

# #Pide un número e indica si es positivo, negativo o cero.
# numero = int(input("Dame un número.\n"))
# if numero > 0:
#     print("Es positivo")
# elif numero == 0:
#     print("Es cero")
# else:
#     print("Es negativo")

# #Pide la edad de una persona e indica si es mayor de edad.
#
# edad = int(input("¿Cuántos años tienes?\n"))
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Fuera de aquí enano!")
#
# #Pide dos números e indica cuál es mayor.
#
# numero1= int(input("Dime el primer numero"))
# numero2= int(input("Dime el segundo numero"))
# if numero1 > numero2:
#     print(f"{numero1} es mayor que {numero2}")
# elif numero1==numero2:
#     print(f"{numero2} es igual a {numero1}")
# else:
#     print(f"{numero2} es mayor que {numero1}")

#Muestra los números del 1 al 10 usando un bucle.
#
# numero = 1
# for numero in range(0,10):
#     print(numero+1)

#Muestra los números pares entre 1 y 20.
#
# for numero in range(1,21):
#     if(numero%2==0):
#         print(numero)
#
# #Pide un número y muestra su tabla de multiplicar.
#
# numero = int(input("Dame un numero:\n "))
# for i in range(0,11):
#     print(numero*i)
#
# #Calcula la suma de los números del 1 al 100.
# suma =0
# for i in range(0,101):
#     suma +=i
#     print(suma)

# #Cuenta cuántos números pares hay entre 1 y 100.
# contador =0
# for i in range(1,101):
#     if i%2==0:
#         contador +=1
# print(contador)

# #Pide 5 números al usuario y muestra cuál es el mayor.
#
# numero1 = int(input("Dame el primer numero: "))
# numero2 = int(input("Dame el segundo numero: "))
# numero3 = int(input("Dame el tercer numero: "))
# numero4 = int(input("Dame el cuarto numero: "))
# numero5 = int(input("Dame el quinto numero: "))
#
# lista = [numero1, numero2, numero3, numero4, numero5]
# listaordenada=sorted(lista)
# print(listaordenada[-1])

# 13. Pide una contraseña y sigue preguntando hasta que el usuario escriba "python" .
#
#
# contrasena = "python"
# userdice = ""
#
# while userdice != contrasena:
#     userdice = input("Dime la contraseña: ")
#     if userdice != contrasena:
#         print("Contraseña incorrecta")
#
# print("¡Correcto!")

# #Ejercicio 14 Crea una lista con 5 números y muestra todos los elementos.
#
# lista =[1,2,3,4,5]
# print(lista[0], lista[1], lista[2], lista[3], lista[4])
#
#
# # Ejercicio 15
# # Calcula la suma de todos los elementos de una lista.
# lista =[1,2,3,4,5]
# print(sum(lista))
#
# # Ejercicio 16 Encuentra el número más grande de una lista sin usar max() .
# lista = [4,5,33,6,8,99,0]
# ordenada = sorted(lista)
# print(ordenada[-1])

#17 . Cuenta cuántos números pares hay en una lista.
#
# lista = [2,3,4,5,6,6]
# par =0
# for each in lista:
#     if each % 2 == 0:
#         par+=1
# print(par)

# 18. Ejercicio 18
# # Crea una nueva lista que contenga solo los números mayores que 5.
#
# lista = [1,5,8,2,3,6,7]
# mayor5lista = []
# for each in lista:
#     if each >5:
#         mayor5lista.append(each)
#
# print(mayor5lista)
