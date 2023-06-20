import pygame
import Colours
import random
from pygame.mixer import Sound

class Settings:
    def __init__(self, screen):
        """
        Constructor de la clase Settings.
        Esta clase va a crear la pantalla de Settings.

        Params: None

        Return: Void
        """
        #Fuentes
        self.font_title = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\8-bit Arcade_In.ttf', 80)
        self.font_title_shadow = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\8-bit Arcade_Out.ttf', 80)

        self.font_headers = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 20)
        self.font_general = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 15)

        #Textos
        self.title = self.font_title.render('Settings', False, (Colours.RED))
        self.title_position = ((screen.get_width() // 2 - self.title.get_width() // 2), 
                               (screen.get_height() - 750))
        
        self.title_shadow = self.font_title_shadow.render('Settings', False, (Colours.GREEN))
        self.title_shadow_position = ((screen.get_width() // 2 - self.title.get_width() // 2),
                                      (screen.get_height() - 750))
        
        self.return_text = self.font_general.render('Press "R" to return', False, (Colours.LIGHT_GREY))
        self.return_text_position = ((screen.get_width() // 2 - self.return_text.get_width() // 2),
                                     (screen.get_height() - 80))

        # self.font = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Tetris.ttf', 50)
        # self.title = self.font.render('Settings', True, (Colours.WHITE))
        # self.title_position = (10, 10)
        self.main_menu = None
        self.fps = 5
        self.music = False
        self.sound_effects = False
        self.sound_effects_sound = Sound('Laboratorio_1-2do_Parcial\\sounds\\lines.wav')
    
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
                if event.key == pygame.K_m:
                    self.music = not self.music
                if event.key == pygame.K_s:
                    self.sound_effects = not self.sound_effects
                    if self.sound_effects:
                        self.sound_effects_sound.play()
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

        #Music Text
        if self.music:
            music_text = self.font_headers.render("Music On (Press 'M' to switch)", False, (Colours.LIGHT_GREY))
            music_text_position = ((screen.get_width() // 2 - music_text.get_width() // 2),
                                   (screen.get_height() - 630))
        else:
            music_text = self.font_headers.render("Music Off (Press 'M' to switch)", False, (Colours.LIGHT_GREY))
            music_text_position = ((screen.get_width() // 2 - music_text.get_width() // 2),
                                   (screen.get_height() - 630))
        screen.blit(music_text, music_text_position)
        
        #Sound Effects Text
        if self.sound_effects:
            sound_effects_text = self.font_headers.render("Sound Effects On (Press 'S' to switch)", False, (Colours.LIGHT_GREY))
            sound_effects_text_position = ((screen.get_width() // 2 - sound_effects_text.get_width() // 2),
                                           (screen.get_height() - 580))
        else:
            sound_effects_text = self.font_headers.render("Sound Effects Off (Press 'S' to switch)", False, (Colours.LIGHT_GREY))
            sound_effects_text_position = ((screen.get_width() // 2 - sound_effects_text.get_width() // 2),
                                           (screen.get_height() - 580))
        screen.blit(sound_effects_text, sound_effects_text_position)
        
        #Return Text
        screen.blit(self.return_text, self.return_text_position)