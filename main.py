#importando bibliotecas
import pygame
from os import path
import random

#iniciando o pygame
pygame.init()
pygame.mixer.init()


#constantes
IMG_DIR = path.dirname(__file__)
BLACK = (0, 0, 0)
WHITE =  (255, 255, 255)
GREEN = (0, 128, 0)
DONE = 0
PLAYING = 1
GROUND = 550


class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y


#tela do jogo
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Detetive')


#carregar imagens
arma1_img = pygame.image.load(path.join(IMG_DIR, 'imagens/arma1.png')).convert_alpha()
arma_pá_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_pá.png')).convert_alpha()
Socoinglês_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_socoinglês.png')).convert_alpha()
veneno_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_veneno.png')).convert_alpha()
banco_img = pygame.image.load(path.join(IMG_DIR, 'imagens/banco.png')).convert_alpha()
biblioteca_img = pygame.image.load(path.join(IMG_DIR, 'imagens/biblioteca.png')).convert_alpha()
hotel_img = pygame.image.load(path.join(IMG_DIR, 'imagens/hotel.png')).convert_alpha()
praca_img = pygame.image.load(path.join(IMG_DIR, 'imagens/praca.png')).convert_alpha()
cemit_img = pygame.image.load(path.join(IMG_DIR, 'imagens/cemit.png')).convert_alpha()
boate_img = pygame.image.load(path.join(IMG_DIR, 'imagens/boate.png')).convert_alpha()
flori_img = pygame.image.load(path.join(IMG_DIR, 'imagens/flori.png')).convert_alpha()
prefeitura_img = pygame.image.load(path.join(IMG_DIR, 'imagens/prefeitura.png')).convert_alpha()
metro_img = pygame.image.load(path.join(IMG_DIR, 'imagens/metro.png')).convert_alpha()

#conseguir abrir a tela e fechar ela
state = PLAYING
while state != DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print (position[0])

    #A cada loop, redesenhe o fundo e os sprites
    screen.fill(GREEN)
    # screen.blit(veneno_img, (50, 50))
    # screen.blit(arma1_img, (100, 50))
    # screen.blit(arma_pá_img, (200, 50))
    # screen.blit(Socoinglês_img, (300, 50))
    screen.blit(banco_img, (10, 10))
    screen.blit(biblioteca_img, (10, 200))
    screen.blit(hotel_img, (10, 380))
    screen.blit(metro_img, (200, 10))
    screen.blit(cemit_img, (380, 10))
    screen.blit(boate_img, (380, 200))
    screen.blit(flori_img, (380, 380))
    screen.blit(prefeitura_img, (200, 380))
    screen.blit(praca_img, (200, 200))
# comentário

    #depois de desenhar tudo, mostra a nova tela
    pygame.display.flip()

pygame.quit()