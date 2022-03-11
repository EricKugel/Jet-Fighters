import pygame
from math import *

WIDTH = 30
HEIGHT = 30

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Jet():
    # A jet can be represented by a vector. It has a speed and a direction angle.
    def update(self):
        self.surface = pygame.transform.rotate(self.template, self.rotateAngle)
        self.rect = self.surface.get_rect()

        # The vector, self.vector, is in component form. 
        # The x value is self.vector[0] and the y value is self.vector[1]. 
        # This code moves the jet along the vector.
        self.x += self.vector[0]
        self.y -= self.vector[1]
        self.rect.center = (self.x, self.y)

        # The jet's speed can be found by taking the magnitude, sqrt(x^2 + y^2)
        self.speed = sqrt(self.vector[0] ** 2 + self.vector[1] ** 2)

        # The direction can be found using trigonometry. Remember to add 180 degrees if x is negative!
        if self.vector[0] != 0:
            self.direction = degrees(atan(self.vector[1]/self.vector[0]))
        if self.vector[0] < 0:
            self.direction += 180
        
        # To decelerate the jet, we can just reduce the speed.
        if (self.speed > .3):
            self.speed -= .15
        elif (self.speed < -.3):
            self.speed += .15
        elif (self.speed < .3 and self.speed > -.3):
            self.speed = 0
          
        # With the new speed, we can remake the vector.
        self.vector[0] = cos(radians(self.direction)) * self.speed
        self.vector[1] = sin(radians(self.direction)) * self.speed

        # This code just moves the jet to the other side of the screen if it goes too far (screen wrapping).
        if (self.rect.left > SCREEN_WIDTH):
            self.rect.right = 0
        elif (self.rect.right < 0):
            self.rect.left = SCREEN_WIDTH
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.bottom = 0
        elif (self.rect.bottom < 0):
            self.rect.top = SCREEN_HEIGHT
        self.x, self.y = self.rect.center[0], self.rect.center[1]
      
    def accelerate(self):
        accelerationSpeed = 0.5

        # The acceleration vector can be found using trigonometry.
        xDelta = cos(radians(self.rotateAngle)) * accelerationSpeed
        yDelta = sin(radians(self.rotateAngle)) * accelerationSpeed

        # The jet's new vector is found using vector addition, which is just adding each part.
        self.vector[0] += xDelta
        self.vector[1] += yDelta

    # Below is just code to draw and initialize the jet.
    # ----------------------------------------------------------------------
    def __init__(self):
            self.color = pygame.Color("WHITE")
            self.size = (WIDTH, HEIGHT)
    
            self.x, self.y = 100, 200
    
            self.template =  pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.polygon(self.template, pygame.Color(self.color), [
              (0,0), 
              (WIDTH, HEIGHT / 2), 
              (0, HEIGHT), 
              (WIDTH / 5, HEIGHT / 2)
            ])
    
            self.rotateAngle = 0
            self.speed = 0
            self.direction = self.rotateAngle
            self.vector = [0,0]

    def draw(self, SURFACE):
        SURFACE.blit(self.surface, (self.rect))