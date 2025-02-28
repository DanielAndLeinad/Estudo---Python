abrir = open('teste.txt', 'r')
print(abrir.read())

# Necessario que o arquivo teste.txt esteja no mesmo diretorio que o arquivo leitura_escrita.py
# Caso contrario, o python retornara um erro
# O usuario também precisa estar dentro da pasta, no caso:

# cd estudo
# cd '.\2- BaseSolidaPython\'
# cd .\1-manipulacao-de-arquivos\
    #execute "python + nome do arquivo.py"
# python .\leitura_escrita.py
    # Aperte TAB para autocompletar .