import pygame 
import sys 
import random

RES = (720,720)
SCREEN = pygame.display.set_mode(RES)
SIZE = 75
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

        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit() 
                sys.exit

            # if mouse clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                pair = get_square(mouse)

        
        pygame.display.update()
    
def draw_grid():
    for x in range (2, 7):
        for y in range (2, 7):
            rectangle = pygame.Rect(x * SIZE + 5, y * SIZE + 40, SIZE, SIZE)
            pygame.draw.rect(SCREEN, YELLOW, rectangle, 5)

def get_square(mouse):
    x = mouse[0]
    y = mouse[1]

    for x1 in range (2, 7):
        for y1 in range (2, 7):
            x2 = x1 * SIZE + 5
            y2 = y1 * SIZE + 40
            x3 = x2 + SIZE
            y3 = y2 + SIZE

            if x2 <= x <= x3 and y2 <= y <= y3:
                pair = []
                pair[0] = x1
                pair[1] = y1
                return pair

def update_button():
    pass

main()