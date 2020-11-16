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

#coordenadas dos locais
X_BANCO = 10
Y_BANCO = 10

X_BIBLIOTECA = 10
Y_BIBLIOTECA = 200

X_HOTEL = 10
Y_HOTEL = 380

X_METRO = 200
Y_METRO = 10

X_CEMIT = 380
Y_CEMIT = 10

X_BOATE = 380
Y_BOATE = 200

X_FLORI = 380
Y_FLORI = 380

X_PREFEITURA = 200
Y_PREFEITURA = 380

X_PRACA = 200
Y_PRACA = 200

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y


class Local(pygame.sprite.Sprite):
    def __init__(self, x, y, img, nome):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.nome = nome


def verifica_clique(locais):
    mouse_pos = pygame.mouse.get_pos()
    for local in locais:
        if local.rect.collidepoint(mouse_pos):
            print(local.nome)  # Mostrar a tela. O print é só teste


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

#dicionario definindo os locais
locais = [
    Local(X_BANCO, Y_BANCO, banco_img, 'banco'),
    Local(X_BIBLIOTECA, Y_BIBLIOTECA, biblioteca_img, 'biblioteca'),
    Local(X_HOTEL, Y_HOTEL, hotel_img, 'hotel'),
    Local(X_METRO, Y_METRO, metro_img, 'metro'),
    Local(X_CEMIT, Y_CEMIT, cemit_img, 'cemiterio'),
    Local(X_BOATE, Y_BOATE, boate_img, 'boate'),
    Local(X_FLORI, Y_FLORI, flori_img, 'floricultura'),
    Local(X_PREFEITURA, Y_PREFEITURA, prefeitura_img, 'prefeitura'),
    Local(X_PRACA, Y_PRACA, praca_img, 'praca'),
]

#conseguir abrir a tela e fechar ela
state = PLAYING
while state != DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE
        if event.type == pygame.MOUSEBUTTONDOWN:
            verifica_clique(locais)
            print('---------------------------')


    #A cada loop, redesenhe o fundo e os sprites
    screen.fill(GREEN)
    # screen.blit(veneno_img, (50, 50))
    # screen.blit(arma1_img, (100, 50))
    # screen.blit(arma_pá_img, (200, 50))
    # screen.blit(Socoinglês_img, (300, 50))
    for local in locais:
        screen.blit(local.image, local.rect)

    #depois de desenhar tudo, mostra a nova tela
    pygame.display.flip()


pygame.quit()