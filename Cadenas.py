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

cad1=input("Cadena 1:")
cad2=input("Cadena 2:")
if cad2 in cad1:
	print ("cad2 es subcadena de cad1")
else:
	print ("cad2 no es subcadena de cad1")

print(cad1 if cad1<cad2 else cad2)#en este caso > ordena por orden alfabetico