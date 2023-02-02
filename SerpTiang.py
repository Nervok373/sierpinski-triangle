import time

import pygame
from pygame.locals import *

import sys
import random


# settings
WIDTH = 1400  # ширина экрана
HEIGHT = 1000  # высота экрана
FPS = 0  # кадры в секунду
dotScore = 0
text_color = (255, 255, 255)
text_size = 26

cord = (600, 500)
# [(700, 30), (200, 950), (1300, 900)]
aCord = []

background_color = (5, 5, 10)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF)
pygame.display.set_caption("Triangle")
clock = pygame.time.Clock()

surface_text = pygame.Surface((200, 50))
font_text = pygame.font.SysFont('Aria', text_size)


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1, 1))
        self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

All_sprites = pygame.sprite.Group()
for i in aCord:
    point = Point(*i)
    All_sprites.add(point)

def newPoint():
    global cord
    a = random.choice(aCord)
    #1.75
    newCord = (cord[0]-(cord[0]-a[0])//2, cord[1]-(cord[1]-a[1])//2)
    cord = newCord

    dot = Point(*cord)
    All_sprites.add(dot)

def setAnglePos():
    print("задание углов исходя из положение курсора")
    for i in range(3):
        print(f"расположите курсор на месте {i} угла")
        for j in range(3):
            print(abs(3-j))
            time.sleep(1)

        pygame.event.get()
        aCord.append(pygame.mouse.get_pos())

setAnglePos()

running_main_win = True
while running_main_win:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # проверка на нажатие крестика для выхода
            sys.exit()

    dotScore += 1
    newPoint()
    render_text = font_text.render(f"point: {dotScore}", False, text_color)

    # обновление спрайтов
    All_sprites.update()

    # Отрисовка
    screen.fill(background_color)
    screen.blit(render_text, (10, 10))
    All_sprites.draw(screen)
    pygame.display.flip()
