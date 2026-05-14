import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 600
ALTURA = 400
TAMANHO_BLOCO = 20

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Clock
clock = pygame.time.Clock()

# Fonte
fonte = pygame.font.SysFont(None, 35)

def desenhar_cobra(lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(
            tela,
            VERDE,
            [bloco[0], bloco[1], TAMANHO_BLOCO, TAMANHO_BLOCO]
        )

def mostrar_pontos(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, [10, 10])

def jogo():
    x = LARGURA // 2
    y = ALTURA // 2

    mover_x = 0
    mover_y = 0

    cobra = []
    tamanho_cobra = 1

    maca_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / 20) * 20
    maca_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / 20) * 20

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    mover_x = -TAMANHO_BLOCO
                    mover_y = 0

                elif evento.key == pygame.K_RIGHT:
                    mover_x = TAMANHO_BLOCO
                    mover_y = 0

                elif evento.key == pygame.K_UP:
                    mover_y = -TAMANHO_BLOCO
                    mover_x = 0

                elif evento.key == pygame.K_DOWN:
                    mover_y = TAMANHO_BLOCO
                    mover_x = 0

        x += mover_x
        y += mover_y

        # Colisão com parede
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            rodando = False

        tela.fill(PRETO)

        # Desenha maçã
        pygame.draw.rect(
            tela,
            VERMELHO,
            [maca_x, maca_y, TAMANHO_BLOCO, TAMANHO_BLOCO]
        )

        cabeca = [x, y]
        cobra.append(cabeca)

        if len(cobra) > tamanho_cobra:
            del cobra[0]

        # Colisão com si mesma
        for parte in cobra[:-1]:
            if parte == cabeca:
                rodando = False

        desenhar_cobra(cobra)
        mostrar_pontos(tamanho_cobra - 1)

        pygame.display.update()

        # Comer maçã
        if x == maca_x and y == maca_y:
            maca_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / 20) * 20
            maca_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / 20) * 20
            tamanho_cobra += 1

        clock.tick(10)

    pygame.quit()

jogo()
