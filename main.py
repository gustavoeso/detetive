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
GROUND = 550

#coordenadas dos locais
T_TELA_X = 1080
T_TELA_Y = 820

X_BANCO = 10*2.16
Y_BANCO = 10*1.64


X_METRO = 10*2.16
Y_METRO = 200*1.40

X_HOTEL = 10*2.16
Y_HOTEL = 380*1.50

X_BIBLIOTECA = 200*2.16
Y_BIBLIOTECA = 10*1.64

X_CEMIT = 380*2.16
Y_CEMIT = 10*1.64

X_BOATE = 380*2.16
Y_BOATE = 200*1.40

X_FLORI = 380*2.16
Y_FLORI = 380*1.50

X_PREFEITURA = 200*2.16
Y_PREFEITURA = 380*1.50

X_PRACA = 200*2.16
Y_PRACA = 200*1.20

X_BACK = 400*2.50
Y_BACK = 400*1.85

X_TROFEU = 250*2.16
Y_TROFEU = 250*1.64

Y_CHUTE = 410

# variaveis
game_state = 0 


class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y

class Arma(pygame.sprite.Sprite):
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
    def __init__(self, x, y, img, img_grande, nome, Armas, Objetos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.img_grande = img_grande
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.nome = nome
        self.Armas = Armas
        self.Objetos = Objetos

def verifica_clique(locais):
    mouse_pos = pygame.mouse.get_pos()
    for local in locais:
        if local.rect.collidepoint(mouse_pos):
            return local
    return None

def verifica_clique_local(local_rect):
    mouse_pos = pygame.mouse.get_pos()
    if local_rect.collidepoint(mouse_pos):
        return True
    # return game_state
    return False

class chute_local(pygame.sprite.Sprite):
    def __init__(self, x, y, img, local_chute):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.local_chute = local_chute

def verifica_clique_chute(locais):
    mouse_pos = pygame.mouse.get_pos()
    for local in locais:
        if local.rect.collidepoint(mouse_pos):
            return local
    return None

# def verifica_clique_arma(local_rect):
#     mouse_pos = pygame.mouse.get_pos()
#     for Arma in Armas:    
#         if local_rect.collidepoint(mouse_pos):
#             return Objeto
#     # return game_state
#     return False


#tela do jogo
screen = pygame.display.set_mode((T_TELA_X, T_TELA_Y))
pygame.display.set_caption('Detetive')


#carregar imagens

arma1_img = pygame.image.load(path.join(IMG_DIR, 'imagens/arma1.png')).convert_alpha()
arma_pá_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_pá.png')).convert_alpha()
Socoinglês_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_socoinglês.png')).convert_alpha()
veneno_img = pygame.image.load(path.join(IMG_DIR, 'imagens/armas_veneno.png')).convert_alpha()
trofeu_img = pygame.image.load(path.join(IMG_DIR, 'imagens/trofeu.png')).convert_alpha()
tesoura_img = pygame.image.load(path.join(IMG_DIR, 'imagens/tesoura.png')).convert_alpha()
pistola_img = pygame.image.load(path.join(IMG_DIR, 'imagens/pistola.png')).convert_alpha()
castical_img = pygame.image.load(path.join(IMG_DIR, 'imagens/castical.png')).convert_alpha()
corda_img = pygame.image.load(path.join(IMG_DIR, 'imagens/corda.png')).convert_alpha()
chave_inglesa_img = pygame.image.load(path.join(IMG_DIR, 'imagens/chave_inglesa.png')).convert_alpha()
blank_img = pygame.image.load(path.join(IMG_DIR, 'imagens/blank.png')).convert_alpha()
back_img = pygame.image.load(path.join(IMG_DIR, 'imagens/back.png')).convert_alpha()
back_img_rect = back_img.get_rect()
back_img_rect.x = X_BACK
back_img_rect.y = Y_BACK
teste_img = pygame.image.load(path.join(IMG_DIR, 'imagens/teste.png')).convert_alpha()
banco_img = pygame.image.load(path.join(IMG_DIR, 'imagens/banco.png')).convert_alpha()
biblioteca_img = pygame.image.load(path.join(IMG_DIR, 'imagens/restaurante.png')).convert_alpha()
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
banco_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/banco_grande.jpg')).convert_alpha()
flori_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/flori_grande.png')).convert_alpha()
praca_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/praca_grande.png')).convert_alpha()
prefeitura_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/prefeitura_grande.png')).convert_alpha()
biblioteca_grande_img = pygame.image.load(path.join(IMG_DIR, 'imagens/biblioteca_grande.png')).convert_alpha()
tutorial1_img = pygame.image.load(path.join(IMG_DIR, 'imagens/tutorial1.png')).convert_alpha()
tutorial2_img = pygame.image.load(path.join(IMG_DIR, 'imagens/tutorial2.png')).convert_alpha()
tutorial3_img = pygame.image.load(path.join(IMG_DIR, 'imagens/tutorial3.png')).convert_alpha()

# Fazer uma lista de n+1 objetos
posicoes = [
    [100, 200],
    [300, 380], 
    [400, 400], 
    [300, 400], 
    [900, 300],
    [250, 700],
    [100, 450],
    [450, 300],
    [15, 70],
    [1000, 600],
    [400, 400],
    [200, 400],
    [100, 400],
    [200, 200],
    [900, 700],
]


Armas = [
    Arma(posicoes[0][0], posicoes[0][1], tesoura_img), 
    Arma(posicoes[1][0], posicoes[1][1], arma1_img), 
    Arma(posicoes[2][0], posicoes[2][1], arma_pá_img),
    Arma(posicoes[3][0], posicoes[3][1], Socoinglês_img),
    Arma(posicoes[4][0], posicoes[4][1], trofeu_img),
    Arma(posicoes[5][0], posicoes[5][1], pistola_img),
    Arma(posicoes[6][0], posicoes[6][1], castical_img),
    Arma(posicoes[7][0], posicoes[7][1], corda_img),
    Arma(posicoes[8][0], posicoes[8][1], chave_inglesa_img),
    Arma(posicoes[9][0], posicoes[9][1], veneno_img),
]


random.shuffle(Armas)
Arma_selecionada = Armas.pop()

Objetos = [
    Objeto(posicoes[10][0], posicoes[10][1], blank_img),
    Objeto(posicoes[11][0], posicoes[11][1], blank_img),
    Objeto(posicoes[12][0], posicoes[12][1], blank_img),
    Objeto(posicoes[13][0], posicoes[13][1], blank_img),
    Objeto(posicoes[14][0], posicoes[14][1], blank_img),
]
random.shuffle(Objetos)

#dicionario definindo os locais
locais = [
    Local(X_BANCO, Y_BANCO, banco_img, banco_grande_img, 'banco', Armas[0:2], Objetos[0:1]),
    Local(X_BIBLIOTECA, Y_BIBLIOTECA, biblioteca_img, biblioteca_grande_img, 'biblioteca', Armas[0:0], Objetos[1:2]),
    Local(X_HOTEL, Y_HOTEL, hotel_img, hotel_grande_img, 'hotel', Armas[2:4], Objetos[2:3]),
    Local(X_METRO, Y_METRO, metro_img, metro_grande_img, 'metro', Armas[4:5], Objetos[3:4]),
    Local(X_CEMIT, Y_CEMIT, cemit_img, cemit_grande_img, 'cemiterio', Armas[0:0], Objetos[4:5]),
    Local(X_BOATE, Y_BOATE, boate_img, boate_grande_img, 'boate', Armas[5:8], Objetos[5:6]),
    Local(X_FLORI, Y_FLORI, flori_img, flori_grande_img, 'floricultura', Armas[0:0], Objetos[6:7]),
    Local(X_PREFEITURA, Y_PREFEITURA, prefeitura_img, prefeitura_grande_img, 'prefeitura', Armas[8:9], Objetos[7:8]),
    Local(X_PRACA, Y_PRACA, praca_img, praca_grande_img, 'praca', Armas[9:10], Objetos[8:9]),
]

# Define constantes para as telas
STARTING = 0
DONE = 1
PLAYING = 2
GAME = 3
END = 4
CREDITOS = 5
TUTORIAL1 = 6
TUTORIAL2 = 7
TUTORIAL3 = 8
CHUTE = 9
GANHOU = 10
PERDEU = 11


#conseguir abrir a tela e fechar ela
def game_screen(screen):
    chute_lista = []
    local_atual = None
    state = PLAYING
    pygame.mixer.music.load((path.join(SND_DIR, 'Musicas/sherlock.mp3')))
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.MOUSEBUTTONDOWN:
                for chutes in chute_lista:
                    if chutes.rect.collidepoint(event.pos):
                        return CHUTE
                if local_atual is None:
                    local_atual = verifica_clique(locais)
                else:
                    voltar = verifica_clique_local(back_img_rect)
                    sound_click = pygame.mixer.Sound((path.join(SND_DIR, 'Musicas/click.mp3')))
                    sound_click.play()
                    if voltar:
                        local_atual = None
        #A cada loop, redesenhe o fundo e os sprites

        if local_atual is None:
            screen.fill(GREEN)
            for local in locais:
                screen.blit(local.image, local.rect)
                #adicionando botão para página de chute
                chute = chute_local(10, 10, teste_img, local.nome)
                chute_lista.append(chute)
                screen.blit(chute.image, chute.rect)
        else:
            screen.fill(BLACK)
            screen.blit(local_atual.img_grande, (0, 0))
            screen.blit(back_img, back_img_rect)
            i = 0
            for Arma in local_atual.Armas:
                screen.blit(Arma.image, Arma.rect)
                i += 1
            for Objeto in local_atual.Objetos:
                screen.blit(Objeto.image, Objeto.rect)
                i += 1
        #depois de desenhar tudo, mostra a nova tela
        pygame.display.flip()

#mudanddo telas iniciais e do jogo
def tutorial_screen(screen, background_img, next_screen):
    state = PLAYING
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return END
            if event.type == pygame.MOUSEBUTTONDOWN:
                return next_screen

        screen.blit(background_img, (0,0))
        #depois de desenhar tudo, mostra a nova tela
        pygame.display.flip()

def ganhou_screen(screen):
    state = PLAYING
    while state != DONE: 
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return END
            if event.type == pygame.NOFRAME:
                screen = screen.blit(boate_grande_img)
        pygame.display.flip()
game_state = TUTORIAL1

def chute_screen(screen):
    local_atual = None
    state = PLAYING
    Armas.append(Arma_selecionada)
    random.shuffle(Armas)
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.MOUSEBUTTONDOWN:
                local_atual = verifica_clique_chute(Armas)
                if local_atual == Arma_selecionada:
                    print("ganhou")
                    game_state == GANHOU
                else:
                    print("perdeu")
        #A cada loop, redesenhe o fundo e os sprites
        if local_atual is None:
            screen.fill(GREEN)
            X_CHUTE = 50
            for Arma in Armas:
                Arma.rect.x = X_CHUTE
                Arma.rect.y = Y_CHUTE
                screen.blit(Arma.image, (X_CHUTE, Y_CHUTE))
                X_CHUTE += 90
        #depois de desenhar tudo, mostra a nova tela
        pygame.display.flip()

while game_state != END:
    # if game_state == STARTING:
    #     game_state = start_screen(screen)
    if game_state == GAME:
        game_state = game_screen(screen)
    elif game_state == TUTORIAL1:
        game_state = tutorial_screen(screen, tutorial1_img, TUTORIAL2)
    elif game_state == TUTORIAL2:
        game_state = tutorial_screen(screen, tutorial2_img, TUTORIAL3)
    elif game_state == TUTORIAL3:
        game_state = tutorial_screen(screen, tutorial3_img, GAME)
    elif game_state == CHUTE:
        game_state = chute_screen(screen)
    elif game_state == GANHOU:
        game_state = ganhou_screen(screen)
    else:
        game_state = END

pygame.quit()