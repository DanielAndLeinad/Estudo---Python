import pygame #NO TERMINAL COLOQUE "pip install pygame" E DEPOIS "python.exe -m pip install --upgrade pip"
import random

# Inicializa o Pygame
pygame.init()

# Definições básicas da tela
LARGURA = 300
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetris com Python")

# Definição de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Configuração da grade do tabuleiro
COLUNAS = 10
LINHAS = 20
TAMANHO_BLOCO = LARGURA // COLUNAS

# Peças do Tetris (formatos básicos)
PECAS = [
    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[1, 1],
     [1, 1]],
    [[1, 1, 1, 1]]
]

# Classe para representar uma peça do Tetris
class Peca:
    def __init__(self, matriz, x, y, cor):
        self.matriz = matriz
        self.x = x
        self.y = y
        self.cor = cor

    def desenhar(self):
        for i, linha in enumerate(self.matriz):
            for j, bloco in enumerate(linha):
                if bloco:
                    pygame.draw.rect(tela, self.cor, (self.x + j * TAMANHO_BLOCO, self.y + i * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))

# Função para desenhar a grade
def desenhar_grade():
    for x in range(0, LARGURA, TAMANHO_BLOCO):
        pygame.draw.line(tela, CINZA, (x, 0), (x, ALTURA))
    for y in range(0, ALTURA, TAMANHO_BLOCO):
        pygame.draw.line(tela, CINZA, (0, y), (LARGURA, y))

# Criar peça inicial
peca_atual = Peca(random.choice(PECAS), LARGURA // 2, 0, random.choice([VERMELHO, AZUL, VERDE]))

# Variáveis de controle
tempo_queda = 0
TAXA_QUEDA = 500  # Milissegundos
pontuacao = 0
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    tela.fill(PRETO)
    desenhar_grade()
    peca_atual.desenhar()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Controle de tempo para movimentação automática da peça
    tempo_queda += clock.get_rawtime()
    if tempo_queda > TAXA_QUEDA:
        peca_atual.y += TAMANHO_BLOCO
        tempo_queda = 0
    
    pygame.display.flip()
    clock.tick(30)

# Encerra o Pygame
pygame.quit()
