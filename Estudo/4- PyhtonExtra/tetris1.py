import pygame #NO TERMINAL COLOQUE "pip install pygame" E DEPOIS "python.exe -m pip install --upgrade pip"

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

# Configuração da grade do tabuleiro
COLUNAS = 10
LINHAS = 20
TAMANHO_BLOCO = LARGURA // COLUNAS

def desenhar_grade():
    """Desenha a grade do tabuleiro."""
    for x in range(0, LARGURA, TAMANHO_BLOCO):
        pygame.draw.line(tela, CINZA, (x, 0), (x, ALTURA))  # Linhas verticais
    for y in range(0, ALTURA, TAMANHO_BLOCO):
        pygame.draw.line(tela, CINZA, (0, y), (LARGURA, y))  # Linhas horizontais

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill(PRETO)  # Limpa a tela com a cor preta
    desenhar_grade()  # Desenha a grade do tabuleiro
    pygame.display.flip()  # Atualiza a tela

# Encerra o Pygame
pygame.quit()