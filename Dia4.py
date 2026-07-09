# # Crea una lista con diferentes tipos de datos literales. Recorre la lista y mediante la función
# # type() muestra el tipo de dato de cada elemento.
# lista = ["uno","dos","tres", 1, 2.3, True]
# print(lista)
# for each in lista:
#     print(type(each))
# # Aparece la palabra 'class' en la salida de type() porque todo en Python es un objeto, y cada tipo de dato es una clase.
# # Usa el slicing para mostrar solo el nombre del tipo de dato sin la palabra 'class' y sin los símbolos <>,
# # y sin comillas.
# # Por ejemplo, para un elemento 11, la salida debería ser: Elemento: 11, Tipo: int.
# lista = ["uno","dos","tres", 1, 2.3, True]
# for each in lista:
#    nuevaLista = str(type(each))
#    print(f"Elemento: {each}, Tipo: {nuevaLista[8:-2]}")
#
# # Crea una lista de elementos falsy y otra de elementos truthy. Recorre ambas listas e imprime si cada elemento
# # es falsy o truthy.
#
# elementosTruthy = ["si", 1, True]
# elementosFalsy = ["", 0, False]
# for each in elementosTruthy + elementosFalsy:
#     print(type(each))
# Escribe un programa que pida al usuario un número en binario (0b1010).
# # Deberá convertirlo a entero en base 10, a hexadecimal (base 16) y a texto, mostrando los resultados.
#
# numero = input("Ingrese un numero binario: ")
# numeroBase10 =int(numero, 2)
# print(f"El número binario: {numero} es también: {int(numeroBase10)}, {hex(numeroBase10)} y {chr(numeroBase10)}")

# Escribe un programa que pida al usuario un número en octal (0o12).
# Deberá convertirlo a entero en base 10, a binario (base 2),
# a hexadecimal (base 16) y a texto, mostrando los resultados.

# numero = input("Ingrese un numero octal: ")
# numeroBase10 =int(numero, 8)
# print(f"El número octal{numero}, es también: {hex(numeroBase10)}, {bin(numeroBase10)}, {numeroBase10} y {chr(numeroBase10)}")
# Escribe un programa que pida al usuario un número en decimal (12).
# Deberá convertirlo a binario (base 2), a octal (base 8), a hexadecimal (base 16) y a texto, mostrando los resultados.

# Escribe un programa que pida al usuario un número en hexadecimal (0x1A).
# Deberá convertirlo a entero en base 10, a binario (base 2), a octal (base 8) y a texto, mostrando los resultados.

