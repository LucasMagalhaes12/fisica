import pygame
from circle import Circle

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Fisica")
clock = pygame.time.Clock()


circle = Circle(screen.get_size())

running = True
mousePressed = False

while running:
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
    circle.update(screen)    
    


    pygame.display.update()
    clock.tick(60)


pygame.quit()