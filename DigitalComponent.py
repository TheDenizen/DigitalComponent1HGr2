import pygame

pygame.init()

display_height = 800
display_width = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Turf Wars')
clock = pygame.time.Clock()
blue = (0,0,255)
red = (200,0,0)
black = (0,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
white = (255,255,255)



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(blue)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Turf Wars", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
        
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 

game_intro()
pygame.quit()
quit()