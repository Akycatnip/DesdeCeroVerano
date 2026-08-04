# 1. "adivinalo.py" Genera un número aleatorio del 1 al 100. Pide al usuario que lo adivine,
# indicando si es mayor o menor. En caso de adivinarlo se sale con "EUREKA. Lo has adivinado."
# import random
# numero_aleatorio = random.randint(1, 100)
#
# while True:
#     numero_user = int(input("Dime un número: \n"))
#     if numero_user > numero_aleatorio:
#         print("El número es menor")
#     elif(numero_user < numero_aleatorio):
#         print("El número es mayor")
#     else:
#         print("EUREKA!")
#         break


# 2. "adivinalo2.py" Igual que el anterior pero con un máximo de 10 intentos,
# # indicando los intentos que quedan y en cuánto lo ha adivinado.
# import random
#
# numero_aleatorio = random.randint(1, 100)
# intentos = 10
#
# while True:
#     numero_user = int(input("Dime un número: "))
#     intentos -= 1
#
#     if numero_user == numero_aleatorio:
#         print(f"EUREKA! Te ha costado {10 - intentos} intentos.")
#         break
#
#     if intentos == 0:
#         print("Se han agotado los intentos!")
#         break
#
#     print(f"Te quedan {intentos} intentos.")
#
#     if numero_user > numero_aleatorio:
#         print("El número es menor.")
#     else:
#         print("El número es mayor.")


# 3. "cuenta_cuentos.py" Pide un número y cuenta desde 1 hasta ese número.
# numero = int(input("Dime un numero\n"))
# for i in range(1, numero+1):
#     print(i)

# 4. "suma_numeros.py" Pide el número de iteraciones.
# En cada iteración pide un número y al final muestra la suma de los números positivos,
# la suma de los negativos y cuántos ceros se han introducido.
# iteraciones = int(input("Dime el número de iteraciones:\n"))
# positivos = 0
# negativos = 0
# ceros = 0
# for i in range(iteraciones):
#     numero = int(input("Dame un número\n"))
#         if numero == 0:
#         ceros += 1
#     elif numero < 0:
#         negativos += numero
#     else:
#         positivos += numero
# print(f"positivos = {positivos}, negativos = {negativos}, ceros = {ceros}")




# 5. "contador_numeros.py" Realizar un algoritmo que pida números
# (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
#
# cantidad_numeros = int(input("¿Cuántos números quieres introducir?\n"))
# contador_ceros = 0
# contador_positivos = 0
# contador_negativos = 0
# numero = 0
# for i in range(cantidad_numeros):
#     numero = int(input("Dame un número.\n"))
#     if numero ==0:
#         contador_ceros+=1
#     elif numero >0:
#         contador_positivos +=1
#     else:
#         contador_negativos +=1
# print(f"Hay un total de {contador_ceros} ceros, {contador_positivos} números positivos y {contador_negativos} números negativos.")



# 6. "tabla_multiplicar.py" Pide un número y muestra su tabla de multiplicar.
#
# numero = int(input("Elige un número: \n"))
# for i in range(0,11):
#     resultado = i*numero
#     print(f"{numero} X {i} ={resultado}")


# 7. "factorial.py" Pide un número y muestra su factorial.

# numero = int(input("dime el número: \n"))
# factorial = 1
# for i in range (1,numero+1):
#     factorial*=i
# print(factorial)


# 8. "con_caracter.py" Pide un caracter al usuario.
# Indicará si es o no vocal. Finaliza con la introducción de un "*".
# caracter=""
# while caracter != "*":
#     caracter = input("Dame un caracter. \n")
#     if caracter == "*":
#         break
#     elif caracter in ["a","e","i","o","u"]:
#         print("Es vocal.")
#     else:
#         print("no es vocal.")


# 9. "pares.py" Imprime todos los números pares entre dos números que se le pidan al usuario.
# a = int(input("Dime el primer número: \n"))
# b = int(input("Dime el segundo número. \n"))
# for i in range (a,b):
#     if i%2 ==0:
#         print(i)

# 10. "intervalo.py" Se le pide al usuario que introduzca el limite inferior y superior de un intervalo.
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0.
# Entonces el programa dará las siguientes informaciones:
#     - La suma de los números que están dentro del intervalo (intervalo abierto).
#     - Cuántos números están fuera del intervalo.
#     - Informa si hemos introducido algún número igual a los límites del intervalo.
limite_inferior= int(input("Dime el límite inferior. \n"))
limite_superior= int(input("Dime el límite superior. \n"))
if limite_inferior > limite_superior:
    print("Error, vuelve a introducirlos.")
    limite_inferior = int(input("Dime el límite inferior. \n"))
    limite_superior = int(input("Dime el límite superior. \n"))
numero =1
numeros=[]
no_en_rango = 0
igual_lim_inferior = 0
igual_lim_superior =0
while numero!=0 & numero in range(limite_inferior,limite_superior):
    numeros.append(int(input("Dame el número: \n")))
if numero not in range(limite_inferior,limite_superior):
    no_en_rango+=1
if numero == limite_inferior:
    igual_lim_inferior+=1
if numero == limite_superior:
    igual_lim_superior +=1
if numero ==0:
    print(f"Has introducido {no_en_rango} números fuera del rango, {igual_lim_inferior} números iguales al límite inferior, {igual_lim_superior} números iguales al límite superior, y la suma de todos los números en rango es: ")








# 11. "potencia_sin.py" Pide  dos números, uno real (base) y un entero positivo (exponente).
# Sacará  por pantalla el resultado de la potencia sin utilizar el operador de potencia.

# 12. "pagos.py" Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
# 13. "cronometro.py" Muestra un cronómetro, indicando las horas, minutos y segundos. Usa del módulo time `time.sleep(1)` para que el programa espere un segundo entre cada actualización.
# 14. "primos.py" Muestra los N primeros números primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
# 15. "caracter_en_cadena.py" Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.
# 16. "reemplazar_caracter.py" Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.
# 17. "contar_palabras.py" Pide una cadena por teclado y cuenta cuántas palabras tiene.
# 18. "mayusculas_minusculas.py" Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.
# 19. "subcadena.py" Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
# 20. "palindromo.py" Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.
# 21. "numeros_primos.py" Lee un número por teclado e indica si es un número primo o no.
# 22. "reemplazar_caracter.py" Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.