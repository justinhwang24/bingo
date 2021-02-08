import pygame 
import sys 
import random

RES = (720,720)
SCREEN = pygame.display.set_mode(RES)

WHITE = (255, 255, 255)
BLUE = (3, 152, 252) 
TEAL = (0, 160, 181) 
DARK_TEAL = (0, 79, 89) 
YELLOW = (252, 206, 3)

def main():
    # initializing the constructor 
    pygame.init() 
    pygame.font.init()
    
    width = SCREEN.get_width() 
    height = SCREEN.get_height()
    
    smallfont = pygame.font.SysFont('Helvetica', 35) 
    textfont = pygame.font.SysFont('Helvetica', 50)
    
    text = smallfont.render('Start', True , WHITE)
    text1 = smallfont.render('By Justin Vincent David', True, (209, 237, 255))

    image = pygame.image.load('logo.png')

    while True: 
        # objects on screen
        SCREEN.fill(BLUE)
        draw_grid()
        SCREEN.blit(image, (200, 20))

        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit() 
                sys.exit
        
        pygame.display.update()
    
def draw_grid():
    size = 75
    for x in range (2, 7):
        for y in range (2, 7):
            rectangle = pygame.Rect(x * size + 5, y * size + 40, size, size)
            pygame.draw.rect(SCREEN, YELLOW, rectangle, 5)

main()