import pygame
import Colours
import random

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

        self.font_gameplay = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 28)
        self.font_general = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 20)
        #Textos
        self.title = self.font_title.render('Hall of Fame', False, (Colours.ORANGE))
        self.title_position = ((screen.get_width() // 2 - self.title.get_width() // 2), 
                               (screen.get_height() - 750))
        
        self.title_shadow = self.font_title_shadow.render('Hall of Fame', False, (Colours.BLUE))
        self.title_shadow_position = ((screen.get_width() // 2 - self.title.get_width() // 2),
                                      (screen.get_height() - 750))

        
        self.gameplay_text_text = self.font_gameplay.render('Play Game - Press "Space bar"', False, (Colours.LIGHT_GREY))
        self.gameplay_text_position = ((screen.get_width() // 2 - self.gameplay_text_text.get_width() // 2), 
                                       (screen.get_height() - 350))
        
        self.return_text = self.font_general.render('Press "R" to return', False, (Colours.LIGHT_GREY))
        self.return_text_position = ((screen.get_width() // 2 - self.return_text.get_width() // 2),
                                     (screen.get_height() - 100))

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

        # screen.blit(self.candela_v_text, self.candela_v_text_position)
        # screen.blit(self.gameplay_text_text, self.gameplay_text_position)
        # screen.blit(self.high_scores_text, self.high_scores_text_position)
        screen.blit(self.return_text, self.return_text_position)