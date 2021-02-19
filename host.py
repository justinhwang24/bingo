import pygame 
import sys 
import random

pygame.init() 
pygame.font.init()
pygame.display.init()

RES = (720, 720)
SCREEN = pygame.display.set_mode(RES)
WIDTH = SCREEN.get_width() 
HEIGHT = SCREEN.get_height()
SIZE = 75

WHITE = (255, 255, 255)
BLUE = (3, 152, 252) 
TEAL = (0, 160, 181) 
DARK_TEAL = (0, 79, 89) 
YELLOW = (252, 206, 3)
BLACK = (0, 0, 0)

smallfont = pygame.font.SysFont('Helvetica', 30) 
midfont = pygame.font.SysFont('Helvetica', 45) 
bigfont = pygame.font.SysFont('Helvetica', 70)
numbers = []

text = smallfont.render('Generate!', True, WHITE)

def main():

    image = pygame.image.load('logo.png')
    numbers.append(" ")

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
                if WIDTH/2-320 <= mouse[0] <= WIDTH/2-220 and HEIGHT/2-320 <= mouse[1] <= HEIGHT/2-280: 
                    import start
                    start.main()
                else:
                    generate_num()
        
        pygame.draw.rect(SCREEN, YELLOW, [WIDTH/2 - 100, HEIGHT/2 - 200, 200, 200])
        num_text = bigfont.render(str(numbers[-1]), True, BLACK)
        SCREEN.blit((num_text), (WIDTH/2 - 30, HEIGHT/2 - 120))
        char_text = midfont.render(get_letter(numbers[-1]), True, BLACK)
        SCREEN.blit((char_text), (WIDTH/2 - 15, HEIGHT/2 - 175))

        # if hovering on a button, change to a lighter shade  
        if WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2+100 <= mouse[1] <= HEIGHT/2+140: 
            pygame.draw.rect(SCREEN, TEAL, [WIDTH/2 - 70, HEIGHT/2 + 100, 140, 40])
        else: 
            pygame.draw.rect(SCREEN, DARK_TEAL, [WIDTH/2 - 70, HEIGHT/2 + 100, 140, 40])

        if WIDTH/2-320 <= mouse[0] <= WIDTH/2-220 and HEIGHT/2-320 <= mouse[1] <= HEIGHT/2-280: 
            pygame.draw.rect(SCREEN, TEAL,[WIDTH/2 - 320, HEIGHT/2 - 320, 100, 40])
        else: 
            pygame.draw.rect(SCREEN, DARK_TEAL,[WIDTH/2 - 320, HEIGHT/2 - 320, 100, 40])

        go_back = smallfont.render("Back", True, WHITE)
        SCREEN.blit(go_back, (WIDTH/2 - 300, HEIGHT/2 - 310))
        SCREEN.blit(text, (WIDTH/2 - 52, HEIGHT/2 + 110))
        
        pygame.display.update()

def generate_num():
    if len(numbers) < 75:
        num = random.randint(1, 75)
        while num in numbers:
            num = random.randint(1, 75)
        numbers.append(num)
    else:
        numbers.append("Done")

def get_letter(num):
    if num in range (16):
        return "B"
    elif num in range (16, 31):
        return "I"
    elif num in range (31, 46):
        return "N"
    elif num in range (46, 61):
        return "G"
    elif num in range (61, 76):
        return "O"

main()