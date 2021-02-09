import pygame 
import sys 
import random

pygame.init() 
pygame.font.init()

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
clicked = []
numbers = []

def main():
    # initializing the constructor
    
    width = SCREEN.get_width() 
    height = SCREEN.get_height()

    image = pygame.image.load('logo.png')
    generate_board()

    while True: 
        # objects on screen
        SCREEN.fill(BLUE)
        draw_grid()
        SCREEN.blit(image, (200, 20))

        i = 0
        for x in range (0, 5):
            for y in range (0, 5):
                num = numbers[i]
                text = smallfont.render(str(num), True, BLACK)
                SCREEN.blit(text, ((x + 2.2) * SIZE, (y + 2.8) * SIZE))
                i += 1

        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit() 
                sys.exit

            # if mouse clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                pair = get_square(mouse)
                update_button(pair)
        
        pygame.display.update()

def generate_board():
    for x in range (0, 5):
        for y in range (0, 5):
            num = random.randint(15*(x)+1, 15*(x+1)+1)

            while num in numbers:
                num = random.randint(15*(x)+1, 15*(x+1)+1)

            if num != 0:
                numbers.append(num)
    numbers[12] = "Free"

def draw_grid():
    for x in range (2, 7):
        for y in range (2, 7):
            pair = [x, y]
            num = random.randint(25*(x-2)+1, 25*(x-1))
            rectangle = pygame.Rect(x * SIZE + 5, y * SIZE + 40, SIZE, SIZE)
            text = smallfont.render(str(num), True, BLACK)
            SCREEN.blit(text, (x * SIZE + 5, y * SIZE + 40))

            if pair not in clicked:
                pygame.draw.rect(SCREEN, WHITE, rectangle)
                pygame.draw.rect(SCREEN, BLUE, rectangle, 5)
            else:
                pygame.draw.rect(SCREEN, YELLOW, rectangle)
                pygame.draw.rect(SCREEN, BLUE, rectangle, 5)

def get_square(mouse):
    x = mouse[0]
    y = mouse[1]
    pair = []

    for x1 in range (2, 7):
        for y1 in range (2, 7):
            x2 = x1 * SIZE + 5
            y2 = y1 * SIZE + 40
            x3 = x2 + SIZE
            y3 = y2 + SIZE

            if x2 <= x <= x3 and y2 <= y <= y3:
                pair.append(x1)
                pair.append(y1)
                return pair

def update_button(pair):
    if pair != None:
        if pair not in clicked:
            clicked.append(pair)
        else:
            clicked.remove(pair)

main()