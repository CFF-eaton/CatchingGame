import pygame
import os
import random

pygame.init()
pygame.font.init()


font = pygame.font.Font(None, 36)
WIDTH, HEIGHT = 900, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60

# Set up screen and font
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Stuff")
font = pygame.font.Font(None, 36)

# Score and lives
score = 0
lives = 5

# Object and player velocities
object1_velo = 10
player_velo = 6
class Object ():
    def __init__(self, Object_height,Object_width):
        self.width=Object_width
        self.height=Object_height
        self.rect = pygame.Rect(0,0,Object_width,Object_height)

        self.reset()
    def updateX(self, x_diff):
        self.rect.x += x_diff
    
    def updateY(self, y_diff):
        self.rect.y += y_diff
    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.width)
        self.rect.y = -self.height
    def ifTouchPlayer(self,player_rect):
        if self.rect.colliderect(player_rect):
            self.reset()
            return True
        return False

    def ifTouchBorder(self, screen_height):
        if self.rect.y > screen_height:
            self.reset()
            return True
        return False
            


class Player:
    def __init__(self):
        self.pos = [450, 800]
        self.dimension = [100, 40]
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





pygame.display.set_caption("Catch the stuff")


#define a draw_window function that displays all elements on the screen
def draw_window():
  pygame.draw.rect(WIN,BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
  pygame.draw.rect(WIN,WHITE,player_one.player_rect)
  pygame.draw.rect(WIN,RED,Object_one.rect)
  score_text = font.render(f"Score: {score}", True, WHITE)
  lives_text = font.render(f"Lives: {lives}", True, WHITE)
  WIN.blit(score_text, (10, 10))
  WIN.blit(lives_text, (WIDTH - 120, 10))



  


clock = pygame.time.Clock()
game_running = True
while game_running:
    

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
    

    if Object_one.ifTouchBorder(900):
        lives-=1
    if Object_one.ifTouchPlayer(player_one.player_rect):
        score+=1



    draw_window()
    pygame.display.update()
    
    if lives <= 0:

        pygame.time.delay(2000)
        pygame.quit()
        os._exit(0)


    
    

pygame.quit()