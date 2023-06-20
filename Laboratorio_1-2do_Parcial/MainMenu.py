import pygame
import Colours
import random

class MainMenu:
    def __init__(self, screen):
        """
        Constructor de la clase MainMenu.
        Esta clase va a crear el menú principal.

        Params:
        - screen: (type: pantalla)

        Return: Void
        """
        #Fuentes
        self.font_title = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\8-bit Arcade_In.ttf', 220)
        self.font_title_shadow = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\8-bit Arcade_Out.ttf', 220)
        self.font_gameplay = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 28)
        self.font_general = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 20)
        #Textos
        self.title = self.font_title.render('Tetris', False, (Colours.YELLOW))
        self.title_position = ((screen.get_width() // 2 - self.title.get_width() // 2), 
                               (screen.get_height() - 650))
        
        self.title_shadow = self.font_title_shadow.render('Tetris', False, (Colours.PURPLE))
        self.title_shadow_position = ((screen.get_width() // 2 - self.title.get_width() // 2), 
                               (screen.get_height() - 650))
        
        self.gameplay_text_text = self.font_gameplay.render('Play Game - Press "Space bar"', False, (Colours.LIGHT_GREY))
        self.gameplay_text_position = ((screen.get_width() // 2 - self.gameplay_text_text.get_width() // 2), 
                                       (screen.get_height() - 400))
        
        self.high_scores_text = self.font_general.render('High Scores - Press "H"', False, (Colours.LIGHT_GREY))
        self.high_scores_text_position = ((screen.get_width() // 2 - self.high_scores_text.get_width() // 2), 
                                          (screen.get_height() - 300))
        
        self.settings_text = self.font_general.render('Settings - Press "S"', False, (Colours.LIGHT_GREY))
        self.settings_text_position = ((screen.get_width() // 2 - self.settings_text.get_width() // 2), 
                                       (screen.get_height() - 260))


        #Otras Pantallas
        self.gameplay_scene = None
        self.settings = None
        self.high_scores = None
        self.fps = 5
    
    def update(self, events) -> object:
        """
        Actualiza los atributos de la clase.

        Params:
        - events: (type: eventos) eventos de teclado o mouse capturados por el loop principal

        Return: (type: object) Clase con la pantalla a mostrar a continuación
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
        title_random = random.randint(0, 1)
        if title_random == 0:
            screen.blit(self.title_shadow, self.title_shadow_position)
        else:
            screen.blit(self.title, self.title_position)

        # screen.blit(self.title_shadow, self.title_shadow_position)
        screen.blit(self.gameplay_text_text, self.gameplay_text_position)
        screen.blit(self.high_scores_text, self.high_scores_text_position)
        screen.blit(self.settings_text, self.settings_text_position)