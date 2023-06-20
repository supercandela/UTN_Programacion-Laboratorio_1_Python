import pygame
from pygame.locals import *
import random
import Colours
import Grid

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
    def __init__(self, x: int, y:int, screen):
        """
        Constructor de la clase Block. Esta clase hereda de la clase Grid.
        Sobre la grilla de fondo, crea los bloques que van a ir cayendo y el tablero donde se van a ir acomodando los bloques al caer y tocar el fondo.

        Params:
        - x: (type: int) tipo del bloque según BLOCKS
        - y: (type: int) rotación del bloque según BLOCKS
        - screen: (type: surface)
        """
        Grid.Grid.__init__(self, screen)
        self.x = x
        self.y = y
        self.type = random.randint(0 , len(BLOCKS) - 1)
        self.rotation = 0
        self.colour = COLOR_BLOQUE[self.type]
        self.game_board = []
        # Inicializa el Game Board (tablero) en color negro
        for i in range(self.number_cols):
            new_col = []
            for j in range(self.number_rows):
                new_col.append(Colours.BLACK)
                self.game_board.append(new_col)

    def shape(self):
        """
        Basado en las dos propiedades type y rotation, define sobre la lista BLOCKS cuál elemento muestra de la matriz.
        Type selecciona cuál forma va a utilizar.
        Rotation selecciona cuál vista de las posibles rotaciones.
        """
        return BLOCKS[self.type][self.rotation]
    
    def draw(self, screen):
        """
        Dibuja la grilla base para cargar los bloques.
        Dibuja sobre la grilla de fondo, el tablero donde los bloques se van a ir acomodando y creando las filas. 
        Dibuja el bloque, recorriendo la matriz de 4 x 4 con los dos for anidados.

        Params:
        - screen: (type: surface)
 
        Return: void
        """
        self.draw_grid(screen)
        self.draw_block(screen)
    
    def draw_grid(self, screen):
        #Dibuja la grilla y el gameboard
        for y in range(self.number_rows): #Rows
            for x in range(self.number_cols): #Cols
                pygame.draw.rect(screen, Colours.GRID_GREY, 
                                [x * self.grid_size + self.grid_size, y * self.grid_size + self.y_gap, self.grid_size, self.grid_size], 1)
                if self.game_board[x][y] is not Colours.BLACK:
                    print('grid con color')
                    pygame.draw.rect(screen, self.game_board[x][y], 
                                    [x * self.grid_size + self.grid_size + 1, y * self.grid_size + self.y_gap + 1, self.grid_size - 1, self.grid_size - 1])


    def draw_block(self, screen): 
        #Dibuja el bloque
        for y in range(4):
            for x in range(4):
                # Revisa si el valor existe en la instancia del bloque que estamos chequeando. Si existe, dibuja el cuadrado que corresponde.
                # Este if aplana el valor de la matriz que estamos chequeando (la lista blocks)
                if y * 4 + x in self.shape():
                    pygame.draw.rect(screen, 
                                    self.colour, 
                                    [(x + self.x) * self.grid_size + self.grid_size + 1, 
                                    (y + self.y) * self.grid_size + self.y_gap + 1,
                                    self.grid_size - 2, 
                                    self.grid_size - 2])
                    
    def update(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rotate_block()


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
                if y * 4 + x in self.shape():
                    if self.collides( dx, 0):
                        can_move = False

        if can_move:
            self.x +=dx
        else:
            #Si can_move es False, fuerza que el bloque siga cayendo
            self.drop_block()

    def rotate_block(self):
        """
        Cambia el valor de rotation en el objeto Block, de manera que cambie su dibujo en la pantalla.
        Confirma que el bloque no se salga de los límites laterales de la pantalla.
        """
        last_rotation = self.rotation
        self.rotation = (self.rotation + 1) % len(BLOCKS[self.type])
        can_rotate = True
        for y in range(4):
            for x in range(4):
                if y * 4 + x in self.shape():
                    if self.collides( 0, 0):
                        can_rotate = False

        if not can_rotate:
            self.rotation = last_rotation

    def collides(self, next_x: int, next_y: int) -> bool:
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
                if y * 4 + x in self.shape():
                    #Chequea:
                    # que no salga de la pantalla por arriba
                    # que no salga de la pantalla por abajo
                    # que no salga de la pantalla por el costado izquierdo
                    # que no salga de la pantalla por el costado derecho
                    # que colisione con algún elemento del game_board
                    if (y + self.y + next_y < 0) or \
                        (y + self.y + next_y > self.number_rows - 1) or \
                        (x + self.x + next_x < 0) or \
                        (x + self.x + next_x > self.number_cols - 1) or \
                        (self.game_board[x + self.x + next_x][y + self.y + next_y] is not Colours.BLACK):
                        print('colision')
                        collision = True
                        break
        
        return collision

    def drop_block(self) -> bool:
        """
        Cambio el valor de y para el bloque, de manera que crezca y el bloque vaya bajando por la pantalla.
        Chequea si llega al final de la pantalla, para detener el movimiento de caída.
        """
        can_drop = True
        for y in range(4):
            for x in range(4):
                if y * 4 + x in self.shape():
                    if self.collides(0, 1):
                        can_drop = False
        
        if can_drop:
            self.y += 1
        else:
            #Al tocar el fondo, agrego el bloque al game board
            for y in range(4):
                for x in range(4):
                    if y * 4 + x in self.shape():
                        print(self.colour)
                        print(x + self.x)
                        print(y + self.y)
                        print(self.game_board[x + self.x][y + self.y])
                        self.game_board[x + self.x][y + self.y] = self.colour
                        print(self.game_board[x + self.x][y + self.y])
                        print('can_drop: ' + str(can_drop))
        return can_drop


# #Reloj
# clock = pygame.time.Clock()
# #Frames per second
# fps = 5



# score = 0
# font = pygame.font.SysFont('Arial', 25, True, False)

# #GAME OVER
# font_game_over = pygame.font.SysFont('Arial', 50, True, False)
# game_finished_text = font_game_over.render('Game Over', True, RED)
# game_finished_text_position = ((screen.get_width() // 2 - game_finished_text.get_width() // 2), 
#                                (screen.get_height() // 2 - game_finished_text.get_height() // 2))
# game_finished = False

# #LOOP DEL JUEGO
# game_over = False

# #Loop principal del Juego
# while not game_over:
#     clock.tick(fps)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#             #Evita chequear todo lo que viene después, porque ya quiero salir del juego. Es para que no se queje el programa.
#             continue
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 rotate_block()

#     #Muevo los bloques a los costados
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_LEFT:
#             side_move(-1)
#         if event.key == pygame.K_RIGHT:
#             side_move(1)
        
    
#     screen.fill(BLACK)
    
#     #Dibujo la grilla
#     draw_grid(number_cols, number_rows, grid_size, x_gap, y_gap)
#     #Dibujo el bloque
#     if block is not None:
#         draw_block()
#         #Cae el bloque, sólo si no lo estoy moviendo
#         if event.type != pygame.KEYDOWN:
#             if not drop_block() and not game_finished:
#                 #Chequea si se crearon líneas. Si se crearon, suma el puntaje.
#                 created_lines = find_lines()
#                 if created_lines > 0:
#                     score = 100 * created_lines
#                 block = Block((number_cols - 1) // 2, 0)
#                 if collides(0,0):
#                     game_finished = True
    
#     text = font.render('Score: ' + str(score), True, WHITE)
#     screen.blit(text, [0, 0])
#     if game_finished:
#         screen.blit(game_finished_text, game_finished_text_position)
#     pygame.display.update()

# pygame.quit()