import pygame
import os
import random

class Boundary():
    def __init__(self):
        self.rect(0,HEIGHT-899,WIDTH,1)

class Object ():
    def __init__(self, Object_height,Object_width):
        #a_surf = pygame.image.load(os.path.join('Assets',img))
        #self.surface = pygame.Rect(dimension)
        self.rect = pygame.Rect(random.randint(0,WIDTH),0,Object_width,Object_height)
       # self.x = self.rect.x
       # self.y = self.rect.y
        self.velocity = 5
    
    def updateX(self, x_diff):
        self.rect.x += x_diff
    
    def updateY(self, y_diff):
        self.rect.y += y_diff
    def ifTouchingPlayer():
        pass

class Player():
    def __init__(self,PLAYER_WIDTH,PLAYER_HEIGHT):
        #self.surface = pygame.Rect(dimension)
        # Create a pygame Rect ojbect
        # Rect(left, top, width, height) -> Rect
        self.rect = pygame.Rect(0,HEIGHT-100,PLAYER_HEIGHT,PLAYER_WIDTH)
        #we do not need to keep track of the position, the rectangle will do that 
        #self.x = WIDTH/2
        #self.y = HEIGHT-100
        
    def updateX(self, x_diff):
        self.rect.x += x_diff
        #self.x += x_diff
    
    def updateY(self, y_diff):
        self.rect.y += y_diff

WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60 #frames per second
lives=3
score=0
object_velo=7
Object_width,Object_height=50,50
PLAYER_WIDTH, PLAYER_HEIGHT = 55,40
NEW_Player=Player(PLAYER_HEIGHT,PLAYER_WIDTH)
pygame.display.set_caption("Catch the stuff")


#define a draw_window function that displays all elements on the screen
def draw_window():
  pygame.draw.rect(WIN,BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
  



game_running = True
while game_running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    #check for all the events that can occur
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running = False
    keys_pressed=pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        Player.updateX(0-5)
    if keys_pressed[pygame.K.RIGHT]:
        Player.updateX(0+5)
    draw_window()
    pygame.display.update()
    


    
    

pygame.quit()