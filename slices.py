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
life = 3
life = True
sleep_time = 3
font = pygame.font.Font(None , 60)
def symboles(symboles):
    symboles = ['a','z','e','r','t','y','u','i','o','p','q','s','d','f',
            'g','h','j','k','l','m','w','x','c','v','b','n',',',';',':','!','1','2','3','4','5','6','7','8','9','/','*','-',
            '+']

    symbole_aleatoire = random.choice(symboles)
    return symbole_aleatoire


cherry_img = pygame.image.load("image/cherry.png")
strawberry_img = pygame.image.load("image/strawberry.png")
ice_img = pygame.image.load("image/ice.png")
kiwi_img = pygame.image.load("image/kiwi.png")
bomb_img = pygame.image.load("image/bomb.png")
banane_img = pygame.image.load("image/banane.png")

# Redimensionnement des images
fruits = [    
    pygame.transform.scale(cherry_img, (100, 100)),
    pygame.transform.scale(strawberry_img, (100, 100)),
    pygame.transform.scale(ice_img, (100, 100)),
    pygame.transform.scale(kiwi_img, (100, 100)),
    pygame.transform.scale(bomb_img, (100, 100)),
    pygame.transform.scale(banane_img, (100, 100))
]
    

y = 720
s_y = -20
x = random.randint(100, 1180)

keepGameRunning = True
fruits_timer = 0
FRUIT_DISPLAY_TIME = 2000
    
fruits_random = random.choice(fruits)
pygame.display.update()


while keepGameRunning:
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGameRunning = False

    s_y += 0.4
    y += s_y
    
    if y > 720:
        s_y = -20    
        fruits_random = random.choice(fruits)
        x = random.randint(100, 1180)
        
        #generer un rectangle autour du fruit

        #generer un symbole/lettre aleatoire 
        # integre la lettre/symbole au rectangle
    screen.blit(fruits_random, (x, y))
    ecrire = font.render('salut' ,True, (255,255,255))
    
    screen.blit(ecrire,(x , y))
    pygame.display.update()
    pygame.time.Clock().tick(60)
    
        
       
# def score() :


#def combos() :




# def user() :
    




# def lettre_au_hasard():
#     with open("lettre au hasard", "w", encoding = "utf8")as fichier :
#         fichier.write(lettre_au_hasard)