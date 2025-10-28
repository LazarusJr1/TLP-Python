import pygame

import random
 
pygame.init()

tamanho_tela = (600, 600)

tela = pygame.display.set_mode(tamanho_tela)

pygame.display.set_caption("Brick Breaker")


bola = pygame.Rect(100, 500, 15, 15)

jogador = pygame.Rect(350, 500, 100, 15)  # Barra do jogador na parte inferior


qtde_blocos_linha = 8

qtde_linhas_blocos = 5


velocidade_bola = [1, -1]  # Movimento bem devagar, tanto horizontal quanto vertical

def criar_blocos(qtde_blocos_linha, qtde_linhas_blocos):

    blocos = []

    largura_bloco = (tamanho_tela[0] / qtde_blocos_linha) - 5

    altura_bloco = 20
 
    for j in range(qtde_linhas_blocos):

        for i in range(qtde_blocos_linha):

            bloco = pygame.Rect(i * (largura_bloco + 5), j * (altura_bloco + 10), largura_bloco, altura_bloco)

            blocos.append(bloco)

    return blocos


blocos = criar_blocos(qtde_blocos_linha, qtde_linhas_blocos)


cores = {

    "branca": (255, 255, 255),

    "preta": (0, 0, 0),

    "amarela": (255, 255, 0),

    "azul": (0, 0, 255),

    "verde": (0, 255, 0)

}


def desenhar_tela():

    tela.fill(cores["preta"])

    pygame.draw.rect(tela, cores["azul"], jogador)  # Desenha a barra do jogador

    pygame.draw.rect(tela, cores["branca"], bola)  # Desenha a bola

    for bloco in blocos:

        pygame.draw.rect(tela, cores["verde"], bloco)  # Desenha os blocos

    pygame.display.flip()


def mover_bola():

    bola.x += velocidade_bola[0]

    bola.y += velocidade_bola[1]


    if bola.left <= 0 or bola.right >= tamanho_tela[0]:

        velocidade_bola[0] = -velocidade_bola[0]


    if bola.top <= 0:

        velocidade_bola[1] = -velocidade_bola[1]


    if bola.bottom >= tamanho_tela[1]:

        return True  # Bola caiu, fim de jogo
 
    return False


def colisao_jogador():

    if bola.colliderect(jogador):

        velocidade_bola[1] = -velocidade_bola[1]


def colisao_blocos():

    global blocos

    for bloco in blocos[:]:

        if bola.colliderect(bloco):

            velocidade_bola[1] = -velocidade_bola[1]

            blocos.remove(bloco)


movimento_jogador = 0

velocidade_jogador = 10
 


clock = pygame.time.Clock()
 
fim_jogo = False

while not fim_jogo:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            fim_jogo = True


    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and jogador.left > 0:

        movimento_jogador = -velocidade_jogador

    elif teclas[pygame.K_RIGHT] and jogador.right < tamanho_tela[0]:

        movimento_jogador = velocidade_jogador

    else:

        movimento_jogador = 0


    jogador.x += movimento_jogador


    if mover_bola():

        fim_jogo = True  # A bola caiu, fim de jogo


    colisao_jogador()

    colisao_blocos()


    desenhar_tela()
 


    clock.tick(400) 


pygame.quit()
 