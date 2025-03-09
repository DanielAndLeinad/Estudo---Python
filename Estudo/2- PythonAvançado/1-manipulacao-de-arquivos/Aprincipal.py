"""
# Manipulação de Arquivos e Pastas em Python

## Introdução
Neste material, aprenderemos a:
1. Criar, ler e escrever arquivos CSV e variáveis dentro deles
2. Manipular pastas utilizando os módulos `os` e `shutil`
3. Criar um projeto prático unindo todos os conceitos

Vamos começar com a manipulação de arquivos!

# with = abre e fecha o arquivo automaticamente
# open = função que abre o arquivo
# "r" = modo de leitura
# encoding = codificação do arquivo
# as = apelido para o arquivo
# arquivo = nome do arquivo
# leitor = função que lê o arquivo
# csv.reader = função que lê o arquivo csv
# for = loop
# linha = linha do arquivo
# print = função que imprime a linha do arquivo

"""

#1. criando e escrevendo arquivo em CSV
import csv
 
#criando um arquivo CSV e escrevendo nele
with open("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    #Escrevendo o cabeçalho
    escritor.writerow(["Nome", "Idade", "Cidad3e"])
    #Escrevendo Dados
    escritor.writerow(["Alice", 24, "Sao Paulo"])
    escritor.writerow(["Bob", 30, "Rio de Janeiro"])
    escritor.writerow(["Carol", 22, "Belo Horizonte"])
    
print("Arquivo CSV criado com sucesso!")

#2. Lendo arquivo CSV

with open("dados.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)  # Exibe cada linha do arquivo
        
#3. Manipulação de Pastas com `os` e `shutil`

import os
import shutil

# Criando uma poasta

if not os.path.exists("nova_pasta"):
    os.mkdir("nova_pasta")
    print("Pasta 'nova_pasta' criada com sucesso!")

# Movendo o arquivo CSV para a nova pasta
shutil.move("dados.csv", "nova_pasta/dados.csv")
print("Arquivo movido para 'nova_pasta'!")

# listando arquivos na pasta
print("Arquivos em 'nova_pasta':", os.listdir("nova_pasta"))