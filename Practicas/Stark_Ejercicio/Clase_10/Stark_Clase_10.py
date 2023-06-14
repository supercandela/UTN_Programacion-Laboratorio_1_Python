from data_menu_opciones import menu_desafio
import re
import json
import csv

def generar_separador(patron, largo, imprimir = True) -> str:
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

def imprimir_menu():
    """
    Imprime por consola las opciones del menú. 
    
    Params: none

    Return: void
    """
    lista_menu = menu_desafio

    for item in lista_menu:
        imprimir_dato(item)

def stark_menu_principal():
    """
    Imprime el menú principal y pide al usuario que ingrese una opción.

    Params: none

    Return:
    -(letra): (type: string) si es correcto, la letra elegida por el usuario
    -1: (type: int) si el usuario ingresa un valor inválido
    """
    imprimir_menu()
    
    opcion = input('\n     Ingrese una opción -> ')

    if (re.findall('[a-zA-Z]+', opcion)):
        opcion = opcion.upper()
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
    return(dic_json['heroes'])

def pedir_cantidad_usuario() -> int:
    """
    Pide al usuario la cantidad que desea imprimir y valida si es un entero. 

    Params: none

    Return: (type: int)
    int: valor ingresado por el usuario
    -1 : Si el usuario ingresa un valor inválido
    """
    valor_a_retornar = input('Ingrese la cantidad que desea imprimir: ')
    imprimir_dato('\n')
    if (re.match('[1-9]+', valor_a_retornar)):
        valor_a_retornar = int(valor_a_retornar)
    else:
        valor_a_retornar = -1
    
    return valor_a_retornar

def listar_cantidad_pedida_heroes(cantidad:int, lista_heroes:list) -> list:
    """
    Listar la cantidad de elementos de la lista pasada por parámetro.

    Params:
    - cantidad: (type: int) cantidad que se desea listar
    - lista_heroes: (type: list) lista a procesar

    Return:
    - list: (type: list) lista de elementos
    - -1: (type: int) en caso de que la cantidad pedida supere el largo de la lista.
    """
    if (cantidad <= len(lista_heroes)):
        valor_a_retornar = []
        for index in range(cantidad):
            heroe = lista_heroes[index]
            valor_a_retornar.append(heroe)
    else:
        valor_a_retornar = -1

    return valor_a_retornar

def pedir_cantidad_y_listar_heroes(lista_heroes:list) -> list:
    """
    Pide al usuario que ingrese un número.
    Imprime por pantalla la cantidad de elementos de la lista solicitados.

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: (type:list)
    - lista filtrada
    """
    opcion = -1

    while (opcion == -1):
        opcion = pedir_cantidad_usuario()

        if (opcion > 0):
            valor_retornado = listar_cantidad_pedida_heroes(opcion, lista_heroes)
            if (type(valor_retornado) == list):
                valor_retornado = valor_retornado
                for elemento in valor_retornado:
                    imprimir_dato(f'NOMBRE HEROE: {elemento["nombre"]}')
            
                return valor_retornado
        
            else:
                imprimir_dato('El valor ingresado supera el largo de la lista. Vuelva a ingresar un valor')
                opcion = valor_retornado

def pedir_usuario_ordenamiento() -> int:
    """
    Pide al usuario que ingrese un valor para el ordenamiento y valida si es un entero.

    Params: none

    Return: (type: int)
    int: valor ingresado por el usuario
    -1 : Si el usuario ingresa un valor inválido
    """
    valor_a_retornar = input('¿Cómo prefiere ordenar? 1 - Ascendente / 2 - Descendente')
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

def ordenar_y_listar_heroes(lista_heroes:list, key_a_ordenar:str) -> list:
    """
    Ordena y lista los elementos de la lista, según la clave obtenida por parámetro.
    Pide al usuario que indique criterio de ordenamiento (asc o desc).
    
    Params:
    - lista_heroes: (type:list) lista a ordenar
    - key_a_ordenar: (type:string) clave que se desea usar para considerar en el ordenamiento

    Return: (type: list)
    - lista ordenada según los criterios pedidos.    
    """
    if (len(lista_heroes) > 0 and key_a_ordenar in lista_heroes[0]):
        ordenamiento = -1

        while (ordenamiento == -1):
            ordenamiento = pedir_usuario_ordenamiento()
            if (ordenamiento > 0):
                lista_ordenada = ordenar(lista_heroes, key_a_ordenar, ordenamiento)
                for elemento in lista_ordenada:
                    imprimir_dato(f'NOMBRE HEROE: {elemento["nombre"]} - {key_a_ordenar.upper()}: {elemento[key_a_ordenar]}')
        
        return lista_ordenada

    else:
        imprimir_dato('Lista vacía o clave inexistente')

def pedir_usuario_clave_promedio() -> int:
    """
    Pide al usuario que ingrese un valor para la clave a promediar y valida si es un entero.

    Params: none

    Return: (type: int)
    int: valor ingresado por el usuario
    -1 : Si el usuario ingresa un valor inválido
    """
    valor_a_retornar = input('¿Qué valor quiere promediar? 1 - Altura / 2 - Peso / 3 - Fuerza')
    imprimir_dato('\n')
    if (re.match('[1-3]+', valor_a_retornar)):
        valor_a_retornar = int(valor_a_retornar)
    else:
        valor_a_retornar = -1
    
    return valor_a_retornar

def obtener_promedio(lista:list, key_a_filtrar:str) -> float:
    """
    Obtiene el promedio de una clave numérica de una lista de diccionarios.

    Params:
    - lista: (type: list) lista de diccionarios a procesar
    - key_a_filtrar: (type: string) clave a buscar en el diccionario

    Return: (type: float)
    Promedio de los valores
    """
    suma = 0
    contador = 0
    if (len(lista) > 0 and key_a_filtrar in lista[0]):
        for elemento in lista:
            suma += elemento[key_a_filtrar]
            contador += 1

    promedio = suma / contador
    return promedio

def pedir_usuario_sobre_o_bajo_promedio() -> int:
    """
    Pide al usuario que ingrese un valor para determinar si se muestran los valores por sobre el promedio o por debajo de él.

    Params: none

    Return: (type: int)
    int: valor ingresado por el usuario - 1 - Debajo del promedio / 2 - Sobre el promedio
    -1 : Si el usuario ingresa un valor inválido
    """
    valor_a_retornar = input('¿Qué héroes quiere mostrar? 1 - Debajo del promedio / 2 - Sobre el promedio')
    imprimir_dato('\n')
    if (re.match('[1-2]+', valor_a_retornar)):
        valor_a_retornar = int(valor_a_retornar)
    else:
        valor_a_retornar = -1
    
    return valor_a_retornar

def elegir_key_promediar_y_mostrar(lista_heroes:list) -> list:
    """
    Pide al usuario que seleccione una característica numérica.
    Calcula el promedio de todos los valores de esa clave. 
    Pide al usuario que elija si quiere mostrar quienes superen o no el promedio.
    Filtrar y mostrar el resultado.

    Params:
    - lista_heroes: (type:list) lista a procesar

    Return: (type: list)
    - lista con los datos filtrados
    """
    nueva_lista_filtrada = []

    # Seleccionar una key numérica
    clave_para_promediar = -1
    while (clave_para_promediar == -1):
        clave_para_promediar = pedir_usuario_clave_promedio()

    if (clave_para_promediar == 1):
        clave_a_usar = 'altura'
    elif (clave_para_promediar == 2):
        clave_a_usar = 'peso'
    elif (clave_para_promediar == 3):
        clave_a_usar = 'fuerza'
    
    # Pide al usuario que elija si quiere mostrar quienes superen o no el promedio.
    sobre_o_bajo_promedio = -1
    while (sobre_o_bajo_promedio == -1):
        sobre_o_bajo_promedio = pedir_usuario_sobre_o_bajo_promedio()

    # Calcula el promedio de todos los valores de esa clave.
    promedio = obtener_promedio(lista_heroes, clave_a_usar)

    for elemento in lista_heroes:
        valor = elemento[clave_a_usar]
        if ((sobre_o_bajo_promedio == 1 and valor <= promedio) or
            (sobre_o_bajo_promedio == 2 and valor >= promedio)):
            nueva_lista_filtrada.append(elemento)

    imprimir_dato(f'Clave elegida: {clave_a_usar.upper()} - Valor Promedio: {promedio}')

    for elemento in nueva_lista_filtrada:
        imprimir_dato(f'NOMBRE HEROE: {elemento["nombre"]} - {clave_a_usar.upper()}: {elemento[clave_a_usar]}')
    
    return nueva_lista_filtrada

def seleccionar_tipo_inteligencia() -> int:
    """
    Pide al usuario que ingrese un valor para determinar el tipo de inteligencia a filtrar.

    Params: none

    Return: (type: int)
    int: valor ingresado por el usuario - 1 - Good / 2 - Average / 3 - High
    -1 : Si el usuario ingresa un valor inválido
    """
    valor_a_retornar = input('¿Qué tipo de inteligencia quiere filtrar? 1 - Good / 2 - Average / 3 - High')
    imprimir_dato('\n')
    if (re.match('[1-3]+', valor_a_retornar)):
        valor_a_retornar = int(valor_a_retornar)
    else:
        valor_a_retornar = -1
    
    return valor_a_retornar

def filtrar_por_inteligencia(lista_heroes:list) -> list:
    """
    Buscar héroes que coincidan con el criterio de búsqueda por inteligencia.

    Params:
    - lista_heroes: (type:list) lista a procesar

    Return: (type: list)
    - lista con los datos filtrados
    """
    if (len(lista_heroes) > 0):
        tipo_inteligencia = -1
        nueva_lista = []

        while (tipo_inteligencia == -1):
            tipo_inteligencia = seleccionar_tipo_inteligencia()

            for heroe in lista_heroes:
                if ((tipo_inteligencia == 1 and re.search(r'\bgood\b', heroe['inteligencia'])) or
                    (tipo_inteligencia == 2 and re.search(r'\baverage\b', heroe['inteligencia'])) or
                    (tipo_inteligencia == 3 and re.search(r'\bhigh\b', heroe['inteligencia']))):
                    nueva_lista.append(heroe)

            if (tipo_inteligencia == 1):
                tipo_inteligencia = 'good'
            elif (tipo_inteligencia == 2):
                tipo_inteligencia = 'average'
            elif (tipo_inteligencia == 3):
                tipo_inteligencia = 'high'
        
        for item in nueva_lista:
            imprimir_dato(f'NOMBRE HEROE: {item["nombre"]} | INTELIGENCIA: {item["inteligencia"]}')
        return nueva_lista
    else:
        imprimir_dato('La lista no contiene elementos')

def guardar_csv(lista_heroes:list):
    """
    Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

    Params:
    - lista_heroes: (type:list) lista a procesar

    Return: void
    """
    if (len(lista_heroes) > 0):
        keys = lista_heroes[0].keys()

        with open('c:\\Users\\Administrator\\Desktop\\Prog-Labo-1\\Stark_Ejercicio\\Clase_10\\data_stark.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(lista_heroes)


def stark_ejecutar_app(lista_heroes:list):
    """
    Se encarga de la ejecución principal del programa.

    Params:
    - lista_heroes: (type: list) lista a procesar

    Return: void
    """
    generar_separador(' *', 50)
    imprimir_dato('\n                    Stark Industries - Desafío Clase 10\n')
    generar_separador(' *', 50)

    continuar = True
    lista_a_guardar = []

    while(continuar):
        opcion = stark_menu_principal()
        imprimir_dato('\n')
        if (opcion == 'A'):
            lista_aux = lista_heroes.copy()
            lista_a_guardar = pedir_cantidad_y_listar_heroes(lista_aux)
        elif (opcion == 'B'):
            lista_aux = lista_heroes.copy()
            lista_a_guardar = ordenar_y_listar_heroes(lista_aux, 'altura')
        elif (opcion == 'C'):
            lista_aux = lista_heroes.copy()
            lista_a_guardar = ordenar_y_listar_heroes(lista_aux, 'fuerza')
        elif (opcion == 'D'):
            lista_aux = lista_heroes.copy()
            lista_a_guardar = elegir_key_promediar_y_mostrar(lista_aux)
        elif (opcion == 'E'):
            lista_aux = lista_heroes.copy()
            lista_a_guardar = filtrar_por_inteligencia(lista_aux)
        elif (opcion == 'F'):
            if (len(lista_a_guardar) > 0):
                guardar_csv(lista_a_guardar)
            else:
                imprimir_dato('Todavía no generó datos para guardarlos')
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
lista_a_usar = leer_archivo_json('c:\\Users\\Administrator\\Desktop\\Prog-Labo-1\\Stark_Ejercicio\\Clase_10\\data_stark.json')

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

stark_normalizar_datos(lista_a_usar)

stark_ejecutar_app(lista_a_usar)