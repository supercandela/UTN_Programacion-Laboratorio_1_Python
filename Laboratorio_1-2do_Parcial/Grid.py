# # import pygame
# # from pygame.locals import *
# # import random
# # import Colours

# class Grid:
#     def __init__(self, screen):
#         """
#         Constructor de la clase Grid.
#         Crea la grilla donde se va a jugar la partida.

#         Params:
#         - screen: (type: surface)
#         """
#         # Tamaño de cada cuadrado de la grilla
#         self.grid_size = 30
#         # Número de columnas
#         self.number_cols = (screen.get_width() - 300) // self.grid_size
#         # Número de filas
#         self.number_rows = screen.get_height() // self.grid_size
#         # Espacio restante que se suma a derecha e izquierda de la grilla
#         self.x_gap = (screen.get_width() - self.number_cols * self.grid_size) // 2
#         # Espacio restante que se suma a arriba y abajo de la grilla
#         self.y_gap = (screen.get_height() - self.number_rows * self.grid_size) // 2