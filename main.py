#importando bibliotecas
import pygame
from os import path
import random

#iniciando o pygame
pygame.init()
pygame.mixer.init()


#constantes
# IMG_DIR = path.join(path.dirname(__file__), 'img')
IMG_DIR = path.dirname(__file__)
BLACK = (0, 0, 0)
WHITE =  (255, 255, 255)
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


#conseguir abrir a tela e fechar ela
state = PLAYING
while state != DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE

    #A cada loop, redesenhe o fundo e os sprites
    screen.fill(BLACK)
    screen.blit(veneno_img, (50, 50))
    screen.blit(arma1_img, (100, 50))
    screen.blit(arma_pá_img, (200, 50))
    screen.blit(Socoinglês_img, (300, 50))

    #depois de desenhar tudo, mostra a nova tela
    pygame.display.flip()

pygame.quit()