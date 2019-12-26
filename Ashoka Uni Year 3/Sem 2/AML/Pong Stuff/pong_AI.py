import pygame
import random
from pygame.locals import *

pointcounter = 0

class Pong(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*0.5)

        self.radius = 8

        self.rect = pygame.Rect(self.centerx-self.radius,
                                self.centery-self.radius,
                                self.radius*2, self.radius*2)

        self.color = (255,255,255)

        self.direction = [1,1]
            #speed of ball
        self.speedx = 5
        self.speedy = 5

        self.hit_edge_left = False
        self.hit_edge_right = False

    def update(self, player_paddle, ai_paddle, obstruction):

        global pointcounter
        self.centerx += self.direction[0]*self.speedx
        self.centery += self.direction[1]*self.speedy

        self.rect.center = (self.centerx, self.centery)

        if self.rect.top <= 0:
            self.direction[1] = 1
        elif self.rect.bottom >= self.screensize[1]-1:
            self.direction[1] = -1

        if self.rect.right >= self.screensize[0]-1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True

        if self.rect.colliderect(player_paddle.rect):
            self.direction[0] = -1
            self.direction[1] = self.direction[1] + random.randint(-5,5)
            pointcounter += 1

        if self.rect.colliderect(ai_paddle.rect):
            self.direction[0] = 1
            self.direction[1] = self.direction[1] + random.randint(-5,5)

        if self.rect.colliderect(obstruction.rect):
            self.direction[0] = -1 * self.direction[0]
            self.direction[1] = self.direction[1] + random.randint(-5,5)

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (0,0,0), self.rect.center, self.radius, 1)

#creates the AI paddle
class AIPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = 5
        self.centery = int(screensize[1]*0.5)

        #ai paddle dimensions
        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5),      self.width, self.height)

        self.color = (255,255,255)
        #ai paddle speed
        self.speed = 6

    def update(self, pong):
        if pong.rect.top < self.rect.top:
            self.centery -= self.speed
        elif pong.rect.bottom > self.rect.bottom:
            self.centery += self.speed

        self.rect.center = (self.centerx, self.centery)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

#creates the player paddle
class PlayerPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = screensize[0]-5
        self.centery = int(screensize[1]*0.5)

        #player paddle dimensions
        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5),     self.width, self.height)

        self.color = (255,255,255)

        #player paddle speed
        self.speed = 10
        self.direction = 0

    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

class Obstruction(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*0.5)

        #obstruction dimensions
        self.height = 80
        self.width = 5

        self.rect = pygame.Rect(self.centerx-int(self.width*0.5), self.centery-int(self.height*0.5),     self.width, self.height)

        self.color = (255,255,255)

        #obstruction speed
        self.speed = 10
        self.direction = 0

    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)


def main():

    pygame.init()

    global pointcounter

    screensize = (800,400)

    screen = pygame.display.set_mode(screensize)

    clock = pygame.time.Clock()

    pong = Pong(screensize)
    ai_paddle = AIPaddle(screensize)
    player_paddle = PlayerPaddle(screensize)
    obstruction = Obstruction(screensize)
    central_line = pygame.Rect(800/2, 0, 1, 400)

    running = True

    while running:

        clock.tick(64)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player_paddle.direction = -1
                elif event.key == K_DOWN:
                    player_paddle.direction = 1
            if event.type == KEYUP:
                if event.key == K_UP and player_paddle.direction == -1:
                    player_paddle.direction = 0
                elif event.key == K_DOWN and player_paddle.direction == 1:
                    player_paddle.direction = 0


        ai_paddle.update(pong)
        player_paddle.update()
        pong.update(player_paddle, ai_paddle , obstruction)

        if pong.hit_edge_left:
            print ('You Won')
            running = False
        elif pong.hit_edge_right:
            print ('Your Score')
            print (pointcounter)
            running = False


        screen.fill((0,0,0))

        ai_paddle.render(screen)
        player_paddle.render(screen)
        pong.render(screen)

        obstruction.render(screen)
        pygame.draw.rect(screen,(255,255,255),central_line)

        pygame.display.flip()

    pygame.quit()


main()
