import pygame
import os
from pygame.locals import *

from jet import Jet

pygame.init()
FPS = 24
FramesPerSec = pygame.time.Clock()
SURFACE = pygame.display.set_mode((640,480))
SURFACE.fill(pygame.Color("white"))
pygame.display.set_caption("Jet Vector Demonstration")

player = Jet()

while True:
    SURFACE.fill('gray')

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            os.sys.exit()
          
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rotateAngle += 5
    if keys[pygame.K_RIGHT]:
        player.rotateAngle -= 5
    if keys[pygame.K_UP]:
        player.accelerate()

    player.update()
    player.draw(SURFACE)

    FramesPerSec.tick(FPS)
    pygame.display.update()