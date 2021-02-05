import pygame 
import sys 
  
# initializing the constructor 
pygame.init() 
pygame.font.init()
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 

color = (255,255,255) 
color_light = (0, 160, 181) 
color_dark = (0, 79, 89) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Helvetica', 35) 
textfont = pygame.font.SysFont('Helvetica', 50) 
textfont1 = pygame.font.SysFont('Helvetica', 35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('Start', True , color) 
textsurface = textfont.render('BINGO!', True, (209, 237, 255))
textsurface1 = textfont1.render('By Justin Vincent David', True, (209, 237, 255))

while True: 
    # fills the screen with a color 
    screen.fill((3, 152, 252)) 
    screen.blit(textsurface, dest=(300,50))
    screen.blit(textsurface1, dest=(225,100))
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get(): 
        
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-50 <= mouse[1] <= height/2-10: 
                pygame.quit()
                # TODO - START
      
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-50 <= mouse[1] <= height/2-10: 
        pygame.draw.rect(screen,color_light,[width/2 - 70, height/2 - 50, 140, 40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2 - 70, height/2 - 50, 140, 40]) 
      
    # superimposing the text onto our button 
    screen.blit(text, (width/2 - 35, height/2 - 43)) 
      
    # updates the frames of the game 
    pygame.display.update()