from data_stark import lista_personajes
import re

def mensaje_bienvenida():
    """
    Muestra por consola un mensaje de bienvenida al programa

    Params: none

    Return: void
    """
    print('\n*****************************************\n'
          ' Stark Industries - Desafío 02 (Cadenas)'
          '\n*****************************************\n')

def mensaje_salida():
    """
    Muestra por consola un mensaje de salida del programa

    Params: none

    Return: void
    """
    print('\n**********************************\n'
          ' Usted está saliendo del programa\n'
          '**********************************\n')

def mensaje_error():
    """
    Muestra por consola un mensaje de error, cuando el usuario ingresa un valor erróneo

    Params: none

    Return: void
    """
    print('\n-------------------------------------------\n'
          '\n |||||||||| ERROR ||||||||||\n'
          '\nDebe ingresar una opción válida\n'
          '\n-------------------------------------------\n')

def mostrar_opciones(opciones_a_mostrar):
    """
    Muestra por consola las opciones de un menú

    Params:
    - opciones_a_mostrar: (type: lista) lista con los valores que se debe iterar y mostrar

    Return: (type: any)
    - opcion ingresada por el usuario
    """
    for index in range(0, len(opciones_a_mostrar)):
        print(opciones_a_mostrar[index])
    
    opcion = input('\n     Ingrese una opción -> ')
    return opcion

def extraer_iniciales(nombre_heroe):
    """
    Extrae las iniciales del string entregado como parámetro.
    Elimina subcadenas con el artículo 'the'
    Reemplaza guiones medios por espacios en blanco

    Params:
    - nombre_heroe: (type: string) string del que vamos a extraer las iniciales

    Return: (type: string) 
    - iniciales del string recibido seguidas por un punto (.)
    - 'N/A' en caso de recibir un string vacío
    """
    nombre_sin_the = []
    iniciales = []
    iniciales_final = '.'
    nombre_heroe = nombre_heroe.strip()

    if (nombre_heroe == ''):
        iniciales_final = 'N/A'
    else:
        nombre_heroe = nombre_heroe.replace('-', ' ')
        nombre_heroe = nombre_heroe.split(' ')
        for palabra in nombre_heroe:
            if (palabra == 'the'):
                continue
            else:
                nombre_sin_the.append(palabra)

        for palabra in nombre_sin_the:
            iniciales.append(palabra[0].upper())

        iniciales_final = iniciales_final.join(iniciales) + '.'

    return iniciales_final

def definir_iniciales_nombre(heroe):
    """
    Agrega una nueva clave-valor al diccionario recibido como param.
    Nombre clave: 'iniciales'
    Valor: retorno de la funcion 'extraer_iniciales'

    Params:
    - heroe: (type: diccionario) diccionario con los datos del personaje

    Return: (type: bool) 
    - False: si encuentra algún error
    - True: si funciona correctamente
    """
    key_a_buscar = 'nombre'
    key_a_agregar = 'iniciales'
    if (type(heroe) == dict and key_a_buscar in heroe):
        valor_a_agregar = extraer_iniciales(heroe[key_a_buscar])
        if (valor_a_agregar == 'N/A'):
            return False
        else:
            heroe[key_a_agregar] = valor_a_agregar
            return True
    else:
        return False
    
def agregar_iniciales_nombre(lista_heroes):
    """
    Itera la lista_heroes pasándole cada héroe a la función 'definir_iniciales_nombre'
    Si la función 'definir_iniciales_nombre' devuelve False, debe 
    detener la iteración y mostrar un mensaje de error.

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: (type: bool) 
    - False: si encuentra algún error
    - True: si funciona correctamente
    """
    if (type(lista_heroes) == list and len(lista_heroes) > 0):
        for heroe in lista_heroes:
            if (definir_iniciales_nombre(heroe) == False):
                print('El origen de datos no contiene el formato correcto')
                return False
        return True
    else:
        return False

def stark_imprimir_nombres_con_iniciales(lista_heroes):
    """
    Llama a la función 'agregar_iniciales_nombre', para agregar una nueva 
    clave-valor al diccionario que es cada elemento de la lista.
    Luego imprime la lista completa de nombres seguida por las iniciales,
    encerradas entre paréntesis.

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: void
    """
    if (type(lista_heroes) == list and len(lista_heroes) > 0):
        if (agregar_iniciales_nombre(lista_heroes)):
            print('\n-------------------------------------------\n')
            print(' * Listado de Superhéroes con Iniciales * \n')
            
            for personaje in lista_heroes:
                print('* ', personaje['nombre'], ' (', personaje['iniciales'], ')')

            print('\n-------------------------------------------\n')
        else:
            print('Se produjo un error en la ejecución.')

def generar_codigo_heroe(id_heroe, genero_heroe):
    """
    Genera un string con el siguiente formato: GENERO-000…000ID
    (género_heroe + - + id_heroe) de un máximo de 10 caracteres.

    Params:
    - id_heroe: (type: int) identificador del héroe
    - genero_heroe: (type: string) representa el género del héroe 
        (puede tomar los valores 'M', 'F' o 'NB')

    Return: (type: string)
    - codigo: si pudo generarse correctamente
    - 'N/A' en caso de algún error
    """
    if (type(id_heroe) == int and (len(genero_heroe) > 0 and (genero_heroe == 'F' or genero_heroe == 'M' or genero_heroe == 'NB'))):
        codigo = f'{genero_heroe}-{id_heroe}'
        while (len(codigo) < 10):
            nuevo_valor = codigo.split('-')
            nuevo_valor[1] = nuevo_valor[1].zfill(len(nuevo_valor[1]) + 1)
            codigo = f'{nuevo_valor[0]}-{nuevo_valor[1]}'
        return codigo
    else:
        return 'N/A'
    
def agregar_codigo_heroe(heroe, id_heroe):
    """
    Agrega una nueva clave-valor al diccionario recibido como param.
    Nombre clave: 'codigo_heroe'
    Valor: retorno de la funcion 'generar_codigo_heroe'

    Params:
    - heroe: (type: diccionario) diccionario a procesar
    - id_heroe: (type: int) identificador del heroe

    Return: (type: bool) 
    - False: si encuentra algún error
    - True: si funciona correctamente
    """
    key_a_buscar = 'genero'
    key_a_agregar = 'codigo_heroe'
    if (type(heroe) == dict and key_a_buscar in heroe):
        valor_a_agregar = generar_codigo_heroe(id_heroe, heroe[key_a_buscar])
        if (valor_a_agregar == 'N/A'):
            return False
        elif (len(valor_a_agregar) == 10):
            heroe[key_a_agregar] = valor_a_agregar
            return True
        else:
            return False
    else:
        return False

def stark_generar_codigos_heroes(lista_heroes):
    """
    Llama a la función 'agregar_codigo_heroe', para agregar una nueva 
    clave-valor al diccionario que es cada elemento de la lista.
    Luego imprime el codigo generado para cada heroe

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: void

    Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
    (## representa la cantidad de códigos generados):
    Se asignaron ## códigos
    * El código del primer héroe es: M-00000001
    * El código del del último héroe es: M-00001224

    """
    contador = 0
    key_a_confirmar = 'genero'
    exito = False

    if (len(lista_heroes) > 0):
        for index in range(0, len(lista_heroes)):
            if (type(lista_heroes[index]) == dict and key_a_confirmar in lista_heroes[index]):
                agregar_codigo_heroe(lista_heroes[index], index + 1)
                contador += 1
                exito = True
            else:
                print('El origen de datos no contiene el formato correcto')

    else:
        print('El origen de datos no contiene el formato correcto')

    if (exito):
        print('\n-------------------------------------------\n')
        print(f' * Se asignaron {contador} códigos * \n')
        
        # for personaje in lista_heroes:
        #     print('* ', personaje['nombre'], ': ', personaje['codigo_heroe'])

        print('\n-------------------------------------------\n')

def sanitizar_entero(numero_str):
    """
    Analiza el valor recibido por parámetro y determina si es un entero positivo.

    Params:
    - numero_str: (type: string) representa un posible número entero

    Return: (type: int)
    - int: valor del parámetro convertido en entero positivo
    - -1: contiene carácteres no numéricos
    - -2: es un número negativo
    - -3: otros errores que no permiten convertir el valor a entero - Cero - Flotantes
    """
    valor_retorno = numero_str.strip()
    if (re.findall('[^a-zA-Z0-9\-]+', valor_retorno)):
        valor_retorno = -3
    elif (re.findall('[a-zA-Z ]+', valor_retorno)):
        valor_retorno = -1
    elif (re.findall('[0-9\-]+', valor_retorno)):
        valor_retorno = int(valor_retorno)
        if (valor_retorno > 0):
            valor_retorno = valor_retorno
        elif (valor_retorno == 0):
            valor_retorno = -3
        else:
            valor_retorno = -2
    else:
        valor_retorno = -3

    return valor_retorno

def sanitizar_flotante(numero_str):
    """
    Analiza el valor recibido por parámetro y determina si es un flotante positivo.
    
    Params:
    - numero_str: (type: string) representa un posible número flotante
    
    Return: (type: float/int)
    - float: valor del parámetro convertido en flotante positivo
    - int -1: contiene carácteres no numéricos
    - int -2: es un número negativo
    - int -3: otros errores que no permiten convertir el valor a flotante
    """
    valor_retorno = numero_str.strip()
    # print(valor_retorno)
    if (re.findall('[^a-zA-Z0-9\-\.]+', valor_retorno)):
        # print('findall caracteres especiales')
        valor_retorno = -3
    elif (re.findall('[a-zA-Z ]+', valor_retorno)):
        # print('findall letras')
        valor_retorno = -1
    elif (re.findall('[0-9\-\.]+', valor_retorno)):
        # print('findall numeros, guiones y puntos')
        valor_retorno = float(valor_retorno)
        if (valor_retorno > 0):
            # print('if')
            valor_retorno = valor_retorno
        elif (valor_retorno == 0):
            # print('elif')
            valor_retorno = -3
        else:
            # print('else')
            valor_retorno = -2
    else:
        # print('else afuera')
        valor_retorno = -3

    return valor_retorno

def sanitizar_string(valor_str, valor_por_defecto = '-'):
    """
    Analiza el valor recibido por parámetro y determina si es sólo texto
    (No incluye números)

    Params:
    - valor_str: (type: string) texto a validar
    - valor_por_defecto: (type: string) (opcional) valor por defecto. Default = '-'

    Return: (type: string)
    - string: el valor recibido por parámetro convertido a minúsculas
    - 'N/A' en caso de que el valor recibido por parámetro contenga números
    """
    mensaje_error = 'N/A'
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    # En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un espacio
    valor_str = valor_str.replace('/', ' ')

    # Convertir return a minúscula
    valor_str = valor_str.lower()
    valor_por_defecto = valor_por_defecto.lower()

    if (re.findall('[0-9]+', valor_str)):
    # 'N/A' en caso de que el valor recibido por parámetro contenga números
        # print("findAll tiene números")
        valor_str = mensaje_error
    elif (re.findall('[a-zA-Z ]+', valor_str)):
    # Revisar valor_str y ver si es sólo texto, sin números
    # El espacio es un caracter válido
        # print('findall letras')
        valor_str = valor_str
    elif (valor_str == ''):
    # En el caso que el texto a validar se encuentre vacío y que nos hayan pasado un valor por defecto, 
    # entonces retornar el valor por defecto convertido a minúsculas
        # print('string vacio')
        valor_str = valor_por_defecto

    return valor_str

def sanitizar_dato(heroe, clave, tipo_dato):
    """
    Sanitiza el dato correspondiente a la clave pasada por parámetro, para
    el diccionario pasado por parámetro, según el tipo de dato que sea, también
    pasado por parámetro. Para eso, llama a las otras funciones. 

    Params:
    - heroe: (type: diccionario) diccionario a procesar
    - clave: (type: string) clave a buscar en el diccionario
    - tipo_dato: (type: string) tipo de dato a sanitizar. 
        Puede tomar los valores 'string', 'entero' y 'flotante'

    Return: (type: bool) 
    - False: si encuentra algún error
    - True: si funciona correctamente
    """
    tipo_dato = tipo_dato.lower()
    retorno = False

    if (tipo_dato == 'string' or tipo_dato == 'entero' or tipo_dato == 'flotante'):
        # print('OK tipo_dato')
        if (clave in heroe):
            # print('OK clave en diccionario')
            valor_a_sanitizar = heroe[clave]
            if (tipo_dato == 'string'):
                nuevo_valor = sanitizar_string(valor_a_sanitizar)
                if (nuevo_valor != 'N/A'):
                    heroe[clave] = nuevo_valor
            elif (tipo_dato == 'entero'):
                nuevo_valor = sanitizar_entero(valor_a_sanitizar)
                if (nuevo_valor > 0):
                    heroe[clave] = nuevo_valor
            elif (tipo_dato == 'flotante'):
                nuevo_valor = sanitizar_flotante(valor_a_sanitizar)
                if (clave == 'altura' and nuevo_valor > 0):
                    nuevo_valor = convertir_cm_a_mtrs(nuevo_valor)
                if (nuevo_valor > 0):
                    heroe[clave] = nuevo_valor
            
        else:
            print('La clave especificada no existe en el héroe')
    else:
        print('Tipo de dato no reconocido')

    if ( ((type(nuevo_valor) == int or type(nuevo_valor) == float) and nuevo_valor > 0 ) or 
            (type(nuevo_valor) == str and nuevo_valor != 'N/A')):
        retorno = True

    return retorno

def stark_normalizar_datos(lista_heroes):
    """
    Recorre la lista y sanitiza los valores de las claves:
    'altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza' e 'inteligencia'.
    
    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: void
    """
    claves_y_tipos = [{'clave': 'altura', 'tipo': 'flotante'},
                      {'clave': 'peso', 'tipo': 'flotante'},
                      {'clave': 'color_ojos', 'tipo': 'string'},
                      {'clave': 'color_pelo', 'tipo': 'string'},
                      {'clave': 'fuerza', 'tipo': 'entero'},
                      {'clave': 'inteligencia', 'tipo': 'string'}]

    if (len(lista_heroes) > 0):
        # print('listaOK')

        for heroe in lista_heroes:

            for index in range(0, len(claves_y_tipos)):
                clave = claves_y_tipos[index]['clave']
                tipo = claves_y_tipos[index]['tipo']
                # print(clave, tipo)
                retorno = sanitizar_dato(heroe, clave, tipo)
                if (retorno == False):
                    print('Error en la normalización')
                    break
        
        generar_separador('*', 30)
        print('\nDatos normalizados\n')
        generar_separador('*', 30)
    else:
        print('Error: Lista de héroes vacía')

def generar_indice_nombres(lista_heroes):
    """
    Recorre la lista pasada como parámetro y genera una nueva lista, donde cada
    elemento es cada palabra que compone el campo 'nombre' de los diccionarios 
    de la lista parámetro.

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: 
    (type: list) - Si el funcionamiento fue correcto y exitoso.
    False. (type: bool) Si encuentra un error.
    """
    key_a_buscar = 'nombre'
    exito = False
    nueva_lista = []

    if (len(lista_heroes) > 0):
        for heroe in lista_heroes:
            exito = False
            if (type(heroe) == dict and key_a_buscar in heroe):
                valor = heroe[key_a_buscar]
                valor = valor.strip()
                valor = valor.replace('-', ' ')
                valor = valor.split(' ')
                for palabra in valor:
                    nueva_lista.append(palabra)
        
                exito = True

    if (exito):
        return nueva_lista
    else:
        print('El origen de datos no contiene el formato correcto')
        return exito

def stark_imprimir_indice_nombre(lista_heroes):
    """
    Muestra por pantalla el índice generado en la función generar_indice_nombres,
    con cada elemento separado por un guión.

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: void
    """
    if (len(lista_heroes) > 0):
        valor = generar_indice_nombres(lista_heroes)
        if (valor != False):
            valor = '-'.join(valor)
            print('\n-------------------------------------------\n')
            print(f' * Índice de Nombres * \n')
            print(valor)
            print('\n-------------------------------------------\n')
        else:
            print('\n-------------------------------------------\n')
            print(f' * Error en los datos ingresados * \n')
            print('\n-------------------------------------------\n')

def convertir_cm_a_mtrs(valor_cm):
    """
    Convierte el valor recibido por parámetro de centímetros a metros.

    Params:
    - valor_cm: (type: float) valor a convertir

    Return: 
    (type: float) - Valor convertido a metros
    -1: (type: int) - En caso de algún error.
    """
    if (type(valor_cm) == float and valor_cm > 0): 
        valor_cm = valor_cm / 100
    else:
        valor_cm = -1
    
    return valor_cm

def generar_separador(patron, largo, imprimir = True):
    """
    Genera un string que contiene el patrón especificado,
    repetido tantas veces como la cantidad indicada en el largo,
    uno junto a otro, sin salto de línea.
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
    patron = patron.strip()
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

def generar_encabezado(titulo):
    """
    Genera un encabezado con el título del parámetro envuelto entre dos separadores.

    Params:
    - titulo: (type: string) título de una sección

    Return: (type: string)
    El encabezado generado.

    La función deberá convertir el titulo recibido en todas letras mayúsculas
    """
    titulo = titulo.upper()

    separador = generar_separador('*', 87, False)

    encabezado =  f'\n{separador}\n{titulo}\n{separador}'

    return encabezado

def imprimir_ficha_heroe(heroe):
    """
    Imprime por pantalla la ficha del diccionario recibido por parámetro

    Params:
    - heroe: (type: diccionario) diccionario a procesar

    Return: void
    """
    encabezado_principal = generar_encabezado('principal')
    print(encabezado_principal)
    print(f'NOMBRE DEL HÉROE: {heroe["nombre"]} ({heroe["iniciales"]})')
    print(f'IDENTIDAD SECRETA: {heroe["identidad"]}')
    print(f'CONSULTORA: {heroe["empresa"]}')
    print(f'CÓDIGO DE HÉROE: {heroe["codigo_heroe"]}')

    encabezado_fisico = generar_encabezado('físico')
    print(encabezado_fisico)
    print(f'ALTURA: {heroe["altura"]} Mtrs.')
    print(f'PESO: {heroe["peso"]} Kg.')
    print(f'FUERZA: {heroe["fuerza"]} N')

    encabezado_senas = generar_encabezado('Señas Particulares')
    print(encabezado_senas)
    print(f'COLOR DE OJOS: {heroe["color_ojos"]}')
    print(f'COLOR DE PELO: {heroe["color_pelo"]}')

    generar_separador('*', 87)

def stark_navegar_fichas(lista_heroes):
    """
    Imprime la ficha del primer personaje de la lista recibida por parámetro.
    Pide al usuario que ingrese una opción:
    [ 1 ] Ir a la izquierda - mostrar el héroe que se encuentra en
    la posición anterior en la lista (en caso de estar en el primero, ir al
    último)
    [ 2 ] Ir a la derecha - mostrar el héroe que se encuentra en
    la posición siguiente en la lista (en caso de estar en el último, ir al
    primero)
    [ S ] Salir - volver al menú principal
    Si ingresa otro valor, volver a mostrar las opciones hasta que
    ingrese un valor válido

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: void
    """
    if (len(lista_heroes) > 0):
        actual = 0
        imprimir_ficha_heroe(lista_heroes[actual])
        continuar = True
        while (continuar):
            opcion = mostrar_opciones(['1. Ir a la izquierda',
                                       '2. Ir a la derecha',
                                       'S. Salir'])
            
            opcion = opcion.upper()
            if (opcion == '1'):
                actual = actual - 1
                if (actual == -1):
                    actual = len(lista_heroes) - 1
                imprimir_ficha_heroe(lista_heroes[actual])
            elif (opcion == '2'):
                actual = actual + 1
                if (actual == len(lista_heroes)):
                    actual = 0
                imprimir_ficha_heroe(lista_heroes[actual])
            elif (opcion == 'S'):
                print('\nVolviendo al menú principal...')
                generar_separador('*', 87)
                continuar = False
            else:
                mensaje_error()

    else:
        print('La lista recibida no es válida')

def imprimir_menu():
    """
    Imprime por pantalla una lista de opciones

    Params: none

    Return: void
    """
    print('1 - Imprimir la lista de nombres junto con sus iniciales')
    print('2 - Generar códigos de héroes')
    print('3 - Normalizar datos')
    print('4 - Imprimir índice de nombres')
    print('5 - Navegar fichas')
    print('S - Salir')

def stark_menu_principal():
    """
    Imprime el menú de opciones y pide al usuario que ingrese una.

    Params: none

    Return: (type: any)
    - opcion ingresada por el usuario
    """
    imprimir_menu()
    
    opcion = input('\n     Ingrese una opción -> ')
    return opcion

def stark_marvel_app_3(lista_heroes):
    """
    Se encarga de la ejecución principal del programa.

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: void
    """
    mensaje_bienvenida()

    continuar = True

    while (continuar):
        opcion = stark_menu_principal()

        opcion = opcion.upper()

        if (opcion == '1'):
            stark_imprimir_nombres_con_iniciales(lista_heroes)
        elif (opcion == '2'):
            stark_generar_codigos_heroes(lista_heroes)
        elif (opcion == '3'):
            stark_normalizar_datos(lista_heroes)
        elif (opcion == '4'):
            stark_imprimir_indice_nombre(lista_heroes)
        elif (opcion == '5'):
            stark_navegar_fichas(lista_heroes)
        elif (opcion == 'S'):
            print('S')
            mensaje_salida()
            continuar = False
        else:
            mensaje_error()

# ----> EJECUTAR PROGRAMA
stark_marvel_app_3(lista_personajes)