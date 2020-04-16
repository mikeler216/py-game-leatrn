import pygame

# init pygame
from helper import PositionDTO

pygame.init()

_window = pygame.display.set_mode(size=(500, 500))

pygame.display.set_caption("First game")

_rect_position = PositionDTO(x=50, y=50, width=40, height=60, vel=5, )
run: bool = True

while run:
    pygame.time.delay(100)

    for _event in pygame.event.get():
        if _event.type == pygame.QUIT:
            run = False

    _key = pygame.key.get_pressed()

    if _key[pygame.K_LEFT]:
        _rect_position.x -= _rect_position.vel
    if _key[pygame.K_RIGHT]:
        _rect_position.x += _rect_position.vel
    if _key[pygame.K_UP]:
        _rect_position.y -= _rect_position.vel
    if _key[pygame.K_DOWN]:
        _rect_position.y += _rect_position.vel

    _window.fill((0, 0, 0))
    pygame.draw.rect(_window, (255, 0, 0),
                     (_rect_position.x, _rect_position.y, _rect_position.width, _rect_position.height))

    pygame.display.update()
