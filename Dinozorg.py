import pygame
import random
from pygame import draw


pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dinozorg')

class Cactus:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            pygame.draw.rect(display, (12, 30, 55),(self.x, self.y, self.width, self.height))
            self.x -= self.speed
            return True
        else:
            # self.x = display_width + 100 + random.randrange(-80, 60)
            return True

    def return_self(self, radius):
        self.x = radius


class Cactus:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    
    def move(self):
        if self.x >= -self.width:
            pygame.draw.rect(display, (12, 30, 55),(self.x, self.y, self.width, self.height))
            self.x -= self.speed
        else:
            self.x = display_width + 50 


usr_width = 60
usr_height = 100
usr_x = display_width / 3
usr_y = display_height - usr_height - 100

cactus_widht = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30

def run_game():
    global make_jump
    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:          
            make_jump = True        

        if make_jump:
            jump()


        display.fill((201, 215, 230))
        draw_array(cactus_arr)


        pygame.draw.rect(display, (240, 120, 100), (usr_x, usr_y, usr_width, usr_height))
        


        pygame.display.update()
        clock.tick(75)


def jump():
    global usr_y, jump_counter, make_jump
    if jump_counter >= -30:
        usr_y -= jump_counter / 2
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_cactus_arr(array):
    array.append(Cactus(display_width + 20, display_height - 170, 20, 70, 4))
    array.append(Cactus(display_width + 300, display_height - 150, 30, 50, 4))
    array.append(Cactus(display_width + 600, display_height - 180, 25, 80, 4))           


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)         

    return radius

def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            radius = find_radius(array)
            cactus.return_self(radius)



run_game()