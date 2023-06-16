import pygame
import random
from Colores import *

pygame.init()
screen = pygame.display.set_mode((500,800))
pygame.display.set_caption('Tetris')

grid_size = 30
number_cols = screen.get_width() // grid_size
number_rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - number_cols * grid_size) // 2
y_gap = (screen.get_height() - number_rows * grid_size) // 2

#BLOCKS
blocks = [
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

color_bloque = [RED, YELLOW, MAGENTA, GREEN, BLUE, ORANGE, CYAN]

#Clase Block
class Block:
    def __init__(self, x, y):
        """
        Constructor.
        Parámetros: self, posición x, posición y
        """
        self.x = x
        self.y = y
        self.type = random.randint(0 , len(blocks) - 1)
        self.rotation = 0
        self.colour = color_bloque[self.type]

    def shape(self):
        """
        Basado en las dos propiedades type y rotation, define sobre la lista blocks cuál elemento muestra de la matriz.
        Type selecciona cuál forma va a utilizar.
        Rotation selecciona cuál vista de las posibles rotaciones.
        """
        return blocks[self.type][self.rotation]

def draw_grid(cols: int, rows: int, grid_size: int, x_gap: int, y_gap: int):
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
    for y in range(rows): #Rows
        for x in range(cols): #Cols
            pygame.draw.rect(screen, GRID_GREY, 
                             [x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size], 1)
            if game_board[x][y] is not BLACK:
                pygame.draw.rect(screen, game_board[x][y], 
                                [x * grid_size + x_gap + 1, y * grid_size + y_gap + 1, grid_size - 1, grid_size - 1])

def draw_block():
    """
    Dibuja el bloque.
    Recorre la matriz de 4 x 4 con los dos for anidados.
    """
    for y in range(4):
        for x in range(4):
            # Revisa si el valor existe en la instancia del bloque que estamos chequeando. Si existe, dibuja el cuadrado que corresponde.
            # Este if aplana el valor de la matriz que estamos chequeando (la lista blocks)
            if y * 4 + x in block.shape():
                pygame.draw.rect(screen, 
                                 block.colour, 
                                 [(x + block.x) * grid_size + x_gap + 1, 
                                  (y + block.y) * grid_size + y_gap + 1,
                                  grid_size - 2, 
                                  grid_size - 2])

def rotate_block():
    """
    Cambia el valor de rotation en el objeto Block, de manera que cambie su dibujo en la pantalla.
    Confirma que el bloque no se salga de los límites laterales de la pantalla.
    """
    last_rotation = block.rotation
    block.rotation = (block.rotation + 1) % len(blocks[block.type])
    can_rotate = True
    for y in range(4):
        for x in range(4):
            if y * 4 + x in block.shape():
                if collides( 0, 0):
                    can_rotate = False

    if not can_rotate:
        block.rotation = last_rotation

def collides(next_x: int, next_y: int):
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
            if y * 4 + x in block.shape():
                #Chequea:
                # que no salga de la pantalla por arriba
                # que no salga de la pantalla por abajo
                # que no salga de la pantalla por el costado izquierdo
                # que no salga de la pantalla por el costado derecho
                # que colisione con algún elemento del game_board
                if (y + block.y + next_y < 0) or \
                    (y + block.y + next_y > number_rows - 1) or \
                    (x + block.x + next_x < 0) or \
                    (x + block.x + next_x > number_cols - 1) or \
                    (game_board[x + block.x + next_x][y + block.y + next_y] is not BLACK):
                    collision = True
                    break
    
    return collision

def drop_block():
    """
    Cambio el valor de y para el bloque, de manera que crezca y el bloque vaya bajando por la pantalla.
    Chequea si llega al final de la pantalla, para detener el movimiento de caída.
    """
    can_drop = True
    for y in range(4):
        for x in range(4):
            if y * 4 + x in block.shape():
                if collides(0, 1):
                    can_drop = False
    
    if can_drop:
        block.y += 1
    else:
        #Al tocar el fondo, agrego el bloque al game board y lo pinto de verde
        for y in range(4):
            for x in range(4):
                if y * 4 + x in block.shape():
                    game_board[x + block.x][y + block.y] = block.colour
    
    return can_drop

def side_move(dx: int):
    """
    Muevo el bloque hacia los costados. Modifica el valor de x en el bloque.
    Chequea si llega al borde de los lados de la pantalla, para detener el movimiento a los costados.
    Params:
    -dx: (type:int) -1 si se mueve a la izquierda, 1 si se mueve a la derecha
    """
    can_move = True

    for y in range(4):
        for x in range(4):
            if y * 4 + x in block.shape():
                if collides( dx, 0):
                    can_move = False

    if can_move:
        block.x +=dx
    else:
        #Si can_move es False, fuerza que el bloque siga cayendo
        drop_block()

def find_lines():
    """
    Determina si se forman líneas en pantalla.
    """
    lines = 0
    for y in range(number_rows):
        empty = 0
        for x in range(number_cols):
            if game_board[x][y] == BLACK:
                empty += 1
        if empty == 0:
            lines += 1
            for y2 in range(y, 1, -1):
                for x2 in range(number_cols):
                    game_board[x2][y2] = game_board[x2][y2 - 1]
    
    return lines


#Reloj
clock = pygame.time.Clock()
#Frames per second
fps = 8

#Tablero de fondo
game_board = []
#Inicializo el Game Board en negro
for i in range(number_cols):
    new_col = []
    for j in range(number_rows):
        new_col.append(BLACK)
    game_board.append(new_col)

#Instancio el bloque, le paso como parámetros el lugar inicial del bloque
block = Block( (number_cols - 1) // 2, 0)

score = 0
font = pygame.font.SysFont('Arial', 25, True, False)

#GAME OVER
font_game_over = pygame.font.SysFont('Arial', 50, True, False)
game_finished_text = font_game_over.render('Game Over', True, RED)
game_finished_text_position = ((screen.get_width() // 2 - game_finished_text.get_width() // 2), 
                               (screen.get_height() // 2 - game_finished_text.get_height() // 2))
game_finished = False

#LOOP DEL JUEGO
game_over = False

#Loop principal del Juego
while not game_over:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            #Evita chequear todo lo que viene después, porque ya quiero salir del juego. Es para que no se queje el programa.
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate_block()

    #Muevo los bloques a los costados
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            side_move(-1)
        if event.key == pygame.K_RIGHT:
            side_move(1)
        
    
    screen.fill(BLACK)
    
    #Dibujo la grilla
    draw_grid(number_cols, number_rows, grid_size, x_gap, y_gap)
    #Dibujo el bloque
    if block is not None:
        draw_block()
        #Cae el bloque, sólo si no lo estoy moviendo
        if event.type != pygame.KEYDOWN:
            if not drop_block() and not game_finished:
                #Chequea si se crearon líneas. Si se crearon, suma el puntaje.
                created_lines = find_lines()
                if created_lines > 0:
                    score = 100 * created_lines
                block = Block((number_cols - 1) // 2, 0)
                if collides(0,0):
                    game_finished = True
    
    text = font.render('Score: ' + str(score), True, WHITE)
    screen.blit(text, [0, 0])
    if game_finished:
        screen.blit(game_finished_text, game_finished_text_position)
    pygame.display.update()

pygame.quit()