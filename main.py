import pygame
import os
from pygame.locals import *

from jet import Jet

pygame.init()
FPS = 24
FramesPerSec = pygame.time.Clock()
SURFACE = pygame.display.set_mode((640,480))
SURFACE.fill(pygame.Color("white"))
pygame.display.set_caption("Jet Fighters")

player1 = Jet("white", (200,400))
player2 = Jet("black", (400,200))

players = [player1, player2]

while True:
    SURFACE.fill('gray')

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            os.sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_SPACE):
                player1.shoot()
            if(event.key == pygame.K_q):
                player2.shoot()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.rotateAngle += 5
    if keys[pygame.K_RIGHT]:
        player1.rotateAngle -= 5
    if keys[pygame.K_UP]:
        player1.accelerate()
    if keys[pygame.K_DOWN]:
        player1.decelerate()

    if keys[pygame.K_w]:
        player2.accelerate()
    if keys[pygame.K_a]:
        player2.rotateAngle += 5
    if keys[pygame.K_d]:
        player2.rotateAngle -= 5
    if keys[pygame.K_s]:
        player2.decelerate()

    for player in players:
        player.update()
        player.draw(SURFACE)

        for bullet in player.bullets:
            for otherPlayer in players:
                if (otherPlayer != player):
                    if otherPlayer.isTouching((bullet.x, bullet.y)):
                        player.point()
                        otherPlayer.hit()
                        player.bullets.remove(bullet)

    FramesPerSec.tick(FPS)
    pygame.display.update()