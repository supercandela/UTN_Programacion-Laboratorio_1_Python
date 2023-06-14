from data_stark import lista_personajes
from data_menu_opciones_Desafio_01 import menu_desafio_01

#-------> Convertir valores a float
def convertir_altura_a_float():
    for personaje in lista_personajes:
        personaje['altura'] = float(personaje['altura'])

def mostrar_opciones(opciones_a_mostrar):
    for index in range(0, len(opciones_a_mostrar)):
        print(opciones_a_mostrar[index])
    
    opcion = input('\n     Ingrese una opción -> ')
    return opcion

def mensaje_bienvenida():
    print('\n*******************************************\n'
          ' Stark Industries - Desafío 01 (Funciones)'
          '\n*******************************************\n')

def mensaje_salida():
    print('\n**********************************\n'
          ' Usted está saliendo del programa\n'
          '**********************************\n')

def mensaje_error(inicio, fin):
    print('\n-------------------------------------------\n'
          '\n |||||||||| ERROR ||||||||||\n'
          '\nDebe ingresar una opción válida entre ', inicio, ' y ', fin, '\n'
          '\n-------------------------------------------\n')

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def filtrar_por_genero(genero):
    filtrados = []
    for personaje in lista_personajes:
        if(personaje['genero'] == genero):
            filtrados.append(personaje)
    
    return filtrados

def filtrar_por_key(key, value):
    filtrados = []
    for personaje in lista_personajes:
        if(personaje[key] == value):
            filtrados.append(personaje)
    
    return filtrados

def filtrar_maximo(lista, key_a_filtrar):
    valor_maximo = lista[0][key_a_filtrar]
    elemento_maximo = lista[0]['nombre']

    for elemento in lista:
        if (elemento[key_a_filtrar] > valor_maximo):
            valor_maximo = elemento[key_a_filtrar]
            elemento_maximo = elemento['nombre']

    return elemento_maximo, valor_maximo

def filtrar_minimo(lista, key_a_filtrar):
    valor_minimo = lista[0][key_a_filtrar]
    elemento_minimo = lista[0]['nombre']

    for elemento in lista:
        if (elemento[key_a_filtrar] < valor_minimo):
            valor_minimo = elemento[key_a_filtrar]
            elemento_minimo = elemento['nombre']

    return elemento_minimo, valor_minimo

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def mostrar_masculino_mas_alto():
    filtrados_genero = filtrar_por_genero('M')
    nombre, altura = filtrar_maximo(filtrados_genero, 'altura')
    print('\n-------------------------------------------\n')
    print('Superhéroe más alto - Género Masculino: ', nombre)
    print('Altura: ', altura)
    print('\n-------------------------------------------\n')

# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def mostrar_femenino_mas_alto():
    filtrados_genero = filtrar_por_genero('F')
    nombre, altura = filtrar_maximo(filtrados_genero, 'altura')
    print('\n-------------------------------------------\n')
    print('Superhéroe más alto - Género Femenino: ', nombre)
    print('Altura: ', altura)
    print('\n-------------------------------------------\n')

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
def mostrar_masculino_mas_bajo():
    filtrados_genero = filtrar_por_genero('M')
    nombre, altura = filtrar_minimo(filtrados_genero, 'altura')
    print('\n-------------------------------------------\n')
    print('Superhéroe más bajo - Género Masculino: ', nombre)
    print('Altura: ', altura)
    print('\n-------------------------------------------\n')

# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def mostrar_femenino_mas_bajo():
    filtrados_genero = filtrar_por_genero('F')
    nombre, altura = filtrar_minimo(filtrados_genero, 'altura')
    print('\n-------------------------------------------\n')
    print('Superhéroe más bajo - Género Femenino: ', nombre)
    print('Altura: ', altura)
    print('\n-------------------------------------------\n')

# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
def obtener_promedio(lista, key_a_filtrar):
    suma_alturas = 0
    contador = 0

    for elemento in lista:
        suma_alturas += elemento[key_a_filtrar]
        contador += 1

    promedio = suma_alturas / contador
    return promedio

def mostrar_promedio_alturas_masculino():
    filtrados_genero = filtrar_por_genero('M')
    promedio = obtener_promedio(filtrados_genero, 'altura')
    print('\n-------------------------------------------\n')
    print('El promedio de las alturas de superhéroes de género masculino es: ', promedio)
    print('\n-------------------------------------------\n')

# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
def mostrar_promedio_alturas_femenino():
    filtrados_genero = filtrar_por_genero('F')
    promedio = obtener_promedio(filtrados_genero, 'altura')
    print('\n-------------------------------------------\n')
    print('El promedio de las alturas de superhéroes de género femenino es: ', promedio)
    print('\n-------------------------------------------\n')

# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# -----> OK

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
def crear_lista_variable(key):
    lista_variable = []
    for personaje in lista_personajes:
        variable_lower = personaje[key].lower()
        # if(variable_lower not in lista_variable):
        #     lista_variable.append(variable_lower)
        # elif(variable_lower == ''):
        #     lista_variable.append('No Tiene')
        if(variable_lower == '' and variable_lower not in lista_variable):
            lista_variable.append('No Tiene')
        elif(variable_lower not in lista_variable):
            lista_variable.append(variable_lower)
    return lista_variable

def contar_personajes_segun_variable(lista_valores_a_comparar, key_a_comparar):
    cantidades = []
    for elemento in lista_valores_a_comparar:
        contador = 0
        for personaje in lista_personajes:
            variable_lower = personaje[key_a_comparar].lower()
            if (variable_lower == elemento or (variable_lower == '' and elemento == 'No Tiene')):
                contador += 1
        cantidades.append(contador)
    
    return cantidades

def print_valores(titulo, lista_valores, lista_cantidades):
    print('\n-------------------------------------------\n')
    print(titulo, '\n')
    for indice in range(0, len(lista_valores)):
        mensaje = f"* {lista_valores[indice].capitalize()}: {lista_cantidades[indice]}"
        print(mensaje)

    print('\n-------------------------------------------\n')

# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

def filtrar_personajes_segun_variable(key):
    diccionario = {}

    for personaje in lista_personajes:
        variable = personaje[key].lower()
        nuevo_valor = 'No tiene'
        
        if (variable == '' and nuevo_valor not in diccionario):
            diccionario[nuevo_valor] = []
            diccionario[nuevo_valor].append(personaje['nombre'])
        elif (variable not in diccionario):
            diccionario[variable] = []
            diccionario[variable].append(personaje['nombre'])
        elif (variable == ''):
            diccionario[nuevo_valor].append(personaje['nombre'])
        else:
            diccionario[variable].append(personaje['nombre'])

    return diccionario

def imprimir_diccionario(diccionario, texto_claves, texto_items):
    print('\n-------------------------------------------\n')

    for clave, valor in diccionario.items():
        print(texto_claves, ': ', clave.capitalize())
        print(texto_items, ': ', valor)

    print('\n-------------------------------------------\n')

def imprimir_valores_filtrados(titulo, lista, key):
    print('\n-------------------------------------------\n')

    print(titulo)

    for elemento in lista:
        print(elemento[key])
    
    print('\n-------------------------------------------\n')


def init():
    convertir_altura_a_float()
    mensaje_bienvenida()

    continuar = True

    while (continuar):
        opcion = mostrar_opciones(menu_desafio_01)

        if (opcion.isdigit()):
            mensaje_error('A', 'P')
        else:
            opcion = opcion.upper()

            if (opcion == 'A'): # A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
                filtrados_genero = filtrar_por_genero('M')
                imprimir_valores_filtrados(' * Listado de Superhéroes - Género Masculino * \n', filtrados_genero, 'nombre')
            elif (opcion == 'B'): # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
                filtrados_genero = filtrar_por_genero('F')
                imprimir_valores_filtrados(' * Listado de Superhéroes - Género Femenino * \n', filtrados_genero, 'nombre')
            elif (opcion == 'C'): # C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
                mostrar_masculino_mas_alto()
            elif (opcion == 'D'): # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
                mostrar_femenino_mas_alto()
            elif (opcion == 'E'): # E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
                mostrar_masculino_mas_bajo()
            elif (opcion == 'F'): # F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
                mostrar_femenino_mas_bajo()
            elif (opcion == 'G'): # G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
                mostrar_promedio_alturas_masculino()
            elif (opcion == 'H'): # H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
                mostrar_promedio_alturas_femenino()
            elif (opcion == 'I'): # I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
                mostrar_masculino_mas_alto()
                mostrar_femenino_mas_alto()
                mostrar_masculino_mas_bajo()
                mostrar_femenino_mas_bajo()
            elif (opcion == 'J'): # J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
                lista_color_ojos = crear_lista_variable('color_ojos')
                cantidades = contar_personajes_segun_variable(lista_color_ojos, 'color_ojos')
                print_valores('Cantidad según color de ojos:', lista_color_ojos, cantidades)
            elif (opcion == 'K'): # K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
                lista_color_pelo = crear_lista_variable('color_pelo')
                cantidades = contar_personajes_segun_variable(lista_color_pelo, 'color_pelo')
                print_valores('Cantidad según color de pelo:', lista_color_pelo, cantidades)
            elif (opcion == 'L'): # L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
                lista_inteligencia = crear_lista_variable('inteligencia')
                cantidades = contar_personajes_segun_variable(lista_inteligencia, 'inteligencia')
                print_valores('Cantidad según tipo de inteligencia:', lista_inteligencia, cantidades)
            elif (opcion == 'M'): # M. Listar todos los superhéroes agrupados por color de ojos.
                diccionario_filtrados = filtrar_personajes_segun_variable('color_ojos')
                imprimir_diccionario(diccionario_filtrados, 'Color de Ojos', 'Superhéroes con ese color')
            elif (opcion == 'N'): # N. Listar todos los superhéroes agrupados por color de pelo.
                diccionario_filtrados = filtrar_personajes_segun_variable('color_pelo')
                imprimir_diccionario(diccionario_filtrados, 'Color de Pelo', 'Superhéroes con ese color')
            elif (opcion == 'O'): # O. Listar todos los superhéroes agrupados por tipo de inteligencia
                diccionario_filtrados = filtrar_personajes_segun_variable('inteligencia')
                imprimir_diccionario(diccionario_filtrados, 'Tipo de Inteligencia', 'Superhéroes con ese color')
            elif (opcion == 'P'): # P. Salir
                mensaje_salida()
                continuar = False
            else:
                mensaje_error()


# -----> EJECUTAR PROGRAMA
init()