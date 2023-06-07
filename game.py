import pygame
from pygame import display, MOUSEBUTTONDOWN, QUIT
from pygame.image import load
from pygame.sprite import Sprite, Group

superficie = display.set_mode((800, 600), display=0)
display.set_caption('GemForce')
fundo = load('img/fundo_menu_principal.png')

class Carta(Sprite):
    def __init__(self):
        super().__init__()
    
    def update(self):
        ...
class Button(Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Lógica para ação de clique no botão
                print("Botão pressionado!")

logo = Button("img/logo.png", (280, 0))

button_player_2 = Button("img/player_2.png", (80, 340))
button_player_3 = Button("img/player_3.png", (490, 340))
button_player_4 = Button("img/player_4.png", (280, 470))
all_sprites = Group()
all_sprites.add(button_player_2)
all_sprites.add(button_player_3)
all_sprites.add(button_player_4)
all_sprites.add(logo)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        button_player_2.handle_event(event)

    # Espaço do Display
    superficie.blit(
    fundo,   # Imagem
    (0, 0 ), # Posição
    )

    all_sprites.update()
    all_sprites.draw(superficie)
    display.update()

quit()