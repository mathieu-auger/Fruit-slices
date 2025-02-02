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
life = True
sleep_time = 3
game_over = False
freeze = False
freeze_timer = 0
FRUIT_DISPLAY_TIME = 2000
score = 0
fruit_coupe = False  # Réinitialiser la variable à chaque cycle


def symboles():
    symboles = ['a','z','e','r','t','y','u','i','o','p','q','s','d','f',
            'g','h','j','k','l','m','w','x','c','v','b','n',',',';',':','!','1','2','3','4','5','6','7','8','9','/','*','-',
            '+']
    return random.choice(symboles)


# Fonction pour déterminer le symbole basé sur le fruit
def fonction_symbole(fruit):
    if fruit == 'kiwi':
        return 'k'  # Assigner "k" pour le kiwi
    elif fruit == 'banane':
        return 'b'  # Assigner "b" pour la banane
    elif fruit == 'cherry':
        return 'c'  # Assigner "c" pour la cerise (cherry)
    elif fruit == 'strawberry':
        return 's'  # Assigner "s" pour la fraise (strawberry)
    elif fruit == 'bomb':
        return 'b'  # Assigner "b" pour la bombe
    elif fruit == 'ice':
        return 'i'  # Assigner "i" pour la glace (ice)
    else:
        return symboles()  # Pour les autres fruits, choisir un symbole aléatoire


# Fonction pour gérer la logique de couper les fruits
def cut_fruit(fruit_name):
    global game_over, freeze, freeze_timer, score, fruit_coupe
    if fruit_coupe:
        return  # Si un fruit a déjà été coupé dans ce cycle, ne rien faire
    fruit_coupe = True  # Marquer un fruit comme coupé
    if fruit_name == 'bomb':
        game_over = True
        print("Game over déclenché !")
    elif fruit_name == 'ice':
        freeze = True
        freeze_timer = pygame.time.get_ticks()
        print("Gel déclenché !")
    else:
        score += 10  # Ajouter des points pour chaque fruit coupé
        print(f"{fruit_name} coupé ! Score: {score}")




# Fonction pour vérifier les touches pressées
def check_key_press(symbol, fruit_name):
    global fruit_coupe
    keys = pygame.key.get_pressed()
    if keys[ord(symbol)]:
        cut_fruit(fruit_name)
        fruit_coupe = False

def afficher_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

cherry_img = pygame.image.load("image/cherry.png")
strawberry_img = pygame.image.load("image/strawberry.png")
ice_img = pygame.image.load("image/ice.png")
kiwi_img = pygame.image.load("image/kiwi.png")
bomb_img = pygame.image.load("image/bomb.png")
banane_img = pygame.image.load("image/banane.png")

# Redimensionnement des images
fruits = {
    'cherry': pygame.transform.scale(cherry_img, (100, 100)),
    'strawberry': pygame.transform.scale(strawberry_img, (100, 100)),
    'ice': pygame.transform.scale(ice_img, (100, 100)),
    'kiwi': pygame.transform.scale(kiwi_img, (100, 100)),
    'bomb': pygame.transform.scale(bomb_img, (100, 100)),
    'banane': pygame.transform.scale(banane_img, (100, 100))
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
        s_y = -20    
        fruit_name, fruits_random = random.choice(list(fruits.items()))
        x = random.randint(100, 1180)
        
          # Draw the fruit
    screen.blit(fruits_random, (x, y))


    # Generate a symbol based on the fruit
    random_letter = fonction_symbole(fruit_name)
    letter_text = font.render(str(random_letter), True, (255, 255, 255))

    # Calculate the rectangle size based on the text size
    text_rect = letter_text.get_rect()
    text_rect.topleft = (x, y)
    
    # Draw the rectangle
    pygame.draw.rect(screen, (0, 0, 0), text_rect, 2)
    
    # Draw the letter inside the rectangle
    screen.blit(letter_text, text_rect.topleft)


     # Vérifier si une touche a été pressée pour couper le fruit
    check_key_press(random_letter, fruit_name)

      # Afficher le score
    afficher_score()

    fruits_coupes = {}  # Réinitialiser le dictionnaire à chaque cycle

        #generer un rectangle autour du fruit

        #generer un symbole/lettre aleatoire 
        # integre la lettre/symbole au rectangle
    # screen.blit(fruits_random, (x, y))
    # ecrire = font.render("", True, (255,255,255))
    
    # screen.blit(ecrire,(x , y))
    pygame.display.update()
    pygame.time.Clock().tick(60)
    
        
       
# def score() :


#def combos() :




# def user() :
    




# def lettre_au_hasard():
#     with open("lettre au hasard", "w", encoding = "utf8")as fichier :
#         fichier.write(lettre_au_hasard)