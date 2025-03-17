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

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill(PRETO)  # Limpa a tela com a cor preta
    pygame.display.flip()  # Atualiza a tela

# Encerra o Pygame
pygame.quit()