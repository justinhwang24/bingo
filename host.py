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

def main():
    image = pygame.image.load('logo.png')

    if len(numbers) == 0:
        numbers.append(" ")

    while True: 
        # objects on screen
        SCREEN.fill(BLUE)
        SCREEN.blit(image, (200, 20))

        pygame.draw.rect(SCREEN, YELLOW, [WIDTH/2 - 100, HEIGHT/2 - 200, 200, 200])
        num_text = bigfont.render(str(numbers[-1]), True, BLACK) # get number
        SCREEN.blit((num_text), (WIDTH/2 - 30, HEIGHT/2 - 120))
        list_numbers() # show generated numbers

        char_text = midfont.render(get_letter(numbers[-1]), True, BLACK) # get letter of number
        SCREEN.blit((char_text), (WIDTH/2 - 15, HEIGHT/2 - 175))

        go_back_text = smallfont.render("Back", True, WHITE) # back button
        SCREEN.blit(go_back_text, (WIDTH/2 - 300, HEIGHT/2 - 310))

        generate_text = smallfont.render('Generate!', True, WHITE)
        SCREEN.blit(generate_text, (WIDTH/2 - 52, HEIGHT/2 + 110))

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
                elif WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2+100 <= mouse[1] <= HEIGHT/2+140: 
                    generate_num()

        # if hovering on a button, change to a lighter shade  
        if WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2+100 <= mouse[1] <= HEIGHT/2+140: 
            pygame.draw.rect(SCREEN, TEAL, [WIDTH/2 - 70, HEIGHT/2 + 100, 140, 40])
        else: 
            pygame.draw.rect(SCREEN, DARK_TEAL, [WIDTH/2 - 70, HEIGHT/2 + 100, 140, 40])

        if WIDTH/2-320 <= mouse[0] <= WIDTH/2-220 and HEIGHT/2-320 <= mouse[1] <= HEIGHT/2-280: 
            pygame.draw.rect(SCREEN, TEAL,[WIDTH/2 - 320, HEIGHT/2 - 320, 100, 40])
        else: 
            pygame.draw.rect(SCREEN, DARK_TEAL,[WIDTH/2 - 320, HEIGHT/2 - 320, 100, 40])
        
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

def list_numbers():
    x = 0
    if len(numbers) >= 10:
        x = 10
    else:
        x = len(numbers)
    for i in range (1, 10):
        pygame.draw.rect(SCREEN, TEAL, [WIDTH/2 - 320, HEIGHT/2 + (i-4) * 60, 100, 50])
    for i in range (1, x):
        num_text = midfont.render(str(numbers[-i]), True, WHITE)
        SCREEN.blit((num_text), (WIDTH/2 - 300, HEIGHT/2 + (i-4) * 60 + 20))

main()