# Importando a biblioteca csv
import csv
# Abrindo o arquivo csv no terminal
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
with open("teste.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)