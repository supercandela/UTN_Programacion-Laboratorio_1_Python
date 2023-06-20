import pygame
import Colours

class Home():
    def __init__(self, screen):
        """
        Constructor de la clase Home.
        Esta clase va a crear la pantalla de inicio del programa.

        Params:
        - screen: (type: surface) 

        Return: Void
        """
        self.image = pygame.image.load('Laboratorio_1-2do_Parcial\\images\\Tetris_Pantalla_Inicio.png')
        self.x = 0
        self.y = 0
        self.frame = 0
        self.sprite_size = 800
        self.font = pygame.font.Font('Laboratorio_1-2do_Parcial\\font\\Minecraft.ttf', 18)
        self.text = self.font.render('(Press any key to continue)', False, (Colours.LIGHT_GREY))
        self.text_rect = self.text.get_rect()
        self.text_position = (310, 700)
        self.main_menu = None
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
                return self.main_menu
        return self

    def draw(self, screen):
        """
        Dibuja en la pantalla los elementos o atributos de la clase
        Parámetros del blit, en orden:
        (la imagen que voy a dibujar,
        [posición en x,
        posición en y,
        tamaño de x que me genera el recorte de la imagen completa,
        tamaño de y que me genera el recorte de la imagen completa],
        (partiendo de la imagen completa esto es desde dónde empiezo a dibujar la imagen en el x de la superficie de la imagen-movimiento del muñeco-,
        partiendo de la imagen completa esto es desde dónde empiezo a dibujar la imagen en el y de la superficie de la imagen-cuál muñeco dibuja-,
        tamaño que dibujo,
        tamaño que dibujo))

        Params:
        - screen: (type: surface) 

        Return: Void
        """
        clock = pygame.time.Clock()
        flip = clock.tick(self.fps)
        if flip % 10 == 0:
            self.flip_frame()

        screen.blit(self.image,
                    [self.x,
                     self.y,
                     self.sprite_size,
                     self.sprite_size],
                     (self.frame * self.sprite_size,
                      self.y,
                      self.sprite_size,
                      self.sprite_size))
        
        screen.blit(self.text, self.text_position)

    def flip_frame(self):
        """
        Intercambia el cuadro del sprite.
        """
        if self.frame == 0:
            self.frame = 1
        elif self.frame == 1:
            self.frame = 2
        else:
            self.frame = 0