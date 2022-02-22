import pygame
from math import sin, cos, radians

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

SPEED = 20
RADIUS = 3

class Bullet():
    def __init__(self, direction, x, y):
        self.x, self.y = x, y
        self.direction = direction
        self.life = 0

    def update(self):
        self.x += cos(radians(self.direction)) * SPEED
        self.y += sin(radians(self.direction)) * SPEED
        self.life += 1
        self.rect = pygame.Rect(self.x - RADIUS, self.y - RADIUS, RADIUS * 2, RADIUS * 2)
        
        # screen wrap
        if (self.rect.left > SCREEN_WIDTH):
            self.rect.right = 0
        elif (self.rect.right < 0):
            self.rect.left = SCREEN_WIDTH
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.bottom = 0
        elif (self.rect.bottom < 0):
            self.rect.top = SCREEN_HEIGHT
        self.x, self.y = self.rect.center[0], self.rect.center[1]

        if self.life > 50:
            return -1

    def draw(self, surface, color):
        pygame.draw.circle(surface, color, (self.x, self.y), RADIUS)