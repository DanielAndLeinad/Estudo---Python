import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definições básicas da tela
LARGURA = 300
ALTURA = 600
COLUNAS = 10
LINHAS = 20
TAMANHO_BLOCO = LARGURA // COLUNAS
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetris com Python")

# Definição de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)
CORES = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Peças do Tetris
PECAS = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]]  # Quadrado
]

# Criar grade do tabuleiro
grade = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]

# Classe da Peça
def nova_peca():
    peca = random.choice(PECAS)
    cor = random.choice(CORES)
    return {'matriz': peca, 'x': COLUNAS // 2 - len(peca[0]) // 2, 'y': 0, 'cor': cor}

peca_atual = nova_peca()

# Função para desenhar o tabuleiro
def desenhar_grade():
    for y in range(LINHAS):
        for x in range(COLUNAS):
            cor = grade[y][x] if grade[y][x] else CINZA
            pygame.draw.rect(tela, cor, (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO), 0 if grade[y][x] else 1)

# Função para desenhar a peça
def desenhar_peca(peca):
    for i, linha in enumerate(peca['matriz']):
        for j, bloco in enumerate(linha):
            if bloco:
                pygame.draw.rect(tela, peca['cor'], ((peca['x'] + j) * TAMANHO_BLOCO, (peca['y'] + i) * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))

# Função para verificar colisão
def colide(peca, dx=0, dy=0):
    for i, linha in enumerate(peca['matriz']):
        for j, bloco in enumerate(linha):
            if bloco:
                novo_x = peca['x'] + j + dx
                novo_y = peca['y'] + i + dy
                if novo_x < 0 or novo_x >= COLUNAS or novo_y >= LINHAS or (novo_y >= 0 and grade[novo_y][novo_x]):
                    return True
    return False

# Função para fixar peça no tabuleiro
def fixar_peca():
    global peca_atual
    for i, linha in enumerate(peca_atual['matriz']):
        for j, bloco in enumerate(linha):
            if bloco:
                grade[peca_atual['y'] + i][peca_atual['x'] + j] = peca_atual['cor']
    remover_linhas()
    peca_atual = nova_peca()
    if colide(peca_atual):
        return False  # Game Over
    return True

# Função para remover linhas completas
def remover_linhas():
    global grade
    nova_grade = [linha for linha in grade if any(bloco == 0 for bloco in linha)]
    while len(nova_grade) < LINHAS:
        nova_grade.insert(0, [0 for _ in range(COLUNAS)])
    grade = nova_grade

# Loop principal
tempo_queda = 0
TAXA_QUEDA = 500  # Milissegundos
clock = pygame.time.Clock()
jogando = True

while jogando:
    tela.fill(PRETO)
    desenhar_grade()
    desenhar_peca(peca_atual)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT and not colide(peca_atual, dx=-1):
                peca_atual['x'] -= 1
            elif evento.key == pygame.K_RIGHT and not colide(peca_atual, dx=1):
                peca_atual['x'] += 1
            elif evento.key == pygame.K_DOWN and not colide(peca_atual, dy=1):
                peca_atual['y'] += 1
            elif evento.key == pygame.K_UP:
                nova_matriz = list(zip(*peca_atual['matriz'][::-1]))
                peca_rotacionada = {'matriz': nova_matriz, 'x': peca_atual['x'], 'y': peca_atual['y'], 'cor': peca_atual['cor']}
                if not colide(peca_rotacionada):
                    peca_atual['matriz'] = nova_matriz

    tempo_queda += clock.get_rawtime()
    if tempo_queda > TAXA_QUEDA:
        if not colide(peca_atual, dy=1):
            peca_atual['y'] += 1
        else:
            jogando = fixar_peca()
        tempo_queda = 0
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()