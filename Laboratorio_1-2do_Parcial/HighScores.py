import pygame
import Colours
import random
import sqlite3

class HighScores:
    def __init__(self, screen):
        """
        Constructor de la clase HighScores.
        Esta clase va a crear la pantalla de puntajes más altos.

        Params: None

        Return: Void
        """
        #Fuentes
        self.font_title = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\8-bit Arcade_In.ttf', 80)
        self.font_title_shadow = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\8-bit Arcade_Out.ttf', 80)

        self.font_headers = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 20)
        self.font_general = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 15)
        #Textos
        self.title = self.font_title.render('Hall of Fame', False, (Colours.ORANGE))
        self.title_position = ((screen.get_width() // 2 - self.title.get_width() // 2), 
                               (screen.get_height() - 750))
        
        self.title_shadow = self.font_title_shadow.render('Hall of Fame', False, (Colours.BLUE))
        self.title_shadow_position = ((screen.get_width() // 2 - self.title.get_width() // 2),
                                      (screen.get_height() - 750))

        
        # self.headers_text = self.font_gameplay.render('Play Game - Press "Space bar"', False, (Colours.LIGHT_GREY))
        # self.headers_position = ((screen.get_width() // 2 - self.gameplay_text_text.get_width() // 2), 
        #                                (screen.get_height() - 350))
        
        self.return_text = self.font_general.render('Press "R" to return', False, (Colours.LIGHT_GREY))
        self.return_text_position = ((screen.get_width() // 2 - self.return_text.get_width() // 2),
                                     (screen.get_height() - 80))

        self.main_menu = None
        self.fps = 5

        self.connection_string = 'Laboratorio_1-2do_Parcial\\db\\tetris_high_scores.db'
        self.table_name = 'tetris_high_scores'
        self.create_db = True
    
    def update(self, events) -> object:
        """
        Actualiza los atributos de la clase.

        Params:
        - events: (type: eventos) eventos de teclado o mouse capturados por el loop principal

        Return: self
        """
        # #Creo la db si no existe
        # if self.create_db:
        #     self.create_table_scores()
        #     self.insert_table_new_data()
        #     self.create_db = False

        #Recorro los eventos y le asigno acciones a cada evento diferente
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return self.main_menu
        return self

    def draw(self, screen):
        """
        Dibuja en la pantalla los elementos o atributos de la clase

        Params:
        - screen: (type: pantalla) 

        Return: Void
        """
        title_random = random.randint(0, 1)
        if title_random == 0:
            screen.blit(self.title_shadow, self.title_shadow_position)
        else:
            screen.blit(self.title, self.title_position)

        high_scores = self.print_high_scores(screen)
        for i in range(11):
            for j in range(5):
                screen.blit(high_scores[i][j][0], high_scores[i][j][1])

        screen.blit(self.return_text, self.return_text_position)

    def create_table_scores(self):
        """
        Crea la tabla inicial para cargar los puntajes más altos
        """
        with sqlite3.connect(self.connection_string) as conexion:
            try:
                sentencia = f"CREATE table {self.table_name} \
                                (\
                                    id integer primary key autoincrement,\
                                    nickname text,\
                                    score int,\
                                    lines int,\
                                    level int\
                                )"
                conexion.execute(sentencia)
                print("Se creo la tabla de high scores")
            except sqlite3.OperationalError:
                print("La tabla high scores ya existe")
    
    def insert_table_new_data(self):
        """
        Inserto 15 valores inventados y standard para cubrir los high scores en la tabla original.
        """
        fake_data = [
            ("Mike Wazowski", 5000, 50, 2),
            ("James P. Sullivan", 4500, 45, 2),
            ("Randall Boggs", 3000, 30, 2),
            ("Celia", 2500, 25, 1),
            ("Roz", 2000, 20, 1),
            ("Fungus", 1500, 15, 1),
            ("The Abominable Snowman", 1000, 10, 1),
            ("Henry J. Waternoose III", 500, 5, 1),
            ("Boo", 300, 3, 1),
            ("George Sanderson", 200, 2, 1)
        ]
        with sqlite3.connect(self.connection_string) as conexion:
            for item in fake_data:
                try:
                    conexion.execute(f"INSERT into {self.table_name} ( nickname, score, lines, level) values (?,?,?,?)", item)
                except:
                    print("Error en la inserción de dato")

    def select_high_scores(self):
        """
        Hace un select a la db y devuelve los 10 puntajes más altos.
        """
        error_message = 'En este momento, no se pueden mostrar los puntajes'
        with sqlite3.connect(self.connection_string) as conexion:
            try:
                #Select all
                # cursor = conexion.execute(f"SELECT * FROM {self.table_name}")
                #Select 10 puntajes más altos
                cursor = conexion.execute(f"SELECT * FROM {self.table_name} \
                                          ORDER BY score DESC \
                                          LIMIT 10")
                return cursor
            except:
                return error_message

    def print_high_scores(self, screen):
        """
        Imprime en pantalla los puntajes más altos

        Params:
        - screen: (type: surface)

        Return: (type:list) lista de tuplas con los valores de texto y posición de cada ítem a imprimir
        """
        scores_to_show = []
        items_cols = []

        posicion_y = 650
        posicion_x_col1 = 100
        posicion_x_col2 = 140
        posicion_x_col3 = 420
        posicion_x_col4 = 560
        posicion_x_col5 = 650

        header1 = self.font_headers.render('{0:<4}'.format('ID'), False, (Colours.MAGENTA))
        header2 = self.font_headers.render('{0:<30}'.format('NICKNAME'), False, (Colours.MAGENTA))
        header3 = self.font_headers.render('{0:^20}'.format('SCORE'), False, (Colours.MAGENTA))
        header4 = self.font_headers.render('{0:^10}'.format('LINES'), False, (Colours.MAGENTA))
        header5 = self.font_headers.render('{0:^10}'.format('LEVEL'), False, (Colours.MAGENTA))

        items_cols = [[header1, (posicion_x_col1, (screen.get_height() - posicion_y))],
                      [header2, (posicion_x_col2, (screen.get_height() - posicion_y))],
                      [header3, (posicion_x_col3, (screen.get_height() - posicion_y))],
                      [header4, (posicion_x_col4, (screen.get_height() - posicion_y))],
                      [header5, (posicion_x_col5, (screen.get_height() - posicion_y))]]
            
        scores_to_show.append(items_cols)
        
        db_scores = self.select_high_scores()
        item_order = 1
        for item in db_scores:
            posicion_y -= 50
            col1 = self.font_headers.render('{0:<4}'.format(item_order), False, (Colours.LIGHT_GREY))
            col2 = self.font_headers.render(f'{item[1].ljust(30)[:30]}', False, (Colours.LIGHT_GREY))
            col3 = self.font_headers.render('{0:^20}'.format(item[2]), False, (Colours.LIGHT_GREY))
            col4 = self.font_headers.render('{0:^10}'.format(item[3]), False, (Colours.LIGHT_GREY))
            col5 = self.font_headers.render('{0:^10}'.format(item[4]), False, (Colours.LIGHT_GREY))

            items_cols = [[col1, (posicion_x_col1, (screen.get_height() - posicion_y))],
                          [col2, (posicion_x_col2, (screen.get_height() - posicion_y))],
                          [col3, (posicion_x_col3, (screen.get_height() - posicion_y))],
                          [col4, (posicion_x_col4, (screen.get_height() - posicion_y))],
                          [col5, (posicion_x_col5, (screen.get_height() - posicion_y))]]
            
            scores_to_show.append(items_cols)
            item_order += 1
        return scores_to_show
    
    def save_game_score(self, score, lines, level):
        """
        Guarda el puntaje obtenido en la base de datos.

        Params:
        - score: (type:int) puntaje obtenido en la partida
        - lines: (type:int) lineas formadas en la partida
        - level: (type:int) nivel alcanzado en la partida
        """
        name = 'Otro Nombre'
        with sqlite3.connect(self.connection_string) as conexion:
            try:
                conexion.execute(f"INSERT into {self.table_name} ( nickname, score, lines, level) values (?,?,?,?)", (name, score, lines, level,))
            except:
                print("Error en la inserción de dato")

    def save_high_scores(self, score, lines, level):
        """
        Chequea si el puntaje hecho en la partida recién finalizada califica para guardarse en el top 10

        Params:
        - score: (type:int) puntaje obtenido en la partida
        - lines: (type:int) lineas formadas en la partida
        - level: (type:int) nivel alcanzado en la partida
        """
        name = 'Candela'
        new_scores = []
        lowers_scores = self.filter_lower_high_scores(score)
        # for element in lowers_scores:
        if len(lowers_scores) >= 1:
            nuevo_elemento_id = lowers_scores[0][0]
            nuevo_elemento_nickname = name
            nuevo_elemento_score = score
            nuevo_elemento_lines = lines
            nuevo_elemento_level = level

            nuevo_elemento = (nuevo_elemento_id, nuevo_elemento_nickname, nuevo_elemento_score, nuevo_elemento_lines, nuevo_elemento_level)

            new_scores.append(nuevo_elemento)

            for element in lowers_scores:
                if element[0] < 10:
                    nuevo_elemento_id = element[0] + 1
                    nuevo_elemento_nickname = element[1]
                    nuevo_elemento_score = element[2]
                    nuevo_elemento_lines = element[3]
                    nuevo_elemento_level = element[4]

                    nuevo_elemento = (nuevo_elemento_id, nuevo_elemento_nickname, nuevo_elemento_score, nuevo_elemento_lines, nuevo_elemento_level)

                    new_scores.append(nuevo_elemento)
                else:
                    lowers_scores.remove(element)

            self.update_values_in_table(new_scores)

    def filter_lower_high_scores(self, score_to_test):
        """
        Hace un select a la db y devuelve los 10 puntajes más altos.

        Params:
        - score_to_test: (type:int) puntaje a confirmar si puedo agregarlo a la db
        """
        error_message = 'En este momento, no se pueden mostrar los puntajes'
        with sqlite3.connect(self.connection_string) as conexion:
            try:
                cursor = conexion.execute(f"SELECT * FROM {self.table_name} \
                                          WHERE score  < {score_to_test}\
                                          ORDER BY score DESC \
                                          LIMIT 10")
                lista = cursor.fetchall()
                return lista
            except:
                return error_message
            
    def update_values_in_table(self, new_scores):
        """
        Actualiza en la db los valores de los puntajes más altos

        Params:
        - new_scores: (type: list) lista de tuplas con los valores a updatear
        """
        with sqlite3.connect(self.connection_string) as conexion:
            for item in new_scores:
                try:
                    sentencia = f"UPDATE {self.table_name} SET nickname = ?, score = ?, lines = ?, level = ? WHERE id = ?"
                    conexion.execute(sentencia, (item[1], item[2], item[3], item[3], item[0],))
                except:
                    print("Error en la inserción de dato")