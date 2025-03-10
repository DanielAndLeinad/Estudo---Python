'''
Automação com Python - Material Didático

Este documento abrange três áreas principais de automação com Python:
1. Envio de e-mails
2. Manipulação de arquivos
3. Automação Web

Cada seção contém uma explicação teórica detalhada, exemplos de código bem comentados e links para a documentação oficial.
No final, há um projeto prático que une todos os conceitos.
'''

'''
Manipulação de Arquivos com Python

Explicação:
Python permite criar, ler, escrever e manipular arquivos usando a função open().
Isso é útil para registrar logs, armazenar dados ou processar informações automaticamente.
'''

# Criando e escrevendo em um arquivo

with open("arquivo_tst.txt", "w") as arquivos:
    arquivos.write("Este é um arquivo criado via Python.\n")
    arquivos.write("Podemos adicionar múltiplas linhas.\n")
print("Arquivo criado com sucesso")

# Lendo um arquivo

with open ("arquivo_tst.txt", "r") as arquivos:
    arquivos.write("Esta linha foi adicionada posteriormente.\n")
    
print("Linha adicionada com sucesso")

# Lendo linha por linha
with open("arquivo_tst.txt", "r") as arquivos:
    print("Lendo linha por linha: ")
    for linha in arquivos:
        print(linha.strip())