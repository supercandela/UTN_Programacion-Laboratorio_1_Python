import pygame
from pygame.locals import *
# import random
import Colours
import Grid

class GameBoard:
    def __init__(self, screen):
        """
        Constructor de la clase GameBoard. Esta clase hereda de la clase Grid.
        Sobre la grilla de fondo, crea el tablero donde se van a ir acomodando los bloques al caer y tocar el fondo.

        Params:
        - screen: (type: surface)
        """
        Grid.Grid.__init__(self, screen)
        self.game_board = []
        # Inicializa el Game Board en negro
        for i in range(self.number_cols):
            new_col = []
            for j in range(self.number_rows):
                new_col.append(Colours.BLACK)
                self.game_board.append(new_col)

    def draw(self, screen):
        """
        Dibuja la grilla base para cargar los bloques.
        Dibuja sobre la grilla de fondo, el tablero donde los bloques se van a ir acomodando y creando las filas. 

        Params:
        - screen: (type: surface)
 
        Return: void
        """
        for y in range(self.number_rows): #Rows
            for x in range(self.number_cols): #Cols
                pygame.draw.rect(screen, Colours.GRID_GREY, 
                                [x * self.grid_size + self.grid_size, y * self.grid_size + self.y_gap, self.grid_size, self.grid_size], 1)
                if self.game_board[x][y] is not Colours.BLACK:
                    print('grid con color')
                    pygame.draw.rect(screen, self.game_board[x][y], 
                                    [x * self.grid_size + self.grid_size + 1, y * self.grid_size + self.y_gap + 1, self.grid_size - 1, self.grid_size - 1])

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





# #Instancio el bloque, le paso como parámetros el lugar inicial del bloque
# block = Block( (number_cols - 1) // 2, 0)





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