import pygame
import Colours

class MainMenu:
    def __init__(self, screen):
        """
        Constructor de la clase MainMenu.
        Esta clase va a crear el menú principal.

        Params:
        - screen: (type: pantalla)

        Return: Void
        """
        self.font = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Tetris.ttf', 80)
        self.title = self.font.render('Tetris', True, (Colours.WHITE))
        self.title_position = (10, 10)
        self.high_scores = None
        self.settings = None
        self.gameplay_scene = None
        self.fps = 5
    
    def update(self, events, screen: None) -> object:
        """
        Actualiza los atributos de la clase.

        Params:
        - events: (type: eventos) eventos de teclado o mouse capturados por el loop principal

        Return: self
        """
        #Recorro los eventos y le asigno acciones a cada evento diferente
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return self.gameplay_scene
                if event.key == pygame.K_h:
                    return self.high_scores
                if event.key == pygame.K_s:
                    return self.settings
        return self

    def draw(self, screen):
        """
        Dibuja en la pantalla los elementos o atributos de la clase

        Params:
        - screen: (type: pantalla) 

        Return: Void
        """
        screen.blit(self.title, self.title_position)