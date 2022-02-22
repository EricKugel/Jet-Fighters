import pygame

from bullet import Bullet

from math import sin, cos, atan, radians, degrees, sqrt

WIDTH = 30
HEIGHT = 30

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

MAXSPEED = 15

pygame.mixer.init()

FIRE = pygame.mixer.Sound("Misc Lasers/Fire 1.mp3")
HIT = pygame.mixer.Sound("Misc Lasers/Hit 1.mp3")

class Jet():
    def __init__(self, color, coords):
        self.color = color
        self.size = (WIDTH, HEIGHT)

        self.x = coords[0]
        self.y = coords[1]

        self.template =  pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.polygon(self.template, pygame.Color(self.color), [(0,0), (WIDTH, HEIGHT / 2), (0, HEIGHT), (WIDTH / 5, HEIGHT / 2)])

        self.rotateAngle = 0
        self.speed = 0
        self.direction = self.rotateAngle
        self.vector = [0,0]

        self.bullets = [] 

        if (self.color == "white"):
            self.textCoords = ((20, 20))
        else:
            self.textCoords = ((20, SCREEN_HEIGHT-60))

        self.font = pygame.font.SysFont('monospace', 48)
        self.score = 0
        self.text = self.font.render(str(self.score), (True), pygame.Color(self.color))
    
    def draw(self, SURFACE):
        SURFACE.blit(self.surface, (self.rect))
        for bullet in self.bullets:
            bullet.draw(SURFACE, self.color)
        SURFACE.blit(self.text, self.textCoords)

    def isTouching(self, point):
        if (abs(self.x - point[0]) < 15 and abs(self.y - point[1]) < 15):
            return True
        else:
            return False

    def update(self):
        self.surface = pygame.transform.rotate(self.template, self.rotateAngle)
        self.rect = self.surface.get_rect()
        
        self.speed = sqrt(self.vector[0] ** 2 + self.vector[1] ** 2)
        if self.vector[0] != 0:
            self.direction = degrees(atan(self.vector[1]/self.vector[0]))
        if self.vector[0] < 0:
            self.direction += 180
        self.x += cos(radians(self.direction)) * self.speed
        self.y -= sin(radians(self.direction)) * self.speed
        self.rect.center = (self.x, self.y)

        # deceleration
        if (self.speed > .3):
            self.speed -= .15
        elif (self.speed < -.3):
            self.speed += .15
        elif (self.speed < .3 and self.speed > -.3):
            self.speed = 0

        # screen wrap
        if (self.rect.left > SCREEN_WIDTH):
            self.rect.right = 0
        elif (self.rect.right < 0):
            self.rect.left = SCREEN_WIDTH
        
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.bottom = 0
        elif (self.rect.bottom < 0):
            self.rect.top = SCREEN_HEIGHT

        if self.speed > MAXSPEED:
            self.speed = MAXSPEED

        self.x, self.y = self.rect.center[0], self.rect.center[1]
        
        # scale vector to speed
        self.vector[0] = cos(radians(self.direction)) * self.speed
        self.vector[1] = sin(radians(self.direction)) * self.speed

        for bullet in self.bullets:
            life = bullet.update()
            if (life == -1):
                self.bullets.remove(bullet)

    def accelerate(self, backwards = False):
        angle = self.rotateAngle

        if backwards:
            angle += 180

        xDelta = cos(radians(angle)) * .5
        yDelta = sin(radians(angle)) * .5

        self.vector[0] += xDelta
        self.vector[1] += yDelta
         
    def decelerate(self):
        self.accelerate(backwards = True)

    def shoot(self):
        if len(self.bullets) < 2:
            pygame.mixer.Sound.play(FIRE)
            direction = self.rotateAngle * -1
            bullet = Bullet(direction, self.x, self.y)
            self.bullets.append(bullet)

    def point(self):
        self.score += 1
        self.text = self.font.render(str(self.score), (True), pygame.Color(self.color))

    def hit(self):
        pygame.mixer.Sound.play(HIT)
