# Ejercicio 1

# from customtkinter import *

# app = CTk()

# def button_on_click():
#     print("Esto funciona de maravilla!!")

# button = CTkButton(master=app, text="Click me!", command=button_on_click)
# button.grid()

# app.mainloop()

# --------------------> END



# Ejercicio 2

# from customtkinter import *

# app = CTk()

# name = input('Please enter your name: ')

# def button_on_click():
#     print("Bienvenid@, " + name)

# button = CTkButton(master=app, text="Click me!", command=button_on_click)
# button.grid()

# app.mainloop()

# --------------------> END



# Ejercicio 3
# Pedir que el usuario ingrese una edad y decir si la persona es mayor de edad

# age = input('Ingrese su edad: ')
# age = int(age)

# if age < 18:
#     print("Usted es menor de edad")
# else:
#     print("Usted es mayor de edad")

# --------------------> END



# Ejercicio 4
# Al ingresar una edad debemos informar si la persona es mayor de edad, sino informar que es un menor de edad

# age = int(input('Ingrese su edad: '))

# if age < 18:
#     print("Usted es menor de edad")
# else:
#     print("Usted es mayor de edad")

# --------------------> END



# Ejercicio 5
# Al ingresar una edad debemos informar si la persona es mayor de edad (mas de 18 años) o adolescente (entre 13 y 17 años) o niño (menor a 13 años).

# age = int(input('Ingrese su edad: '))

# if age < 13:
#     print("Usted es un niñx.")
# else:
#     if age < 18:
#         print("Usted es un adolescente")
#     else:
#         print("Usted es mayor de edad")

# if age < 13:
#     print("Usted es un niñx.")
# elif age < 18:
#     print("Usted es un adolescente")
# else:
#     print("Usted es mayor de edad")

# --------------------> END



# Ejercicio 6
# Mostrar 10 repeticiones con números ASCENDENTE, desde el 1 al 10.

# for numero in range(1,11,1):
#     print(numero)

# --------------------> END



# Ejercicio 7
# Pedir números hasta que el USUARIO QUIERA e informar la suma acumulada y el promedio.

# continuar = "s"
# suma = 0
# contador = 0
# while (continuar == "s"):
#     numero = int(input("Ingrese un número: "))
#     suma += numero
#     contador += 1
#     print("¿Desea continuar? s - SI / n - NO")
#     continuar = input()

# promedio = suma/contador
# print("La suma de los valores ingresados es: " + str(suma) + " y el promedio es: " + str(promedio))

# --------------------> END



# Ejercicio 8
# Pedir números hasta que el USUARIO QUIERA e informar la suma acumulada y el promedio.

# costo = 20
# precio = 23
# flag = 0
# if (costo < precio):
#     utilidad = precio - costo
#     print("La utilidad es: ", utilidad)
# elif (costo > precio):
#     flag = 1
#     perdida = precio - costo
#     print("La pérdida es: ", perdida)
# else:
#     print("Saliste empatado")
    
# if (flag == 1):
#     print(perdida)



# BURBUJEO

# lista = [ 2, 5, 3, 1, 6, 4 ]

# print("Lista desordenada")
# print(lista)

# for i in range(len(lista)-1):
#     for j in range(i+1, len(lista)):
#         if(lista[i] > lista[j]):
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux

# print("Lista ordenada")
# print(lista)

# Version 2
# lista = [ 2, 5, 3, 1, 6, 4 ]
# print("Lista desordenada")
# print(lista)

# bandera_swap = True

# while bandera_swap == True:
#     bandera_swap = False
#     # len--
#     for i in range(len(lista)-1):
#         if(lista[i] > lista[i+1]):
#             aux = lista[i]
#             lista[i] = lista[i+1]
#             lista[i+1] = aux
#             bandera_swap = True

# print("Lista ordenada")
# print(lista)


# Ordenamiento de diccionario:

lista = [ {"nombre":"Tito", "edad":32, "nota":6},
          {"nombre":"Job", "edad":37, "nota":7},
          {"nombre":"Ana", "edad":25, "nota":9},
          {"nombre":"Juan", "edad":28, "nota":8},
          {"nombre":"Jose", "edad":23, "nota":4}
        ]

def ordenar(lista:list, clave:str, tipo:str='ASC')->list:
    bandera_swap = True
    while bandera_swap == True:
        bandera_swap = False
        for i in range(len(lista)-1):
            if ( ( tipo == 'ASC' and lista[i][clave] > lista[i+1][clave] ) or
                ( tipo == 'DESC' and lista[i][clave] < lista[i+1][clave] ) ):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

                bandera_swap = True
    
    return lista

print("Lista desordenada: ")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

ordenar(lista, 'nombre')

print("Lista ordenada: ")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

ordenar(lista, 'nota', 'DESC')

print("Lista ordenada 2: ")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])



# ---------> arreglar csv

def leer_csv(ruta:str):
    lista_retorno = []
    with open (ruta, 'r') as archivo:
        for usuario in archivo:
            lista_aux = usuario.split(',')
            lista_retorno.append(lista_aux)
    
    return lista_retorno

def leer_csv_readlines(ruta:str):
    lista_retorno = []
    with open (ruta, 'r') as archivo:
        lista_aux = archivo.readlines()
        for usuario in lista_aux:
            lista_aux = usuario.split(',')
            lista_retorno.append(lista_aux)
    
    return lista_retorno


def guardar_csv(ruta:str, lista_usuario:list):
    with open (ruta, 'w') as archivo:
        for usuario in lista_usuario:
            archivo.write(','.join(usuario) + '\n')
    
    