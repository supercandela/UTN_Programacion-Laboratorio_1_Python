import pygame
import Colours

class Settings:
    def __init__(self):
        """
        Constructor de la clase Settings.
        Esta clase va a crear la pantalla de puntajes más altos.

        Params: None

        Return: Void
        """
        self.font = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Tetris.ttf', 50)
        self.title = self.font.render('Settings', True, (Colours.WHITE))
        self.title_position = (10, 10)
        self.main_menu = None
        self.fps = 5
    
    def update(self, events) -> object:
        """
        Actualiza los atributos de la clase.

        Params:
        - events: (type: eventos) eventos de teclado o mouse capturados por el loop principal

        Return: self
        """
        #Recorro los eventos y le asigno acciones a cada evento diferente
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return self.main_menu
        return self

    def draw(self, screen):
        """
        Dibuja en la pantalla los elementos o atributos de la clase

        Params:
        - screen: (type: pantalla) 

        Return: Void
        """
        screen.blit(self.title, self.title_position)