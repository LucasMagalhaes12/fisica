import pygame
from circle import Circle
from time import time

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Fisica")
clock = pygame.time.Clock()


circle = Circle(screen.get_size())


prev = time()
dt = 0
FPS = 0

running = True
mousePressed = False

while running:
    clock.tick()

    now = time()
    dt = now - prev
    prev = now


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle.add(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     mousePressed = False


    screen.fill('white')
    circle.update(screen, dt)

    pygame.display.update()


pygame.quit()
