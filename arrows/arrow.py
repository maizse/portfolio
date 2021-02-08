import pygame
import random
import os.path

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 500
PICTURE_X = 50
PICTURE_Y = 50

YELLOW = (255,255,0)
SCORE = 0
GOAL = 20

CAPTION = "Tap Tap It"
FONT = "Impact"
FONT_SIZE = 25

LEFTSPEED = 20
RIGHTSPEED = 20
UPSPEED = 20
DOWNSPEED = 20

FPS = 30


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "left_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        self.rect = self.surf.get_rect(bottomleft=(0,SCREEN_HEIGHT))

    def update(self, pressed_keys):
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "left_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        if pressed_keys[K_LEFT]:
           filepath = os.path.dirname(__file__)
           picture = pygame.image.load(os.path.join(filepath, "left.png"))
           self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))


class PlayerRight(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerRight,self).__init__()
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "right_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        self.rect = self.surf.get_rect(bottomleft=(int(SCREEN_WIDTH/1.25),SCREEN_HEIGHT))

    def update(self, pressed_keys):
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "right_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        if pressed_keys[K_RIGHT]:
           filepath = os.path.dirname(__file__)
           picture = pygame.image.load(os.path.join(filepath, "right.png"))
           self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))

class PlayerUp(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerUp,self).__init__()
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "up_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        self.rect = self.surf.get_rect(bottomleft=(int(SCREEN_WIDTH/3.5),SCREEN_HEIGHT))

    def update(self, pressed_keys):
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "up_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        if pressed_keys[K_UP]:
           filepath = os.path.dirname(__file__)
           picture = pygame.image.load(os.path.join(filepath, "up.png"))
           self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))

class PlayerDown(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerDown,self).__init__()
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "down_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        self.rect = self.surf.get_rect(bottomleft=(int(SCREEN_WIDTH/1.85),SCREEN_HEIGHT))

    def update(self, pressed_keys):
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "down_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        if pressed_keys[K_DOWN]:
           filepath = os.path.dirname(__file__)
           picture = pygame.image.load(os.path.join(filepath, "down.png"))
           self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "left_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        self.rect = self.surf.get_rect(midleft=(0,0))


    def update(self):
        self.rect.move_ip(0, LEFTSPEED)
        if pressed_keys[K_LEFT]:
            if pygame.sprite.spritecollide(player, enemies, True):
                self.kill()
                global SCORE
                SCORE += 1

        if self.rect.top>SCREEN_HEIGHT:
            self.kill()
            SCORE -= 1
            if SCORE < 0:
                SCORE = 0


class RightArrow(pygame.sprite.Sprite):
    def __init__(self):
        super(RightArrow, self).__init__()
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "right_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        self.rect = self.surf.get_rect(midleft=(int(SCREEN_WIDTH/1.25),0))


    def update(self):
        self.rect.move_ip(0, RIGHTSPEED) #drop speed x,y
        if pressed_keys[K_RIGHT]:
            if pygame.sprite.spritecollide(playerright, righties, True):
                self.kill()
                global SCORE
                SCORE += 1

        if self.rect.top>SCREEN_HEIGHT:
            self.kill()
            SCORE -= 1
            if SCORE < 0:
                SCORE = 0
            
class UpArrow(pygame.sprite.Sprite):
    def __init__(self):
        super(UpArrow, self).__init__()
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "up_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        self.rect = self.surf.get_rect(midleft=(int(SCREEN_WIDTH/3.5),0))


    def update(self):
        self.rect.move_ip(0, UPSPEED) #drop speed x,y
        if pressed_keys[K_UP]:
            if pygame.sprite.spritecollide(playerup, upies, True):
                self.kill()
                global SCORE
                SCORE += 1

        if self.rect.top>SCREEN_HEIGHT:
            self.kill()
            SCORE -= 1
            if SCORE < 0:
                SCORE = 0

class DownArrow(pygame.sprite.Sprite):
    def __init__(self):
        super(DownArrow, self).__init__()
        filepath = os.path.dirname(__file__)
        picture = pygame.image.load(os.path.join(filepath, "down_white.png"))
        self.surf = pygame.transform.scale(picture, (PICTURE_X, PICTURE_Y))
        self.rect = self.surf.get_rect(midleft=(int(SCREEN_WIDTH/1.85),0))


    def update(self):
        self.rect.move_ip(0, DOWNSPEED) #drop speed x,y
        if pressed_keys[K_DOWN]:
            if pygame.sprite.spritecollide(playerdown, downies, True):
                self.kill()
                global SCORE
                SCORE += 1

        if self.rect.top>SCREEN_HEIGHT:
            self.kill()
            SCORE -= 1
            if SCORE < 0:
                SCORE = 0



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ADDENEMY = pygame.USEREVENT + 1
ADDRIGHT = pygame.USEREVENT + 2
ADDUP = pygame.USEREVENT + 3
ADDDOWN = pygame.USEREVENT + 4

pygame.time.set_timer(ADDRIGHT, random.randint(500, 2500))
pygame.time.set_timer(ADDENEMY, random.randint(1000,2500)) #ms to wait before creating a new one
pygame.time.set_timer(ADDUP, random.randint(2500,3500))
pygame.time.set_timer(ADDDOWN, random.randint(2500,5000))


player = Player()
playerright = PlayerRight()
playerup = PlayerUp()
playerdown = PlayerDown()

enemies = pygame.sprite.Group()
righties = pygame.sprite.Group()
upies = pygame.sprite.Group()
downies = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(playerright)
all_sprites.add(playerup)
all_sprites.add(playerdown)

pygame.display.set_caption(CAPTION)
myfont = pygame.font.SysFont(FONT, FONT_SIZE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        #adding a new Enemy
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDRIGHT:
            new_right = RightArrow()
            righties.add(new_right)
            all_sprites.add(new_right)

        elif event.type == ADDUP:
            new_up = UpArrow()
            upies.add(new_up)
            all_sprites.add(new_up)

        elif event.type == ADDDOWN:
            new_down = DownArrow()
            downies.add(new_down)
            all_sprites.add(new_down)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    playerright.update(pressed_keys)
    playerup.update(pressed_keys)
    playerdown.update(pressed_keys)

    #update enemies position
    enemies.update()
    righties.update()
    upies.update()
    downies.update()

    screen.fill((0,0,0))
    clock = pygame.time.Clock()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    
    if SCORE == GOAL:
        running = False
        pygame.time.wait(3000)
        

    LABEL_SCORE = myfont.render("Score: " + str(SCORE), False, YELLOW)
    screen.blit(LABEL_SCORE, (10,10))

    pygame.display.flip()
    clock.tick(FPS) #fps
