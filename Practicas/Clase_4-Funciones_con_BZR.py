from canciones_bzrp import lista_bzrp;

# menor_cantidad_reproducciones = lista_bzrp[0]['views']
# titulo_menor_cant_reproducciones = lista_bzrp[0]['title']

# for video in lista_bzrp:
#     if (video['views'] < menor_cantidad_reproducciones):
#         menor_cantidad_reproducciones = video['views']
#         titulo_menor_cant_reproducciones = video['title']

# print('Video con menor cantidad de reproducciones:')
# print('Título: ', titulo_menor_cant_reproducciones)
# print('Cantidad de reproducciones: ', menor_cantidad_reproducciones)


# def calcular_menor_cantidad_vistas(lista, key_1, key_2):
#     value_1 = lista[0][key_1]
#     value_2 = lista[0][key_2]

#     for item in lista:
#         if (item[key_1] < value_1):
#             value_1 = item[key_1]
#             value_2 = item[key_2]

#     print('Video con menor cantidad de reproducciones:')
#     print('Título: ', value_2)
#     print('Cantidad de reproducciones: ', value_1)

# calcular_menor_cantidad_vistas(lista_bzrp, 'views', 'title')


# ---------------->
"""
1 mostrar minimo
2 mostrar maximo
3 mostrar promedio
4 salir
"""

def mostrar_menu():
    print('1. Mostrar mínimo')
    print('2. Mostrar máximo')
    print('3. Mostrar promedio')
    print('4. Salir')
    opcion_elegida = input('Ingrese una opción: ')
    return int(opcion_elegida)

continuar = True

while (continuar):
    opcion = mostrar_menu()
    if (opcion == 1):
        print("Opcion elegida: ", opcion)
    elif (opcion == 2):
        print("Opcion elegida: ", opcion)
    elif (opcion == 3):
        print("Opcion elegida: ", opcion)
    elif (opcion == 4):
        print("Gracias por su visita")
        continuar = False
    else:
        print("Opción incorrecta. Ingrese una opción entre 1 y 4.")