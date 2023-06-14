"""
Ejercicio 1
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
"""

# nombre = input('Ingrese su nombre: ')
# sueldo = float(input('Ingrese su sueldo: '))

# incremento = 10

# sueldo += sueldo * incremento / 100

# print('Bienvenid@, ' + nombre + '. Su sueldo con aumento es: $' + str(sueldo))


"""
Ejercicio 2
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
"""
# age = int(input("Ingrese su edad: "))

# if (age >= 18):
#     print("Usted es mayor de edad")
# elif (age > 12):
#     print("Usted es adolescente")
# else:
#     print("Usted es un niñx")


"""
Ejercicio 3
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
"""
# contador = 0
# cantidad_pares = 0
# cantidad_impares = 0
# flag_pares = False
# suma_positivos = 0
# producto_negativos = 1

# while (contador < 5):
#     numero = int(input("Ingrese un número entero (distinto de cero): "))
#     if (numero == 0):
#         print("El número ingresado debe ser distinto de cero")
#     else:
#         if (contador == 0):
#             numero_menor = numero
#         elif (numero_menor > numero):
#             numero_menor = numero

#         if (numero % 2 == 0):
#             cantidad_pares += 1
#             if (not flag_pares):
#                 mayor_numero_par = numero
#                 flag_pares = True
#             elif (mayor_numero_par < numero):
#                 mayor_numero_par = numero
#         else:
#             cantidad_impares +=1

#         if (numero > 0):
#             suma_positivos += numero
#         else:
#             producto_negativos *=numero

#         contador += 1

# print("Cantidad de números pares ingresados: " + str(cantidad_pares))
# print("Cantidad de números impares ingresados: " + str(cantidad_impares))
# print("Menor número ingresado: " + str(numero_menor))
# print("Mayor número par ingresado: " + str(mayor_numero_par))
# print("Suma de los positivos: " + str(suma_positivos))
# print("Producto de los negativos: " + str (producto_negativos))

"""
Ejercicio 4
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'
"""
# edad = int(input("Ingrese su edad: "))
# validacion = False

# while (not validacion):
#     print("Ingrese su estado civil: 1 - Solterx / 2 - Casadx / 3 - Divorciadx / 4 - Viudx")
#     estado_civil = int(input())
#     if (estado_civil > 0 and estado_civil < 5):
#         validacion = True

# if (estado_civil == 1):
#     estado_civil_str = "Solterx"
# elif (estado_civil == 2):
#     estado_civil_str = "Casadx"
# elif (estado_civil == 3):
#     estado_civil_str = "Divorciadx"
# else:
#     estado_civil_str = "Viudx"

# print("Su edad es " + str(edad) + " y su estado civil es " + estado_civil_str)
# if (edad < 18 and estado_civil != 1):
#     print("Es muy pequeño para NO ser soltero.")

"""
Ejercicio 5
Una agencia de viajes debe sacar las tarifas de los viajes , 
se cobra $15.000 por cada estadía como base, 
se pide el ingreso de una estación del año(Invierno/Verano/Otoño/Primavera) 
y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) para vacacionar 
para poder calcular el precio final:
-en Invierno: 
    Bariloche tiene un aumento del 20% 
    Cataratas y Córdoba tiene un descuento del 10% 
    Mar del Plata tiene un descuento del 20%
-en Verano: 
    Bariloche tiene un descuento del 20% 
    Cataratas y Córdoba tiene un aumento del 10% 
    Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: 
    Bariloche tiene un aumento del 10% 
    Cataratas tiene un aumento del 10% 
    Mar del Plata tiene un aumento del 10%
    Córdoba tiene el precio sin descuento.
Validar el ingreso de datos
"""
# estadia_base = 15000
# validar_estacion = False
# validar_localidad = False

# while (not validar_estacion):
#     print("Ingrese una estación: (1 - Otoño / 2 - Invierno "
#           "/ 3 - Primavera / 4 - Verano)")
#     estacion = int(input())
#     if (estacion > 0 and estacion < 5):
#         validar_estacion = True
#     else:
#         print("Valor no válido. Ingrese un número entre 1 y 4, según la estación")

# while (not validar_localidad):
#     print("Ingrese una localidad: (1 - Bariloche / 2 - Cataratas "
#           "/ 3 - Mar del Plata / 4 - Córdoba)")
#     localidad = int(input())
#     if (localidad > 0 and localidad < 5):
#         validar_localidad = True
#     else:
#         print("Valor no válido. Ingrese un número entre 1 y 4, según la localidad")

# if (estacion == 2):
#     if (localidad == 1):
#         estadia_final = estadia_base + estadia_base * 0.2
#     elif (localidad == 3):
#         estadia_final = estadia_base - estadia_base * 0.2
#     else:
#         estadia_final = estadia_base - estadia_base * 0.1
# elif (estacion == 4):
#     if (localidad == 1):
#         estadia_final = estadia_base - estadia_base * 0.2
#     elif (localidad == 3):
#         estadia_final = estadia_base + estadia_base * 0.2
#     else:
#         estadia_final = estadia_base + estadia_base * 0.1
# else:
#     if (localidad < 4):
#         estadia_final = estadia_base + estadia_base * 0.1
#     else:
#         estadia_final = estadia_base

# if (estacion == 1):
#     estacion_str = "Otoño"
# elif (estacion == 2):
#     estacion_str = "Invierno"
# elif (estacion == 3):
#     estacion_str = "Primavera"
# else:
#     estacion_str = "Verano"

# if (localidad == 1):
#     localidad_str = "Bariloche"
# elif (localidad == 2):
#     localidad_str = "Cataratas del Iguazú"
# elif (localidad == 3):
#     localidad_str = "Mar del Plata"
# else:
#     localidad_str = "Córdoba"

# print("Estadía en: " + localidad_str)
# print("Estación elegida: " + estacion_str)
# print("Valor de las vacaciones: + $" + str(estadia_final))

"""
Ejercicio 6
Utilizar For
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar el mayor.
"""
# lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

# numero_mayor = lista[0]

# for numero in lista:
#     if (numero > numero_mayor):
#         numero_mayor = numero

# print("Mayor número de la lista: " + str(numero_mayor))

"""
Ejercicio 7
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar solo los números pares.
"""
# lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# numeros_pares = []

# for numero in lista:
#     if (numero % 2 == 0):
#         numeros_pares.append(numero)

# print("Números pares de la lista:")
# for numero in numeros_pares:
#     print(numero)

"""
Ejercicio 8
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido
"""
# lista = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

# # SOLUCION MIA
# repetido_anterior = False

# for numero in lista:
#     repetido = 0
#     for numero_a_comprobar in lista:
#         if (numero_a_comprobar == numero):
#             repetido += 1
#         if (repetido == 2):
#             repetido = 0
#             if (repetido_anterior != numero):
#                 print("El número repetido es: " + str(numero))
#                 repetido_anterior = numero

# #Solución de internet
# for i in range(0, len(lista)):    
#     for j in range(i+1, len(lista)):    
#         if(lista[i] == lista[j]):    
#             print("El número repetido es: ", lista[j]);

"""
Ejercicio 9
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
"""
edades = [25,36,18,23,45]
nombres = ["Juan","Ana","Sol","Mario","Sonia"]

# edad_mas_joven = edades[0]
# indice = 0

# if (len(edades) == len(nombres)):
#     for i in range(0, len(edades)):
#         if (edad_mas_joven > edades[i]):
#             edad_mas_joven = edades[i]
#             indice = i

for indice in range(len(edades)):
    if (indice == 0 or edades[indice_minimo] > edades[indice]):
        indice_minimo = indice

print("La persona más joven es " + nombres[indice_minimo] + " y tiene " + str(edades[indice_minimo]) + " años.")
# print("La persona más joven es ", nombres[indice], " y tiene ", edades[indice], " años.")

"""
Ejercicio 10
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]
"""
# nombres = []
# sexo = []
# notas = []

# for i in range(0, 5):
#     print("Ingrese nombre del alumnx: ")|