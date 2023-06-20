import pygame
import Colours
import random
# from Grid import Grid
# from Block import Block

#BLOCKS
BLOCKS = [
    #LINEA
    [[0, 1, 2, 3], [1, 5, 9, 13]],
    #CUADRADO
    [[1, 2, 5, 6]],
    #LETRA S - DOS EN DOS - 1
    [[1, 2, 4, 5], [1, 5, 6, 10]],
    #LETRA Z - DOS EN DOS - 2
    [[0, 1, 5, 6], [2, 5, 6, 9]],
    #LETRA J
    [[0, 1, 2, 6], [2, 6, 9, 10], [4, 8, 9, 10], [0, 1, 4, 8]],
    #LETRA L
    [[0, 4, 8, 9], [0, 1, 2, 4], [1, 2, 6, 10], [6, 8, 9, 10]],
    #LETRA T
    [[5, 8, 9, 10], [0, 4, 5, 8], [0, 1, 2, 5], [2, 5, 6, 10]]
]

COLOR_BLOQUE = [Colours.RED,
                Colours.YELLOW,
                Colours.MAGENTA,
                Colours.GREEN,
                Colours.BLUE,
                Colours.ORANGE,
                Colours.CYAN]

#Clase Block
class Block:
    def __init__(self, x, y):
        """
        Constructor.
        Parámetros: self, posición x, posición y
        """
        self.x = x
        self.y = y
        self.type = random.randint(0 , len(BLOCKS) - 1)
        self.rotation = 0
        self.colour = COLOR_BLOQUE[self.type]

    def shape(self):
        """
        Basado en las dos propiedades type y rotation, define sobre la lista blocks cuál elemento muestra de la matriz.
        Type selecciona cuál forma va a utilizar.
        Rotation selecciona cuál vista de las posibles rotaciones.
        """
        return BLOCKS[self.type][self.rotation]

class GamePlay:
    def __init__(self, screen):
        """
        Constructor de la clase MainMenu.
        Esta clase va a crear el menú principal.

        Params:
        - screen: (type: surface)

        Return: Void
        """
        self.main_menu = None

        #GRID
        # Tamaño de cada cuadrado de la grilla
        self.grid_size = 30
        # Número de columnas
        self.number_cols = (screen.get_width() - 300) // self.grid_size
        # Número de filas
        self.number_rows = screen.get_height() // self.grid_size
        # Espacio restante que se suma a derecha e izquierda de la grilla
        self.x_gap = (screen.get_width() - self.number_cols * self.grid_size) // 2
        # Espacio restante que se suma a arriba y abajo de la grilla
        self.y_gap = (screen.get_height() - self.number_rows * self.grid_size) // 2

        #GameBoard
        #Tablero de fondo
        self.game_board = []
        #Inicializo el Game Board en negro
        for i in range(self.number_cols):
            new_col = []
            for j in range(self.number_rows):
                new_col.append(Colours.BLACK)
            self.game_board.append(new_col)

        #BLOQUE
        #Instancio el bloque, le paso como parámetros el lugar inicial del bloque
        self.block = Block((self.number_cols - 1) // 2, 0)
        self.next_block = Block((self.number_cols - 1) // 2, 0)
        self.next_block_rect = [535, 80, 240, 240]

        self.fps = 5
        self.score = 0
        self.lines = 0
        self.level = 1
        #Para cuando los bloques tocan arriba de la pantalla
        self.game_finished = False

        #Textos
        self.font = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 30)
        self.text_next_block = self.font.render('Next:', False, (Colours.LIGHT_GREY))
        self.text_next_block_position = (550, 90)

        self.text_score = self.font.render('Score:', False, (Colours.LIGHT_GREY))
        self.text_score_position = (550, 380)

        self.text_lines = self.font.render('Lines:', False, (Colours.LIGHT_GREY))
        self.text_lines_position = (550, 530)

        self.text_level = self.font.render('Level:', False, (Colours.LIGHT_GREY))
        self.text_level_position = (550, 680)

        #GAME OVER
        self.font_game_over = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 60)
        self.game_finished_text = self.font_game_over.render('Game Over', False, Colours.PURPLE)
        self.game_finished_text_position = (((screen.get_width() - 300) // 2 - self.game_finished_text.get_width() // 2) + self.grid_size, 
                                            (screen.get_height() // 2 - self.game_finished_text.get_height() // 2))
        
        #BOTON BACK
        self.text_colour = Colours.WHITE
        self.button_colour = Colours.BLUE
        self.button_hover_colour = Colours.MAGENTA
        self.button_width = 50
        self.button_height = 20
        self.button_rect = [screen.get_width() - self.button_width,
                            0,
                            self.button_width,
                            self.button_height]
        self.button_font = pygame.font.SysFont('Arial', 15)
        self.button_text = self.button_font.render('Pause', True, self.text_colour)
        self.mouse_x, self.mouse_y = (0,0)

    def draw_grid(self, screen):
        """
        Dibuja la grilla base para cargar las formas.

        Params:
        - rows: (type: int) Número de filas
        - cols: (type: int) Número de columnas
        - grid_size: (type: int) Tamaño de cada cuadrado de la grilla
        - x_gap: (type: int) Espacio restante que se suma a derecha e izquierda de la grilla
        - y_gap: (type: int) Espacio restante que se suma a arriba y abajo de la grilla

        Return: void
        """
        for y in range(self.number_rows): #Rows
            for x in range(self.number_cols): #Cols
                pygame.draw.rect(screen, Colours.GRID_GREY, 
                                [x * self.grid_size + self.grid_size, y * self.grid_size + self.y_gap, self.grid_size, self.grid_size], 1)
                if self.game_board[x][y] is not Colours.BLACK:
                    pygame.draw.rect(screen, self.game_board[x][y], 
                                    [x * self.grid_size + self.grid_size + 1, y * self.grid_size + self.y_gap + 1, self.grid_size - 1, self.grid_size - 1])
        
    def draw_block(self, screen):
        """
        Dibuja el bloque.
        Recorre la matriz de 4 x 4 con los dos for anidados.
        """
        for y in range(4):
            for x in range(4):
                # Revisa si el valor existe en la instancia del bloque que estamos chequeando. Si existe, dibuja el cuadrado que corresponde.
                # Este if aplana el valor de la matriz que estamos chequeando (la lista blocks)
                if y * 4 + x in self.block.shape():
                    pygame.draw.rect(screen, 
                                    self.block.colour, 
                                    [(x + self.block.x) * self.grid_size + self.grid_size + 1, 
                                    (y + self.block.y) * self.grid_size + self.y_gap + 1,
                                    self.grid_size - 2, 
                                    self.grid_size - 2])
                    
    def draw_next_block(self, screen):
        """
        Dibuja el próximo bloque que va a salir en el panel lateral.
        Recorre la matriz de 4 x 4 con los dos for anidados.
        """
        for y in range(4):
            for x in range(4):
                # Revisa si el valor existe en la instancia del bloque que estamos chequeando. Si existe, dibuja el cuadrado que corresponde.
                # Este if aplana el valor de la matriz que estamos chequeando (la lista blocks)
                if y * 4 + x in self.next_block.shape():
                    pygame.draw.rect(screen, 
                                    self.next_block.colour, 
                                    [(x + self.next_block.x) * self.grid_size + self.grid_size + 1 + 370, 
                                    (y + self.next_block.y) * self.grid_size + self.y_gap + 1 + 170,
                                    self.grid_size - 2, 
                                    self.grid_size - 2])
                    
    def rotate_block(self):
        """
        Cambia el valor de rotation en el objeto Block, de manera que cambie su dibujo en la pantalla.
        Confirma que el bloque no se salga de los límites laterales de la pantalla.
        """
        last_rotation = self.block.rotation
        self.block.rotation = (self.block.rotation + 1) % len(BLOCKS[self.block.type])
        can_rotate = True
        for y in range(4):
            for x in range(4):
                if y * 4 + x in self.block.shape():
                    if self.collides( 0, 0):
                        can_rotate = False

        if not can_rotate:
            self.block.rotation = last_rotation

    def collides(self, next_x: int, next_y: int):
        """
        Chequea si el bloque choca contra el borde inferior o algún objeto en el game_board.
        Le sumo el valor del próximo bloque, porque esta función se llama desde las otras, para evitar que me deje moverlo o que siga cayendo.

        Params:
        - next_x: (type: int) próximo valor de x. Lo sumo al valor actual que chequeo.
        - next_y: (type: int) próximo valor de y. Lo sumo al valor actual que chequeo.
        """
        collision = False
        for y in range(4):
            for x in range(4):
                if y * 4 + x in self.block.shape():
                    #Chequea:
                    # que no salga de la pantalla por arriba
                    # que no salga de la pantalla por abajo
                    # que no salga de la pantalla por el costado izquierdo
                    # que no salga de la pantalla por el costado derecho
                    # que colisione con algún elemento del game_board
                    if (y + self.block.y + next_y < 0) or \
                        (y + self.block.y + next_y > self.number_rows - 1) or \
                        (x + self.block.x + next_x < 0) or \
                        (x + self.block.x + next_x > self.number_cols - 1) or \
                        (self.game_board[x + self.block.x + next_x][y + self.block.y + next_y] is not Colours.BLACK):
                        collision = True
                        break
        
        return collision
    
    def drop_block(self):
        """
        Cambio el valor de y para el bloque, de manera que crezca y el bloque vaya bajando por la pantalla.
        Chequea si llega al final de la pantalla, para detener el movimiento de caída.
        """
        can_drop = True
        for y in range(4):
            for x in range(4):
                if y * 4 + x in self.block.shape():
                    if self.collides(0, 1):
                        can_drop = False
        
        if can_drop:
            self.block.y += 1
        else:
            #Al tocar el fondo, agrego el bloque al game board y lo pinto de verde
            for y in range(4):
                for x in range(4):
                    if y * 4 + x in self.block.shape():
                        self.game_board[x + self.block.x][y + self.block.y] = self.block.colour
        
        return can_drop
    
    def side_move(self, dx: int):
        """
        Muevo el bloque hacia los costados. Modifica el valor de x en el bloque.
        Chequea si llega al borde de los lados de la pantalla, para detener el movimiento a los costados.
        Params:
        -dx: (type:int) -1 si se mueve a la izquierda, 1 si se mueve a la derecha
        """
        can_move = True

        for y in range(4):
            for x in range(4):
                if y * 4 + x in self.block.shape():
                    if self.collides( dx, 0):
                        can_move = False

        if can_move:
            self.block.x +=dx
        else:
            #Si can_move es False, fuerza que el bloque siga cayendo
            self.drop_block()

    def find_lines(self):
        """
        Determina si se forman líneas en pantalla.
        """
        lines = 0
        for y in range(self.number_rows):
            empty = 0
            for x in range(self.number_cols):
                if self.game_board[x][y] == Colours.BLACK:
                    empty += 1
            if empty == 0:
                lines += 1
                for y2 in range(y, 1, -1):
                    for x2 in range(self.number_cols):
                        self.game_board[x2][y2] = self.game_board[x2][y2 - 1]
        
        return lines
                
    def update(self, events) -> object:
        """
        Actualiza los atributos de la clase.

        Params:
        - events: (type: eventos) eventos de teclado o mouse capturados por el loop principal
        - screen: (type: surface)

        Return: self
        """
        #Recorro los eventos y le asigno acciones a cada evento diferente
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_x, self.mouse_y = event.pos
                if self.button_rect[0] <= self.mouse_x <= self.button_rect[0] + self.button_rect[2] and \
                    self.button_rect[1] <= self.mouse_y <= self.button_rect[1] + self.button_rect[3]:
                    return self.main_menu
            if event.type == pygame.MOUSEMOTION:
                self.mouse_x, self.mouse_y = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rotate_block()
            #Muevo los bloques a los costados
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.side_move(-1)
                if event.key == pygame.K_RIGHT:
                    self.side_move(1)

        return self

    def draw(self, screen):
        """
        Dibuja en la pantalla los elementos o atributos de la clase

        Params:
        - screen: (type: surface)

        Return: Void
        """
        #Título en la pantalla
        # screen.blit(self.title, self.title_position)

        #Boton Atrás
        if self.button_rect[0] <= self.mouse_x <= self.button_rect[0] + self.button_rect[2] and \
            self.button_rect[1] <= self.mouse_y <= self.button_rect[1] + self.button_rect[3]:
            pygame.draw.rect(screen, self.button_hover_colour, self.button_rect)
        else:
            pygame.draw.rect(screen, self.button_colour, self.button_rect)

        screen.blit(self.button_text, 
                    (self.button_rect[0] + (self.button_width - self.button_text.get_width()) / 2,
                     self.button_rect[1] + (self.button_height - self.button_text.get_height()) /2))
        
        #GRID - GAMEBOARD
        #Dibuja la grilla y el gameboard
        self.draw_grid(screen)
        
        if self.block is not None:
            self.draw_block(screen)
            #Cae el bloque, sólo si no lo estoy moviendo
            # if event.type != pygame.KEYDOWN:
            if not self.drop_block() and not self.game_finished:
                #Chequea si se crearon líneas. Si se crearon, suma el puntaje.
                self.lines = self.find_lines()
                if self.lines > 0:
                    self.score += 100 * self.lines
                self.block = self.next_block
                self.next_block = Block((self.number_cols - 1) // 2, 0)
                if self.collides(0,0):
                    self.game_finished = True

        # font = pygame.font.SysFont('Arial', 25, True, False)
        # text = font.render('Score: ' + str(self.score), True, Colours.WHITE)
        # screen.blit(text, [0, 0])
        if self.game_finished:
            screen.blit(self.game_finished_text, self.game_finished_text_position)

        #Panel Lateral
        #Next Block
        pygame.draw.rect(screen, Colours.GRID_GREY, self.next_block_rect, 2)
        screen.blit(self.text_next_block, self.text_next_block_position)
        self.draw_next_block(screen)

        #Score
        score_rect = [535, 370, 240, 100]
        pygame.draw.rect(screen, Colours.GRID_GREY, score_rect, 2)
        screen.blit(self.text_score, self.text_score_position)
        live_score = self.font.render(str(self.score), False, Colours.LIGHT_GREY)
        screen.blit(live_score, [740 - live_score.get_width(), 
                                 score_rect[1] + score_rect[3] - live_score.get_height() - 25])

        #Lines
        lines_rect = [535, 520, 240, 100]
        pygame.draw.rect(screen, Colours.GRID_GREY, lines_rect, 2)
        screen.blit(self.text_lines, self.text_lines_position)
        live_lines = self.font.render(str(self.lines), False, Colours.LIGHT_GREY)
        screen.blit(live_lines, [740 - live_lines.get_width(), 
                                 lines_rect[1] + lines_rect[3] - live_lines.get_height() - 25])

        #Level
        level_rect = [535, 670, 240, 100]
        pygame.draw.rect(screen, Colours.GRID_GREY, level_rect, 2)
        screen.blit(self.text_level, self.text_level_position)
        live_level = self.font.render(str(self.lines), False, Colours.LIGHT_GREY)
        screen.blit(live_level, [740 - live_level.get_width(), 
                                 level_rect[1] + level_rect[3] - live_level.get_height() - 25])