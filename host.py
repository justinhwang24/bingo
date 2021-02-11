import pygame 
import sys 
import random

pygame.init() 
pygame.font.init()
pygame.display.init()

RES = (720, 720)
SCREEN = pygame.display.set_mode(RES)
SIZE = 75
WHITE = (255, 255, 255)
BLUE = (3, 152, 252) 
TEAL = (0, 160, 181) 
DARK_TEAL = (0, 79, 89) 
YELLOW = (252, 206, 3)
BLACK = (0, 0, 0)
smallfont = pygame.font.SysFont('Helvetica', 35) 
bigfont = pygame.font.SysFont('Helvetica', 50)
numbers = []
pressed = False

text = smallfont.render('Generate!', True, WHITE)

def main():

    width = SCREEN.get_width() 
    height = SCREEN.get_height()

    image = pygame.image.load('logo.png')

    while True: 
        # objects on screen
        SCREEN.fill(BLUE)
        SCREEN.blit(image, (200, 20))
        
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit() 
                sys.exit

            # if mouse clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                generate_num(True)

        pygame.draw.rect(SCREEN, YELLOW, [width/2 - 100, height/2 - 100, 200, 200])

        # if hovering on a button, change to a lighter shade  
        if width/2-70 <= mouse[0] <= width/2+70 and height/2-50 <= mouse[1] <= height/2-10: 
            pygame.draw.rect(SCREEN, TEAL, [width/2 - 70, height/2 - 50, 140, 40])
        else: 
            pygame.draw.rect(SCREEN, DARK_TEAL, [width/2 - 70, height/2 + 100, 140, 40])
    
        SCREEN.blit(text, (width/2 - 35, height/2 + 107))
        
        pygame.display.update()

def generate_num(pressed):
    if pressed:
        num = random.randint(1, 75)
        while num in numbers:
            num = random.randint(1, 75)
        numbers.append(num)
        text = smallfont.render(str(num), True, BLACK)
        SCREEN.blit(text, (3 * SIZE + 5, 3 * SIZE - 40))

main()