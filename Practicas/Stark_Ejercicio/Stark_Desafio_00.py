from data_stark import lista_personajes

#-------> Convertir valores a float
def convertir_altura_a_float():
    for personaje in lista_personajes:
        personaje['altura'] = float(personaje['altura'])

def convertir_peso_a_float():
    for personaje in lista_personajes:
        personaje['peso'] = float(personaje['peso'])

#-------> Funciones requeridas
def listar_personajes():
    print('\n-------------------------------------------\n')
    print(' * Listado de Superhéroes * \n')
    for personaje in lista_personajes:
        print(personaje['nombre'])
    print('\n-------------------------------------------\n')

def listar_nombre_y_altura_personaje():
    print('\n-------------------------------------------\n')
    print(' * Listado de Superhéroes y alturas * \n')
    for personaje in lista_personajes:
        print(personaje['nombre'], ' - Altura: ', personaje['altura'])
    print('\n-------------------------------------------\n')

def mostrar_mas_alto():
    altura_maxima = lista_personajes[0]['altura']
    personaje_mas_alto = lista_personajes[0]['nombre']

    for personaje in lista_personajes:
        if (personaje['altura'] > altura_maxima):
            altura_maxima = personaje['altura']
            personaje_mas_alto = personaje['nombre']

    print('\n-------------------------------------------\n')
    print('Superhéroe más alto: ', personaje_mas_alto)
    print('Altura: ', altura_maxima)
    print('\n-------------------------------------------\n')

def mostrar_mas_bajo():
    altura_minima = lista_personajes[0]['altura']
    personaje_mas_bajo = lista_personajes[0]['nombre']

    for personaje in lista_personajes:
        if (personaje['altura'] < altura_minima):
            altura_minima = personaje['altura']
            personaje_mas_bajo = personaje['nombre']

    print('\n-------------------------------------------\n')
    print('Superhéroe más bajo: ', personaje_mas_bajo)
    print('Altura: ', altura_minima)
    print('\n-------------------------------------------\n')

def obtener_promedio():
    suma_alturas = 0
    contador = 0

    for personaje in lista_personajes:
        suma_alturas += personaje['altura']
        contador += 1

    promedio = suma_alturas / contador

    print('\n-------------------------------------------\n')
    print('El promedio de las alturas es: ', promedio)
    print('\n-------------------------------------------\n')

def mostrar_mas_pesado_y_mas_liviano():
    peso_mas_bajo = lista_personajes[0]['peso']
    personaje_menos_pesado = lista_personajes[0]['nombre']
    peso_mas_alto = lista_personajes[0]['peso']
    personaje_mas_pesado = lista_personajes[0]['nombre']

    for personaje in lista_personajes:
        if (peso_mas_bajo > personaje['peso']):
            peso_mas_bajo = personaje['peso']
            personaje_menos_pesado = personaje['nombre']
        elif (peso_mas_alto < personaje['peso']):
            peso_mas_alto = personaje['peso']
            personaje_mas_pesado = personaje['nombre']

    print('\n-------------------------------------------\n')
    print('Superhéroe más pesado: ', personaje_mas_pesado)
    print('Peso: ', peso_mas_alto)
    print('Superhéroe más liviano: ', personaje_menos_pesado)
    print('Peso: ', peso_mas_bajo)
    print('\n-------------------------------------------\n')

# J. Construir un menú que permita elegir qué dato obtener

"""
def mostrar_opciones():
    print(' 1. Imprimir el nombre de cada superhéroe')
    print(' 2. Imprimir el nombre de cada superhéroe y su altura')
    print(' 3. Mostrar superhéroe más alto')
    print(' 4. Mostrar superhéroe más bajo')
    print(' 5. Mostrar altura promedio de los superhéroes')
    print(' 6. Informar cual es el nombre del superhéroe asociado al más alto y más bajo')
    print(' 7. Calcular e informar cual es el superhéroe más y menos pesado')
    print(' 8. Salir')
    opcion = input('\n      Ingrese una opción -> ')
    return opcion
"""

lista_opciones = ['1. Imprimir el nombre de cada superhéroe', 
                  '2. Imprimir el nombre de cada superhéroe y su altura', 
                  '3. Mostrar superhéroe más alto', 
                  '4. Mostrar superhéroe más bajo', 
                  '5. Mostrar altura promedio de los superhéroes', 
                  '6. Informar cual es el nombre del superhéroe asociado al más alto y más bajo', 
                  '7. Calcular e informar cual es el superhéroe más y menos pesado', 
                  '8. Salir']

def mostrar_opciones(opciones_a_mostrar):
    for index in range(0, len(opciones_a_mostrar)):
        print(opciones_a_mostrar[index])
    
    opcion = input('\n     Ingrese una opción -> ')
    return opcion

def mensaje_bienvenida():
    print('\n**************************************\n'
          ' Stark Industries le da la bienvenida\n'
          '**************************************\n')

def mensaje_salida():
    print('\n**********************************\n'
          ' Usted está saliendo del programa\n'
          '**********************************\n')

def mensaje_error():
    print('\n-------------------------------------------\n'
          '\n |||||||||| ERROR ||||||||||\n'
          '\nDebe ingresar una opción válida entre 1 y 8\n'
          '\n-------------------------------------------\n')

# --------> Instrucciones

convertir_altura_a_float()
convertir_peso_a_float()
mensaje_bienvenida()

continuar = True

while (continuar):
    opcion = mostrar_opciones(lista_opciones)

    if (opcion.isalpha()):
        mensaje_error()
    else:
        opcion = int(opcion)
        if (opcion == 1):
            listar_personajes()
        elif (opcion == 2):
            listar_nombre_y_altura_personaje()
        elif (opcion == 3):
            mostrar_mas_alto()
        elif (opcion == 4):
            mostrar_mas_bajo()
        elif (opcion == 5):
            obtener_promedio()
        elif (opcion == 6):
            mostrar_mas_alto()
            mostrar_mas_bajo()
        elif (opcion == 7):
            mostrar_mas_pesado_y_mas_liviano()
        elif (opcion == 8):
            mensaje_salida()
            continuar = False
        else:
            mensaje_error()