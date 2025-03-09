"""
## Projeto Final: Gerenciador de Arquivos CSV
Criamos um sistema que:
1. Gera um CSV com dados
2. Move o CSV para uma pasta específica
3. Lê os dados e exibe no console
"""
import csv
import shutil
import os

# Criando o arquivo CSV no diretório do script
nome_arquivo = "cadastro.csv"
with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Curso", "Codigo"])
    escritor.writerow(["Marcos", "Eng. Software", 1])
    escritor.writerow(["Michelle", "Farmacia", 2])
    escritor.writerow(["Melissa", "Psicologia", 3])

# Definindo o caminho correto da pasta "cadastros" (um nível acima)
caminho_pasta = os.path.join(os.pardir, "cadastros")

# Criando a pasta no diretório principal caso não exista
if not os.path.exists(caminho_pasta):
    os.mkdir(caminho_pasta)
    print(f"Pasta 'cadastros' criada em {caminho_pasta}")

# Movendo o CSV para a pasta "cadastros"
caminho_arquivo_destino = os.path.join(caminho_pasta, nome_arquivo)
shutil.move(nome_arquivo, caminho_arquivo_destino)
print(f"Arquivo movido para {caminho_arquivo_destino}")

# Lendo o arquivo CSV da pasta "cadastros"
with open(caminho_arquivo_destino, mode="r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)  # Exibe cada linha do CSV
