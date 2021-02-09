import pygame 
import sys
  
# initializing the constructor 
pygame.init() 
pygame.font.init()
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 

WHITE = (255, 255, 255)
BLUE = (3, 152, 252) 
TEAL = (0, 160, 181) 
DARK_TEAL = (0, 79, 89) 
  
# width and height
width = screen.get_width() 
height = screen.get_height()

# fonts
smallfont = pygame.font.SysFont('Helvetica', 35) 
textfont = pygame.font.SysFont('Helvetica', 50) 
textfont1 = pygame.font.SysFont('Helvetica', 35) 
  
# render text
text = smallfont.render('Start', True , WHITE)
text1 = textfont1.render('By Justin Vincent David', True, (209, 237, 255))

image = pygame.image.load('logo.png')

while True: 
    # objects on screen
    screen.fill(BLUE) 
    screen.blit(text1, (225, 180))
    screen.blit(image, (200, 20))
      
    # stores the (x,y) coordinates into the variable as a tuple 
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT:
            pygame.quit() 

        # if mouse clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            # if clicked on button, start game
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-50 <= mouse[1] <= height/2-10: 
                # Start Game

                import game
                game.main()
      
    # if hovering on a button, change to a lighter shade  
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-50 <= mouse[1] <= height/2-10: 
        pygame.draw.rect(screen, TEAL,[width/2 - 70, height/2 - 50, 140, 40])
    else: 
        pygame.draw.rect(screen, DARK_TEAL,[width/2 - 70, height/2 - 50, 140, 40]) 
      
    # place text on button 
    screen.blit(text, (width/2 - 35, height/2 - 43)) 
      
    # updates frames
    pygame.display.update()