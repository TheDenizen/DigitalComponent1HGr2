import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1300, 700))
pygame.display.set_caption('Turf Wars')
clock = pygame.time.Clock()

blue = (0,0,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    gameDisplay.fill(blue)




    
    pygame.display.update()
    clock.tick(60)



pygame.quit()
quit()