import pygame
pygame.init()
surface = pygame.display.set_mode((400, 400))
surface.fill((255, 255, 255)) #white
Green = (0, 255, 0)
Red = (255, 0, 0)   
pygame.draw.circle(surface, Green, (300, 300), 50)
pygame.draw.circle(surface, Red, (100, 100), 50, 50)
pygame.display.flip()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
pygame.quit()