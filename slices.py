import pygame
from pygame.locals import *
import random
import math
import sys
import time
import pygame.transform


pygame.init()
screen = pygame.display.set_mode((1280,720))
background = pygame.image.load('image/backgroundresize.jpg')
font = pygame.font.Font(None , 60)


# variables globales 
life = 3
sleep_time = 3
game_over = False
freeze = False
freeze_timer = 0
FRUIT_DISPLAY_TIME = 2000
score = 0
fruit_coupe = False  # Reset variable every cycle


def symboles():
    symboles = ['a','z','e','r','t','y','u','i','o','p','q','s','d','f',
            'g','h','j','k','l','m','w','x','c','v','b','n',',',';',':','!','1','2','3','4','5','6','7','8','9','/','*','-',
            '+']
    return random.choice(symboles)


# Function to determine symbol based on fruit
def fonction_symbole(fruit):
    if fruit == 'kiwi':
        return 'k'  # Assign "k" for the kiwi
    elif fruit == 'banane':
        return 'b'  # Assign "b" for the banana
    elif fruit == 'cherry':
        return 'c'  # Assign "c" for the cherry
    elif fruit == 'strawberry':
        return 's'  # Assign "s" for the strawberry
    elif fruit == 'bomb':
        return 'b'  # Assign "b" for the bomb
    elif fruit == 'ice':
        return 'i'  # Assign "i" for the ice
    # else:
    #     return symboles()  # for the other fruit, choose the symboles


# Function to manage the logic of cutting fruit
def cut_fruit(fruit_name):
    global game_over, freeze, freeze_timer, score, fruit_coupe
    if fruit_coupe:
        return  # If a fruit has already been cut in this cycle, do nothing
    fruit_coupe = True  # Mark a fruit as cut
    if fruit_name == 'bomb':
        game_over = True
        print("Game over déclenché !")
    elif fruit_name == 'ice':
        freeze = True
        freeze_timer = pygame.time.get_ticks()
        print("Gel déclenché !")
    else:
        score += 10  # Add points for each cut fruit
        print(f"{fruit_name} coupé ! Score: {score}")

def Show_life():
    global life
    if not fruit_coupe:
        life -= 1
    if life <= 0 :
        print("GAME OVER")    

def print_life():
    life_text = font.render("Vies: " + str(life), True, (255, 0, 0))  
    screen.blit(life_text, (10, 50))
    

# Function to check pressed keys
def check_key_press(symbol, fruit_name):
    global fruit_coupe
    keys = pygame.key.get_pressed()
    if keys[ord(symbol)]:
        cut_fruit(fruit_name)
        fruit_coupe = False

def show_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

cherry_img = pygame.image.load("image/cherry.png")
strawberry_img = pygame.image.load("image/strawberry.png")
ice_img = pygame.image.load("image/ice.png")
kiwi_img = pygame.image.load("image/kiwi.png")
bomb_img = pygame.image.load("image/bomb.png")
banana_img = pygame.image.load("image/banana.png")

# resize the pictures
fruits = {
    'cherry': pygame.transform.scale(cherry_img, (100, 100)),
    'strawberry': pygame.transform.scale(strawberry_img, (100, 100)),
    'ice': pygame.transform.scale(ice_img, (100, 100)),
    'kiwi': pygame.transform.scale(kiwi_img, (100, 100)),
    'bomb': pygame.transform.scale(bomb_img, (100, 100)),
    'banana': pygame.transform.scale(banana_img, (100, 100))
}
    

y = 720
s_y = -20
x = random.randint(100, 1180)

keepGameRunning = True
fruits_timer = 0
FRUIT_DISPLAY_TIME = 2000

fruit_name, fruits_random = random.choice(list(fruits.items()))
pygame.display.update()


while keepGameRunning:
    if game_over:
        screen.fill((0, 0, 0))
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        keepGameRunning = False
        continue
    

    if freeze:
        if pygame.time.get_ticks() - freeze_timer < 3000:
            pygame.display.update()
            pygame.time.Clock().tick(60)
            continue
        else:
            freeze = False
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGameRunning = False


    s_y += 0.4
    y += s_y
    
    if y > 720:
        
        Show_life()
        s_y = -20    
        fruit_name, fruits_random = random.choice(list(fruits.items()))
        x = random.randint(100, 1180)
        
          # Draw the fruit
    screen.blit(fruits_random, (x, y))


    # Generate a symbol based on the fruit
    random_letter = fonction_symbole(fruit_name)
    letter_text = font.render(str(random_letter),True, (255, 255, 255))

    # Calculate the rectangle size based on the text size
    text_rect = letter_text.get_rect()
    text_rect.topleft = (x, y)
    
    
    # Draw the letter inside the rectangle
    screen.blit(letter_text, text_rect.topleft)


     # Check if a button was pressed to cut the fruit
    check_key_press(random_letter, fruit_name)

      # Show score
    show_score()
    print_life()
    fruits_coupes = {}  # Reset the dictionary every cycle
        
    pygame.display.update()
    pygame.time.Clock().tick(60)