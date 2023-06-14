from data_stark import lista_personajes

from data_menu_opciones_Desafio_01 import menu_desafio_01
import re
import json

def generar_separador(patron, largo, imprimir = True):
    """
    Genera un string que contiene el patrón especificado,
    repetido tantas veces como la cantidad indicada en el largo,
    uno carácter junto a otro, sin salto de línea.
    Si imprimir == TRUE: imprime por pantalla el patrón generado
    Si imprimir == FALSE: no imprime por pantalla el patrón generado
    
    Params:
    - patron: (type: string) carácter que se usará como patrón para generar el separador
    - largo: (type: int) cantidad de caractéres que va a ocupar el separador
    - imprimir: (type: bool) (opcional) Default: True

    Return: (type: string)
    El patrón generado
    N/A - los parámetros no son válidos
    """
    # patron = patron.strip()
    nuevo_patron = ''
    if ((len(patron) > 0 and len(patron) < 3) and
        (type(largo) == int) and
        (largo > 0 and largo < 236)):
        while (largo > 0):
            nuevo_patron += patron
            largo -=1

        if (imprimir):
            print(nuevo_patron)

    else:
        nuevo_patron = 'N/A'

    return nuevo_patron

def imprimir_dato(dato):
    """
    Imprime por consola el parámetro recibido.

    Params:
    - dato: (type: string) texto a imprimir

    Return: void
    """
    print(dato)

def imprimir_menu_desafio_5():
    """
    Imprime por consola las opciones del menú. 
    
    Params: none

    Return: void
    """
    lista_menu = menu_desafio_01

    for item in lista_menu:
        imprimir_dato(item)

def stark_menu_principal_desafio_5():
    """
    Imprime el menú principal y pide al usuario que ingrese una opción.

    Params: none

    Return:
    -(letra): (type: string) si es correcto, la letra elegida por el usuario
    -1: (type: int) si el usuario ingresa un valor inválido
    """
    imprimir_menu_desafio_5()
    
    opcion = input('\n     Ingrese una opción -> ')

    if (re.findall('[a-zA-Z]+', opcion)):
        opcion = opcion.upper()
    else:
        opcion = -1

    return opcion

def leer_archivo(nombre_archivo:str) -> list:
    """
    Abre un archivo en modo lectura y retorna su contenido,
    convertido a una lista de diccionarios.

    Params:
    - nombre_archivo: (type: string) nombre y extensión del archivo a leer. 

    Return: (type: list)
    Lista de diccionarios con el contenido del archivo. 
    """
    # archivo = open(nombre_archivo, 'r')
    # texto = archivo.read()
    # contenido = texto[0]
    # print(type(contenido))
    # for item in contenido:
    #     print(item)

    # archivo.close()

    dic_json = {}
    with open (nombre_archivo, 'r') as archivo:
        dic_json = json.load(archivo)
    return(dic_json['heroes'])

def capitalizar_palabras(cadena_a_capitalizar):
    """
    Capitaliza la primera letra de cada palabra del string recibido por parámetro.

    Params:
    - cadena_a_capitalizar: (type: string) cadena que debe ser capitalizada

    Return:
    - string: (type: string) el string recibido por parámetro con la primera
    letra de cada palabra capitalizada.
    """
    nueva_cadena = cadena_a_capitalizar.strip()
    nueva_cadena = nueva_cadena.split(' ')
    cadena_a_retornar = ' '

    for index in range(0, len(nueva_cadena)):
        nueva_cadena[index] = nueva_cadena[index].capitalize()

    cadena_a_retornar = cadena_a_retornar.join(nueva_cadena)

    return cadena_a_retornar

def obtener_nombre_capitalizado(heroe):
    """
    Toma el campo nombre del diccionario recibido por parámetro
    y capitaliza las iniciales de las palabras que contenga. 

    Params:
    - heroe: (type: diccionario) diccionario con los datos del personaje

    Return:
    - string: (type: string) nombre del héroe capitalizado
    """
    key_a_capitalizar = 'nombre'
    if (type(heroe) == dict and key_a_capitalizar in heroe):
        valor = capitalizar_palabras(heroe[key_a_capitalizar])

    return valor

def stark_marvel_app_5():
    """
    Se encarga de la ejecución principal del programa.

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: void
    """
    generar_separador(' *', 50)
    imprimir_dato('\n                    Stark Industries - Desafío 05\n')
    generar_separador(' *', 50)

    continuar = True

    while(continuar):
        opcion = stark_menu_principal_desafio_5()
        imprimir_dato('\n')
        if (opcion == 'A'):
            # leer_archivo('c:\\Users\\Administrator\\Desktop\\Prog-Labo-1\\Stark_Ejercicio\\data_stark.json')
            lista_heroes_stark_json = leer_archivo('c:\\Users\\Administrator\\Desktop\\Prog-Labo-1\\Stark_Ejercicio\\data_stark.json')
            print(lista_heroes_stark_json)
        elif (opcion == 'B'):
            for heroe in lista_personajes:
                valor = obtener_nombre_capitalizado(heroe)
                print(valor)
        elif (opcion == 'Z'):
            generar_separador(' *', 50)
            imprimir_dato('\n                    Usted está saliendo del programa\n')
            generar_separador(' *', 50)
            continuar = False
        elif (opcion == -1):
            generar_separador(' *', 50)
            imprimir_dato('\n |||||||||| ERROR ||||||||||\n'
                          '\nDebe ingresar una opción válida\n')
            generar_separador(' *', 50)

# ----> EJECUTAR
stark_marvel_app_5()