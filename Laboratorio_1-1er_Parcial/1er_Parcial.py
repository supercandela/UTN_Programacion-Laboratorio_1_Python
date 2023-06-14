from data_menu_opciones import menu_opciones
import re
import json
import csv

def generar_separador(patron:str, largo:int, imprimir:bool = True) -> str:
    """
    Genera un string que contiene el patrón especificado,
    repetido tantas veces como la cantidad indicada en el largo,
    un carácter junto a otro, sin salto de línea.
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

def imprimir_dato(dato:str):
    """
    Imprime por consola el parámetro recibido.

    Params:
    - dato: (type: string) texto a imprimir

    Return: void
    """
    print(dato)

def imprimir_menu():
    """
    Imprime por consola las opciones del menú. 
    
    Params: none

    Return: void
    """
    lista_menu = menu_opciones

    for item in lista_menu:
        imprimir_dato(item)

def imprimir_menu_principal() -> int:
    """
    Imprime el menú principal y pide al usuario que ingrese una opción.

    Params: none

    Return: (type: int)
    -(letra): (type: string) si es correcto, la letra elegida por el usuario
    -1: (type: int) si el usuario ingresa un valor inválido
    """
    imprimir_menu()
    
    opcion = input('\n     Ingrese una opción -> ')

    if (re.findall('[1-6]+', opcion)):
        opcion = int(opcion)
        if opcion > 6:
            opcion = -1
    else:
        opcion = -1

    return opcion

def leer_archivo_json(nombre_archivo:str) -> list:
    """
    Abre un archivo de formato JSON en modo lectura y retorna su contenido,
    convertido a una lista de diccionarios.

    Params:
    - nombre_archivo: (type: string) nombre y extensión del archivo a leer. 

    Return: (type: list)
    Lista de diccionarios con el contenido del archivo. 
    """

    dic_json = {}
    archivo = open(nombre_archivo, 'r')
    dic_json = json.load(archivo)
    archivo.close()
    return(dic_json['juegos'])

def sanitizar_entero(numero_str) -> int:
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

def sanitizar_string(valor_str, valor_por_defecto = '-') -> str:
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
    elif (re.findall('[a-zA-Z .]+', valor_str)):
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

def sanitizar_dato(elemento: dict, clave:str, tipo_dato:str) -> bool:
    """
    Sanitiza el dato correspondiente a la clave pasada por parámetro, para
    el diccionario pasado por parámetro, según el tipo de dato que sea, también
    pasado por parámetro. Para eso, llama a las otras funciones. 

    Params:
    - elemento: (type: diccionario) diccionario a procesar
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
        if (clave in elemento):
            valor_a_sanitizar = elemento[clave]
            if (tipo_dato == 'string'):
                nuevo_valor = sanitizar_string(valor_a_sanitizar)
                if (nuevo_valor != 'N/A'):
                    elemento[clave] = nuevo_valor
            elif (tipo_dato == 'entero'):
                nuevo_valor = sanitizar_entero(valor_a_sanitizar)
                if (nuevo_valor > 0):
                    elemento[clave] = nuevo_valor
            
        else:
            print('La clave especificada no existe en el elemento')
    else:
        print('Tipo de dato no reconocido')

    if ( ((type(nuevo_valor) == int or type(nuevo_valor) == float) and nuevo_valor > 0 ) or 
            (type(nuevo_valor) == str and nuevo_valor != 'N/A')):
        retorno = True

    return retorno

def normalizar_datos(lista_a_procesar):
    """
    Recorre la lista y sanitiza los valores de las claves:
    'plataforma', 'modo', 'empresa', 'anio', 'pais' e 'genero'.
    
    Params:
    - lista_a_procesar: (type: list) lista a procesar

    Return: void
    """
    claves_y_tipos = [{'clave': 'plataforma', 'tipo': 'string'},
                      {'clave': 'modo', 'tipo': 'string'},
                      {'clave': 'empresa', 'tipo': 'string'},
                      {'clave': 'anio', 'tipo': 'entero'},
                      {'clave': 'pais', 'tipo': 'string'},
                      {'clave': 'genero', 'tipo': 'string'}]

    if (len(lista_a_procesar) > 0):

        for elemento in lista_a_procesar:

            for index in range(0, len(claves_y_tipos)):
                clave = claves_y_tipos[index]['clave']
                tipo = claves_y_tipos[index]['tipo']
                retorno = sanitizar_dato(elemento, clave, tipo)
                if (retorno == False):
                    print('Error en la normalización')
                    break
        
        generar_separador('*', 50)
        mensaje_datos_normalizados = '\n{0:^50}\n'.format('Datos normalizados')
        imprimir_dato(mensaje_datos_normalizados)
        generar_separador('*', 50)
    else:
        print('Error: Lista a procesar vacía')
        return

def buscar_elementos_por_genero_no_pelea(lista_a_procesar:list, key_a_buscar:str) -> list:
    """
    Buscar elementos por clave en la lista pasada por parámetro

    Params:
    - lista_a_procesar: (type: list) lista de diccionarios a procesar
    - key_a_buscar: (type: str) clave a buscar en los diccionarios de la lista

    Return: type:list
    nueva lista filtrada
    """
    nueva_lista = []
    for elemento in lista_a_procesar:
        if (key_a_buscar in elemento):
            if (re.search(r'\bpelea\b', elemento[key_a_buscar])):
                continue
            else:
                nueva_lista.append(elemento)
        else:
            imprimir_dato('La clave ingresada no figura en los diccionarios de la lista')
            return

    return nueva_lista

def listar_juegos_no_genero_pelea(lista_a_procesar:list):
    """
    Listar por pantalla los juegos cuyo género no contenga la palabra "pelea"
    
    Params:
    - lista_a_procesar: (type: list) lista de diccionarios a procesar
    """
    lista_a_imprimir = buscar_elementos_por_genero_no_pelea(lista_a_procesar, 'genero')

    generar_separador(' *', 50)
    imprimir_dato('\n{0:^100}\n'.format('JUEGOS SIN LA PALABRA "PELEA" EN SU GÉNERO'))
    generar_separador(' *', 50)
    imprimir_dato('\n')
    crear_tabla(lista_a_imprimir)
    imprimir_dato('\n')
    generar_separador(' *', 50)
    imprimir_dato('\n')

    return lista_a_imprimir

def pedir_usuario_ordenamiento() -> int:
    """
    Pide al usuario que ingrese un valor para el ordenamiento y valida si es un entero.

    Params: none

    Return: (type: int)
    int: valor ingresado por el usuario
    -1 : Si el usuario ingresa un valor inválido
    """
    valor_a_retornar = input('¿Cómo prefiere ordenar? 1 - Ascendente / 2 - Descendente -> ')
    imprimir_dato('\n')
    if (re.match('[1-2]+', valor_a_retornar)):
        valor_a_retornar = int(valor_a_retornar)
    else:
        valor_a_retornar = -1
    
    return valor_a_retornar

def ordenar(lista:list, clave:str, tipo:int) -> list:
    """
    Ordena una lista según la clave y criterio indicados por parámetro.

    Params:
    - lista: (type:list) lista a ordenar
    - clave: (type:string) clave a buscar para el ordenamiento
    - tipo: (type:int)
    """
    bandera_swap = True
    while bandera_swap == True:
        bandera_swap = False
        for i in range(len(lista)-1):
            if ( ( tipo == 1 and lista[i][clave] > lista[i+1][clave] ) or
                ( tipo == 2 and lista[i][clave] < lista[i+1][clave] ) ):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

                bandera_swap = True
    
    return lista

def ordenar_y_listar(lista_elementos:list, key_a_ordenar:str) -> list:
    """
    Ordena y lista los elementos de la lista, según la clave obtenida por parámetro.
    Pide al usuario que indique criterio de ordenamiento (asc o desc).
    
    Params:
    - lista_elementos: (type:list) lista a ordenar
    - key_a_ordenar: (type:string) clave que se desea usar para considerar en el ordenamiento

    Return: (type: list)
    - lista ordenada según los criterios pedidos.    
    """
    if (len(lista_elementos) > 0 and key_a_ordenar in lista_elementos[0]):
        ordenamiento = -1

        while (ordenamiento == -1):
            ordenamiento = pedir_usuario_ordenamiento()
            if (ordenamiento > 0):
                lista_ordenada = ordenar(lista_elementos, key_a_ordenar, ordenamiento)

        if (ordenamiento == 1):
            orden = 'ASCENDENTE'
        else:
            orden = 'DESCENDENTE'

        generar_separador(' *', 50)
        imprimir_dato('\n')
        imprimir_dato(f'JUEGOS ORDENADOS POR EMPRESA - ORDEN {orden}'.center(100))
        imprimir_dato('\n')
        generar_separador(' *', 50)
        imprimir_dato('\n')
        crear_tabla(lista_ordenada)
        imprimir_dato('\n')
        generar_separador(' *', 50)
        imprimir_dato('\n')    

        return lista_ordenada

    else:
        imprimir_dato('Lista vacía o clave inexistente')
        return

def seleccionar_modo():
    """
    Pide al usuario que ingrese un valor seleccionar el modo a mostrar.

    Params: none

    Return: (type: int)
    int: valor ingresado por el usuario
    -1 : Si el usuario ingresa un valor inválido
    """
    valor_a_retornar = input('Modo que prefiere mostrar: 1 - Un jugador / 2 - Dos jugadores / 3 - Multijugador / 4 - Cooperativo -> ')
    imprimir_dato('\n')
    if (re.match('[1-4]+', valor_a_retornar)):
        valor_a_retornar = int(valor_a_retornar)
    else:
        valor_a_retornar = -1
    
    return valor_a_retornar

def listar_por_modo(lista_elementos:list, key_a_ordenar:str) -> list:
    """
    Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan dicha búsqueda. (Usando RegitemEx)',

    Params:
    - lista_elementos: (type:list) lista a ordenar
    - key_a_ordenar: (type:string) clave que se desea usar para considerar en el ordenamiento

    Return: (type: list)
    - lista ordenada según los criterios pedidos.  
    """
    if (len(lista_elementos) > 0 and key_a_ordenar in lista_elementos[0]):
        modo_elegido = -1
        nueva_lista = []

        while (modo_elegido == -1):
            modo_elegido = seleccionar_modo()
            if (modo_elegido > 0):
                for elemento in lista_elementos:
                    
                    if ((modo_elegido == 1 and re.search(r'\bun\b', elemento['modo'])) or
                        (modo_elegido == 2 and re.search(r'\bdos\b', elemento['modo'])) or
                        (modo_elegido == 3 and re.search(r'\bmultijugador\b', elemento['modo'])) or
                        (modo_elegido == 4 and re.search(r'\bcooperativo\b', elemento['modo']))):
                        nueva_lista.append(elemento)

            if (modo_elegido == 1):
                modo_elegido = 'Un jugador'
            elif (modo_elegido == 2):
                modo_elegido = 'Dos jugadores'
            elif (modo_elegido == 3):
                modo_elegido = 'Multijugador'
            elif (modo_elegido == 4):
                modo_elegido = 'Cooperativo'

        generar_separador(' *', 50)
        imprimir_dato('\n')
        imprimir_dato(f'JUEGOS ORDENADOS POR MODO - {modo_elegido}'.center(100))
        imprimir_dato('\n')
        generar_separador(' *', 50)
        imprimir_dato('\n')
        crear_tabla(nueva_lista)
        imprimir_dato('\n')
        generar_separador(' *', 50)
        imprimir_dato('\n')    

        return nueva_lista

    else:
        imprimir_dato('Lista vacía o clave inexistente')
        return

def guardar_csv(lista:list):
    """
    Exportar a CSV la lista ordenada según opción elegida anteriormente [1-3]

    Params:
    - lista: (type:list) lista a procesar

    Return: void
    """
    if (len(lista) > 0):
        keys = lista[0].keys()

        with open('lista_juegos.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(lista)

        generar_separador(' *', 50)
        imprimir_dato('\n')
        imprimir_dato(f'ARCHIVO GENERADO'.center(100))
        imprimir_dato('\n')
        generar_separador(' *', 50)
        imprimir_dato('\n')

def ingresar_anio():
    """
    Pide al usuario que ingrese un año para mostrar los juegos de esa década

    Params: none

    Return: (type: int)
    int: valor ingresado por el usuario
    -1 : Si el usuario ingresa un valor inválido
    """
    valor_a_retornar = input('Ingrese un año -> ')
    imprimir_dato('\n')
    if (re.match('[0-9]+', valor_a_retornar)):
        valor_a_retornar = int(valor_a_retornar)
    else:
        valor_a_retornar = -1
    
    return valor_a_retornar

def mostrar_juegos_por_decada(lista_elementos:list) -> list:
    """
    Calcular y mostrar la cantidad de juegos de una década determinada, la misma será ingresada por el usuario por pantalla

    Params:
    - lista_elementos: (type:list) lista a ordenar

    Return: (type:list)
    - lista con los elementos filtrados
    """
    if (len(lista_elementos) > 0):
        anio_elegido = -1
        nueva_lista = []

        while (anio_elegido == -1):
            anio_elegido = ingresar_anio()
            if (anio_elegido > 1959 and anio_elegido < 2023):
                anio_elegido = str(anio_elegido)
                for elemento in lista_elementos:
                    anio_juego = str(elemento['anio'])
                    if ((re.search(r'\b(196[0-9])\b', anio_elegido)) and (re.search(r'\b(196[0-9])\b', anio_juego)) or
                        (re.search(r'\b(197[0-9])\b', anio_elegido)) and (re.search(r'\b(197[0-9])\b', anio_juego)) or
                        (re.search(r'\b(198[0-9])\b', anio_elegido)) and (re.search(r'\b(198[0-9])\b', anio_juego)) or
                        (re.search(r'\b(199[0-9])\b', anio_elegido)) and (re.search(r'\b(199[0-9])\b', anio_juego)) or
                        (re.search(r'\b(200[0-9])\b', anio_elegido)) and (re.search(r'\b(200[0-9])\b', anio_juego)) or
                        (re.search(r'\b(201[0-9])\b', anio_elegido)) and (re.search(r'\b(201[0-9])\b', anio_juego)) or
                        (re.search(r'\b(202[0-9])\b', anio_elegido)) and (re.search(r'\b(202[0-9])\b', anio_juego))):
                        nueva_lista.append(elemento)
                
                generar_separador(' *', 50)
                imprimir_dato('\n')
                imprimir_dato(f'JUEGOS ORDENADOS POR DÉCADA - AÑO ELEGIDO {anio_elegido}'.center(100))
                imprimir_dato('\n')
                generar_separador(' *', 50)
                imprimir_dato('\n')
                crear_tabla(nueva_lista)
                imprimir_dato('\n')
                generar_separador(' *', 50)
                imprimir_dato('\n')

                return nueva_lista
    
            else:
                generar_separador(' *', 50)
                imprimir_dato('\n{0:^100}\n'.format('Año ingresado incorrecto. Ingrese un año entre 1960 y el actual'))
                generar_separador(' *', 50)

    else:
        imprimir_dato('Lista vacía o clave inexistente')
        return

def crear_tabla(lista_elementos:list) -> list:
    """
    Crea una tabla con los elementos de la lista de diccionarios recibida por parámetro.
    
    Params:
    - lista_elementos: (type:list) lista de diccionarios a 

    Return: (type:list)
    - lista con los elementos filtrados
    """
    linea_encabezados = ''
    linea_encabezados += '{0:<4}'.format('ID')
    linea_encabezados += '{0:<25}'.format('NOMBRE')
    linea_encabezados += '{0:<20}'.format('PLATAFORMA')
    linea_encabezados += '{0:<30}'.format('MODO')
    linea_encabezados += '{0:<20}'.format('EMPRESA')
    linea_encabezados += '{0:<6}'.format('AÑO')
    linea_encabezados += '{0:<15}'.format('PAÍS')
    linea_encabezados += '{0:<10}'.format('GÉNERO')                                                                       
    
    print(linea_encabezados)

    for elemento in lista_elementos:
        nueva_linea = ''
        nueva_linea += '{0:<4}'.format(elemento['id'])
        nueva_linea += f'{elemento["nombre"].capitalize().ljust(25)[:25]}'
        nueva_linea += f'{elemento["plataforma"].capitalize().ljust(20)[:20]}'
        nueva_linea += f'{elemento["modo"].capitalize().ljust(30)[:30]}'
        nueva_linea += f'{elemento["empresa"].capitalize().ljust(20)[:20]}'
        nueva_linea += '{0:<6}'.format(elemento['anio'])
        nueva_linea += f'{elemento["pais"].capitalize().ljust(15)[:15]}'
        nueva_linea += f'{elemento["genero"].capitalize().ljust(10)[:10]}'
        
        print(nueva_linea)

def ejecutar_app(lista_juegos:list):
    """
    Se encarga de la ejecución principal del programa.

    Params:
    - lista_juegos: (type: list) lista a procesar

    Return: void
    """
    generar_separador(' *', 50)
    titulo = '\n{0:^100}\n'.format('PRIMER PARCIAL')
    imprimir_dato(titulo)
    generar_separador(' *', 50)

    continuar = True
    lista_a_guardar =[]

    while(continuar):
        imprimir_dato('\n')
        opcion = imprimir_menu_principal()
        imprimir_dato('\n')
        if (opcion == 1):
            lista_aux_1 = lista_juegos.copy()
            lista_a_guardar = listar_juegos_no_genero_pelea(lista_aux_1)
        elif (opcion == 2):
            lista_aux_2 = lista_juegos.copy()
            mostrar_juegos_por_decada(lista_aux_2)
        elif (opcion == 3):
            lista_aux_3 = lista_juegos.copy()
            lista_a_guardar = ordenar_y_listar(lista_aux_3, 'empresa')
        elif (opcion == 4):
            lista_aux_4 = lista_juegos.copy()
            lista_a_guardar = listar_por_modo(lista_aux_4, 'modo')
        elif (opcion == 5):
            if (len(lista_a_guardar) > 0):
                guardar_csv(lista_a_guardar)
            else:
                imprimir_dato('Todavía no generó datos para guardarlos')
        elif (opcion == 6):
            generar_separador(' *', 50)
            mensaje_salida = '\n{0:^100}\n'.format('Usted está saliendo del programa')
            imprimir_dato(mensaje_salida)
            generar_separador(' *', 50)
            continuar = False
        elif (opcion == -1):
            generar_separador(' *', 50)
            mensaje_error = '\n{0:^100}\n'.format('|||||||||| ERROR ||||||||||')
            mensaje_opcion_valida = '\n{0:^100}\n'.format('Debe ingresar una opción válida')
            imprimir_dato(mensaje_error)
            imprimir_dato(mensaje_opcion_valida)
            generar_separador(' *', 50)


# ----> EJECUTAR
# lista_original_archivo = leer_archivo_json('C:\\Users\\Administrator\\Desktop\\X\\Prog-Labo-1\\Laboratorio_1-1er_Parcial\\data_pp.json')
lista_original_archivo = leer_archivo_json('data_pp.json')

normalizar_datos(lista_original_archivo)

ejecutar_app(lista_original_archivo)