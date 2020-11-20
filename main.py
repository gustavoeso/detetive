#importando bibliotecas
import pygame
from os import path
import random

#iniciando o pygame
pygame.init()
pygame.mixer.init()


#constantes
IMG_DIR = path.dirname(__file__)
SND_DIR = path.dirname(__file__)
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

X_BACK = 400

Y_BACK = 400

X_TROFEU = 250

Y_TROFEU = 250

# variaveis
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
            # return locais.index(local)+1
            return local
    # return game_state
    return None

def verifica_clique_local(local_rect):
    mouse_pos = pygame.mouse.get_pos()
    if local_rect.collidepoint(mouse_pos):
        return True
    # return game_state
    return False


#tela do jogo
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Detetive')


#carregar imagens

arma1_img = pygame.image.load(path.join(IMG_DIR, 'imagens/arma1.png')).convert_alpha()
arma_pá_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_pá.png')).convert_alpha()
Socoinglês_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_socoinglês.png')).convert_alpha()
veneno_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_veneno.png')).convert_alpha()
trofeu_img = pygame.image.load(path.join(IMG_DIR, 'imagens/trofeu.png')).convert_alpha()
tesoura_img = pygame.image.load(path.join(IMG_DIR, 'imagens/tesoura.png')).convert_alpha()
back_img = pygame.image.load(path.join(IMG_DIR, 'imagens/back.png')).convert_alpha()
back_img_rect = back_img.get_rect()
back_img_rect.x = X_BACK
back_img_rect.y = Y_BACK
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
tutorial1_img = pygame.image.load(path.join(IMG_DIR, 'imagens/tutorial1.png')).convert_alpha()
tutorial2_img = pygame.image.load(path.join(IMG_DIR, 'imagens/tutorial2.png')).convert_alpha()
tutorial3_img = pygame.image.load(path.join(IMG_DIR, 'imagens/tutorial3.png')).convert_alpha()

# Fazer uma lista de n+1 objetos

objetos = [
    Objeto(X_TROFEU, Y_TROFEU, tesoura_img), 
    Objeto(X_TROFEU, Y_TROFEU, trofeu_img), 
    Objeto(X_TROFEU, Y_TROFEU, trofeu_img),
]
# random.shuffle(objetos)
objeto_selecionado = objetos[-1]
posicoes = [[100, 200], [300, 380], [200, 400]]

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

# Define constantes para as telas
STARTING = 0
GAME = 1
END = 2
CREDITOS = 3
TUTORIAL1 = 4
TUTORIAL2 = 5
TUTORIAL3 = 6


#conseguir abrir a tela e fechar ela
def game_screen(screen):
    state = PLAYING
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return END
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


#conseguir abrir a tela e fechar ela
local_atual = None
state = PLAYING
pygame.mixer.music.load((path.join(SND_DIR, 'Musicas/sherlock.mp3')))
pygame.mixer.music.play(loops=-1)
while state != DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if local_atual is None:
                local_atual = verifica_clique(locais)
                if clicou_botao_tutorial:
                     return TUTORIAL 
                if clicou_botao_creditos:
                     return CREDITOS
            else:
                voltar = verifica_clique_local(back_img_rect)
                sound_click = pygame.mixer.Sound((path.join(SND_DIR, 'Musicas/click.mp3')))
                sound_click.play()
                if voltar:
                    local_atual = None
    #A cada loop, redesenhe o fundo e os sprites
    # if game_state == 0:
    if local_atual is None:
        screen.fill(GREEN)
        for local in locais:
            screen.blit(local.image, local.rect)
    else:
        screen.fill(BLACK)
        screen.blit(local_atual.img_grande, (0, 0))
        screen.blit(back_img, back_img_rect)
        i = 0
        for objeto in local_atual.objetos:
            posicao = posicoes[i]
            screen.blit(objeto.image, posicao)
            i += 1
    #depois de desenhar tudo, mostra a nova tela
    pygame.display.flip()

pygame.quit()
 

def tutorial_screen(screen, background_img, next_screen):
    state = PLAYING
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return END
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if clicou_botao_tutorial:
                #     return TUTORIAL 
                #if clicou_botao_creditos:
                #     return CREDITOS
                return next_screen
    
        screen.fill((255, 0, 0))

        #depois de desenhar tudo, mostra a nova tela
        pygame.display.flip()


game_state = STARTING
while game_state != END:
    if game_state == STARTING:
        game_state = start_screen(screen)
    elif game_state == GAME:
        game_state = game_screen(screen)
    # elif game_state == TUTORIAL1:
    #     game_state = tutorial_screen(screen, tutorial1_img, TUTORIAL2)
    # elif game_state == TUTORIAL2:
    #     game_state = tutorial_screen(screen, tutorial2_img, TUTORIAL3)
    #elif game_state == TUTORIAL3:
    #     game state = tutorial_screen(screen, tutorial3_img, INICIAL)
    else:
        game_state = END

pygame.quit()