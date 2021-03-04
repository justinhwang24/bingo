import pygame 
import sys 
import random
from variables import palette, colors

pygame.init()
pygame.font.init()
pygame.display.init()

RES = (720, 720)
SCREEN = pygame.display.set_mode(RES)
WIDTH = SCREEN.get_width() 
HEIGHT = SCREEN.get_height()
SIZE = 75

WHITE = (255, 255, 255)
TEAL = (0, 160, 181) 
DARK_TEAL = (0, 79, 89) 
GRAY = (207, 207, 207)

smallfont = pygame.font.SysFont('Helvetica', 30) 
midfont = pygame.font.SysFont('Helvetica', 45) 
bigfont = pygame.font.SysFont('Helvetica', 70)

def main():
    image = pygame.image.load('logo.png')

    while True: 
        # objects on screen
        SCREEN.fill(palette[0])
        SCREEN.blit(image, (200, 20))

        for i in range (len(colors)):
            pygame.draw.circle(SCREEN, colors[i], [100 + i * 60, 300], 35)
            pygame.draw.circle(SCREEN, GRAY, [100 + i * 60, 300], 35, 5)
       
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit

            # if mouse clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print(str(mouse[0]) + " " + str(mouse[1]))
                if WIDTH/2-320 <= mouse[0] <= WIDTH/2-220 and HEIGHT/2-320 <= mouse[1] <= HEIGHT/2-280: 
                    import start
                    start.main()
                elif 265 <= mouse[1] < 335: 
                    i = 0
                    while i < len(colors):
                        if 70 + i * 60 <= mouse[0] < 125 + i * 60:
                            palette[0] = colors[i]
                            break
                        else:
                            i += 1

        # if hovering on a button, change to a lighter shade  
        if WIDTH/2-320 <= mouse[0] <= WIDTH/2-220 and HEIGHT/2-320 <= mouse[1] <= HEIGHT/2-280: 
            pygame.draw.rect(SCREEN, TEAL,[WIDTH/2 - 320, HEIGHT/2 - 320, 100, 40])
        else: 
            pygame.draw.rect(SCREEN, DARK_TEAL,[WIDTH/2 - 320, HEIGHT/2 - 320, 100, 40])
        
        go_back_text = smallfont.render("Back", True, WHITE) # back button
        SCREEN.blit(go_back_text, (WIDTH/2 - 300, HEIGHT/2 - 310))

        background_text = smallfont.render("Background Color", True, WHITE)
        SCREEN.blit(background_text, (85, 210))
        
        pygame.display.update()

main()