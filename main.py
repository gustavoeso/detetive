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

#variaveis
game_state = 0

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y


class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y


class Local(pygame.sprite.Sprite):
    def __init__(self, x, y, img, img_grande, nome, objetos):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.img_grande = img_grande
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.nome = nome
        self.objetos = objetos


def verifica_clique(locais):
    mouse_pos = pygame.mouse.get_pos()
    for local in locais:
        if local.rect.collidepoint(mouse_pos):
            print(local.nome)  # Mostrar a tela. O print é só teste
            # return locais.index(local)+1
            return local
    # return game_state
    return None

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
metro_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/metro_grande.png')).convert_alpha()
boate_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/boate_grande.png')).convert_alpha()
cemit_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/cemit_grande.png')).convert_alpha()
hotel_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/hotel_grande.png')).convert_alpha()
banco_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/banco_grande.png')).convert_alpha()
flori_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/flori_grande.png')).convert_alpha()
praca_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/praca_grande.png')).convert_alpha()
prefeitura_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/prefeitura_grande.png')).convert_alpha()
biblioteca_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/biblioteca_grande.png')).convert_alpha()

# Fazer uma lista de n+1 objetos
objetos = [1, 2, 3, 4, 5, 6, 7, 8]  # Trocar por Objeto()
# random.shuffle(objetos)
objeto_selecionado = objetos[-1]

#dicionario definindo os locais
locais = [
    Local(X_BANCO, Y_BANCO, banco_img, banco_grande_img, 'banco', objetos[0:3]),
    Local(X_BIBLIOTECA, Y_BIBLIOTECA, biblioteca_img, biblioteca_grande_img, 'biblioteca', objetos[3:6]),
    Local(X_HOTEL, Y_HOTEL, hotel_img, hotel_grande_img, 'hotel', objetos[6:9]),
    Local(X_METRO, Y_METRO, metro_img, metro_grande_img, 'metro', objetos[9:12]),
    Local(X_CEMIT, Y_CEMIT, cemit_img, cemit_grande_img, 'cemiterio', objetos[12:15]),
    Local(X_BOATE, Y_BOATE, boate_img, boate_grande_img, 'boate', objetos[15:18]),
    Local(X_FLORI, Y_FLORI, flori_img, flori_grande_img, 'floricultura', objetos[18:21]),
    Local(X_PREFEITURA, Y_PREFEITURA, prefeitura_img, prefeitura_grande_img, 'prefeitura', objetos[21:24]),
    Local(X_PRACA, Y_PRACA, praca_img, praca_grande_img, 'praca', objetos[24:27]),
]


#conseguir abrir a tela e fechar ela
local_atual = None
state = PLAYING
while state != DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state ==0:
                local_atual = verifica_clique(locais)
                print('---------------------------')
            # elif tela_de_chute:
            #     verifica_clique_objeto(objetos)
            else:
                print('Hello world')
    #A cada loop, redesenhe o fundo e os sprites
    # if game_state == 0:
    if local_atual is None:
        screen.fill(GREEN)
        for local in locais:
            screen.blit(local.image, local.rect)
    else:
        screen.fill(BLACK)
        screen.blit(local_atual.img_grande, (0, 0))
        for objeto in local_atual.objetos:
            pass

    #depois de desenhar tudo, mostra a nova tela
    pygame.display.flip()


pygame.quit()