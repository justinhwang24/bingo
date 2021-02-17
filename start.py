import pygame 
import sys

pygame.init() 
pygame.font.init()

res = (720,720)
screen = pygame.display.set_mode(res) 

WHITE = (255, 255, 255)
BLUE = (3, 152, 252) 
TEAL = (0, 160, 181) 
DARK_TEAL = (0, 79, 89) 

width = screen.get_width() 
height = screen.get_height()

# fonts
smallfont = pygame.font.SysFont('Helvetica', 35) 
textfont = pygame.font.SysFont('Helvetica', 50) 
textfont1 = pygame.font.SysFont('Helvetica', 35) 
  
# render text
text = textfont1.render('By Justin Vincent David', True, (209, 237, 255))
text1 = smallfont.render('Start', True, WHITE)
text2 = smallfont.render('Host', True, WHITE)

def main():
    image = pygame.image.load('logo.png')

    while True: 
        screen.fill(BLUE)
        screen.blit(text, (225, 180))
        screen.blit(image, (200, 20))
        
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit() 

            # if mouse clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                # start game
                if width/2-70 <= mouse[0] <= width/2+70 and height/2-50 <= mouse[1] <= height/2-10: 
                    import game
                    game.main()
                
                # host - generate numbers
                if width/2-70 <= mouse[0] <= width/2+70 and height/2 + 10 <= mouse[1] <= height/2 + 50:
                    import host
                    host.main()
        
        # if hovering on a button, change to a lighter shade  
        if width/2-90 <= mouse[0] <= width/2+90 and height/2-50 <= mouse[1] <= height/2-10: 
            pygame.draw.rect(screen, TEAL,[width/2 - 90, height/2 - 50, 180, 40])
        else: 
            pygame.draw.rect(screen, DARK_TEAL,[width/2 - 90, height/2 - 50, 180, 40])

        if width/2-90 <= mouse[0] <= width/2+90 and height/2 + 10 <= mouse[1] <= height/2 + 50:
            pygame.draw.rect(screen, TEAL, [width/2 - 90, height/2 + 10, 180, 40])
        else: 
            pygame.draw.rect(screen, DARK_TEAL, [width/2 - 90, height/2 + 10, 180, 40])
        
        screen.blit(text1, (width/2 - 35, height/2 - 43))
        screen.blit(text2, (width/2 - 35, height/2 + 20))
        
        # updates frames
        pygame.display.update()

main()