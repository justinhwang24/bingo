import pygame 
import sys

pygame.init()
pygame.font.init()
pygame.display.init()

RES = (720, 720)
SCREEN = pygame.display.set_mode(RES) 
WIDTH = SCREEN.get_width() 
HEIGHT = SCREEN.get_height()

WHITE = (255, 255, 255)
BLUE = (3, 152, 252) 
TEAL = (0, 160, 181) 
DARK_TEAL = (0, 79, 89) 

# fonts
smallfont = pygame.font.SysFont('Helvetica', 35) 
textfont = pygame.font.SysFont('Helvetica', 50) 
  
# render text
text = smallfont.render('By Justin Vincent David', True, (209, 237, 255))
text1 = smallfont.render('Start', True, WHITE)
text2 = smallfont.render('Host', True, WHITE)

def main():
    image = pygame.image.load('logo.png')

    while True: 
        SCREEN.fill(BLUE)
        SCREEN.blit(text, (225, 180))
        SCREEN.blit(image, (200, 20))
        
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit() 

            # if mouse clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                # start game
                if WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2-50 <= mouse[1] <= HEIGHT/2-10: 
                    import game
                    game.main()
                
                # host - generate numbers
                if WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2 + 10 <= mouse[1] <= HEIGHT/2 + 50:
                    import host
                    host.main()
        
        # if hovering on a button, change to a lighter shade  
        if WIDTH/2-90 <= mouse[0] <= WIDTH/2+90 and HEIGHT/2-50 <= mouse[1] <= HEIGHT/2-10: 
            pygame.draw.rect(SCREEN, TEAL, [WIDTH/2 - 90, HEIGHT/2 - 50, 180, 40])
        else: 
            pygame.draw.rect(SCREEN, DARK_TEAL, [WIDTH/2 - 90, HEIGHT/2 - 50, 180, 40])

        if WIDTH/2-90 <= mouse[0] <= WIDTH/2+90 and HEIGHT/2 + 10 <= mouse[1] <= HEIGHT/2 + 50:
            pygame.draw.rect(SCREEN, TEAL, [WIDTH/2 - 90, HEIGHT/2 + 10, 180, 40])
        else: 
            pygame.draw.rect(SCREEN, DARK_TEAL, [WIDTH/2 - 90, HEIGHT/2 + 10, 180, 40])
        
        SCREEN.blit(text1, (WIDTH/2 - 35, HEIGHT/2 - 43))
        SCREEN.blit(text2, (WIDTH/2 - 35, HEIGHT/2 + 20))
        
        # updates frames
        pygame.display.update()

main()