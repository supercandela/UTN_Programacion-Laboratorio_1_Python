import pygame
import Colours
from pygame.mixer import Sound

class Game:
    def __init__(self, name: str, w: int, h: int):
        """
        Constructor de la clase Game.
        Esta clase va a crear la pantalla que se va a mostrar.

        Params:
        - name: (type: string) nombre de la pantalla a crear
        - w: (type: int) ancho de la pantalla a crear
        - h: (type: int) alto de la pantalla a crear

        Return: Void
        """
        #Inicializo pygame
        pygame.init()
        #Atributos de la clase
        self.game_name = name
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.game_name)
        pygame_icon = pygame.image.load('Laboratorio_1-2do_Parcial\\images\\Tetris_Icon.png')
        pygame.display.set_icon(pygame_icon)
        self.current_state = None
        self.settings = None
        self.music_sound = Sound('Laboratorio_1-2do_Parcial\\sounds\\PowerGlove-Tetris.mp3')

    def run(self, state:object):
        """
        Método que corre el loop principal del juego.

        Params:
        - state: (type: object) pantalla que se va a mostrar o código que vamos a ejecutar.
        """
        game_over = False
        self.current_state = state
        clock = pygame.time.Clock()
        
        #Loop principal
        while not game_over:
            clock.tick(self.current_state.fps)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    game_over = True
                    #Evita chequear todo lo que viene después, porque ya quiero salir del juego. Es para que no se queje el programa.
                    continue
            
            if self.settings.music:
                self.music_sound.play(1000)
            else:
                self.music_sound.stop()
            #Pantalla a mostrar
            #Fondo negro
            self.screen.fill((Colours.BLACK))
            #Al objeto current_state, lo updateo con los eventos del loop principal
            self.current_state = self.current_state.update(events)
            #Dibujo el objeto current_state en la pantalla
            self.current_state.draw(self.screen)
            #Actualizo la pantalla
            pygame.display.update()

        #Cierro pygame
        pygame.quit()