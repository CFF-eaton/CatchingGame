import pygame
import os
import random


class Object ():
    def __init__(self, Object_height,Object_width):

        self.rect = pygame.Rect(random.randint(50,850),0,Object_width,Object_height)

        self.velocity = 5

    def updateX(self, x_diff):
        self.rect.x += x_diff
    
    def updateY(self, y_diff):
        self.rect.y += y_diff
    def ifTouchPlayer(self,object_list):
        if self.rect.colliderect(self.rect):
            del Object
            score+=1
            return True
    def ifTouchBorder(self,object_list):
        if self.rect.y>900:
            del Object
            lives-=1
            return True
            


class Player:
    def __init__(self):
        self.pos = [450, 800]
        self.dimension = [75, 25]
        self.player_rect = pygame.Rect(self.pos[0], self.pos[1], self.dimension[0], self.dimension[1])




    def draw(self):
        pygame.rect()

    def updateX(self,x_diff):
        self.player_rect.x+=x_diff
    def updateY(self,y_diff):
        self.player_rect.y+=y_diff



# Player
player_one = Player()
Object_one=Object(50,50)
object_two=Object(25,25)
object_3=Object(10,10)
object_list=[Object_one,object_two,object_3]
WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60 #frames per second
score=0
lives=5
object3_velo=5
object2_velo=7
object1_velo=9
player_velo=10
Object_width,Object_height=50,50
PLAYER_WIDTH, PLAYER_HEIGHT = 55,40

pygame.display.set_caption("Catch the stuff")


#define a draw_window function that displays all elements on the screen
def draw_window():
  pygame.draw.rect(WIN,BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
  pygame.draw.rect(WIN,WHITE,player_one.player_rect)
  pygame.draw.rect(WIN,RED,Object_one.rect)
  pygame.draw.rect(WIN,YELLOW,object_two.rect)
  pygame.draw.rect(WIN,WHITE,object_3.rect)

  



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
        if player_one.player_rect.x>player_velo:
            player_one.updateX(0-player_velo)
        else:
            pass
    if keys_pressed[pygame.K_RIGHT]:
        if player_one.player_rect.x<900-player_one.dimension[0]-player_velo:
            player_one.updateX(0+player_velo)
        else :
            pass
    Object_one.updateY(0+object1_velo)
    object_two.updateY(0+object2_velo)
    object_3.updateY(0+object3_velo)
    Object_one.ifTouchBorder(object_list)
    object_two.ifTouchBorder(object_list)
    object_3.ifTouchBorder(object_list)
    Object_one.ifTouchPlayer(object_list)
    object_two.ifTouchPlayer(object_list)
    object_3.ifTouchPlayer(object_list)
    draw_window()
    pygame.display.update()
    


    
    

pygame.quit()