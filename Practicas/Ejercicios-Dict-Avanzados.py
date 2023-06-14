from copy import deepcopy

# Se tiene la siguiente lista de diccionarios:
lista_diccionario = [
    {'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
    {'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
    {'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
    {'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
    {'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
]

# Hacer una copia deep copy y trabajar con la copia, de acuerdo a lo siguiente:
copia_lista_original = deepcopy(lista_diccionario)

def calcular_iva(dicc):
    dicc['precio']['con_iva'] = dicc['precio']['sin_iva'] * 1.21
    return dicc

# Se debera mapear al precio con iva, sumando el 21% sobre el precio sin iva.
lista_resultado = list(map(calcular_iva, copia_lista_original))
# Mostrar los datos por pantalla
print(lista_resultado)

# # Modificar el nombre de Destornillador por Destornillador Philips.
# for elemento in copia_lista_original:
#     nombre_a_cambiar = elemento.get('nombre','NO NAME')
#     if (nombre_a_cambiar == 'Destornillador'):
#         elemento.update({'nombre' : 'Destornillador Philips'})

# # Mostrar los datos por pantalla.
# for elemento in copia_lista_original:
#     print(elemento)

# # Agregar una herramienta con sus respectivos datos.
# lista_claves = []
# for elemento in copia_lista_original:
#     for clave in elemento:
#         if (type(elemento[clave]) == dict):
#             lista_claves.append(clave)
#             for item in elemento[clave]:
#                 print(item, elemento[clave][item])
#                 lista_claves.append(item)
#         else:
#             print(clave,elemento[clave])
#             lista_claves.append(clave)
# print(lista_claves)

# nuevo_elemento_1 = {'nombre' : 'Caja de Herramientas','precio': {'sin_iva': 12000.00,'con_iva':0.00}}
# nuevo_elemento_2 = {'nombre' : 'Escalera 10 escalones','precio': {'sin_iva': 23000.00,'con_iva':0.00}}

# copia_lista_original.append(nuevo_elemento_1)
# copia_lista_original.append(nuevo_elemento_2)
## Mostrar los datos.
# print(copia_lista_original)


# Eliminar dos herramientas que no sean ni la primera ni la ultima y agregarlas a una lista de herramientas eliminadas.

# lista_resultado = list(filter(lambda elem : elem >= 18, lista))


# Mostrar los datos.


"""   
    

    Mostrar los datos de la lista original, la lista trabajada y la lista de herramientas eliminadas.
"""