import pygame
import sys

pygame.init()
screen= pygame.display.set_mode((800, 400))
pygame.display.set_caption("cat")
clock = pygame.time.Clock()
surface = pygame.image.load("images/surface.jpeg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(surface, (0,0))
    pygame.display.update()
    clock.tick(60)
