import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The best game ever")

x_coordinate = 400
y_coordinate = 300



running = True
while running == True:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x_coordinate, y_coordinate, 50, 50))
    if event.type == pygame.QUIT:
        break

    button = pygame.key.get_pressed()
    print(x_coordinate, y_coordinate)
    if button[pygame.K_LEFT]:
        x_coordinate -= 1
    if button[pygame.K_RIGHT]:
        x_coordinate += 1
    if button[pygame.K_UP]:
        y_coordinate -= 1
    if button[pygame.K_DOWN]:
        y_coordinate += 1
    if x_coordinate < 0:
        x_coordinate = 0
    if y_coordinate < 0:
        y_coordinate = 0
    pygame.time.Clock().tick(60)
    pygame.display.flip()

