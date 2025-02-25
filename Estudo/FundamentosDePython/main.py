# Data: 24/02/2025
# exemplo de uso de print
print("quero meu primeiro emprego")

# exemplo de uso de variaveis + input
nome = input("Qual seu nome nerdola?: ")
idade = int(input("Qual sua idade?: "))
peso = float(input("Qual seu peso?: "))

# exemplo de uso de print com variaveis
print("Seu nome é", nome, "sua idade é", idade, "e seu peso é", peso)
print(nome)
print(type(idade))
print(type(peso))

# exemplo de uso de operadores aritmeticos
soma = 10 + 10
multiplicacao = 10 * 10
divisao = 10 / 10
subtracao = 10 - 10
exponenciacao = 10 ** 10
resto = 10 % 3

# exemplo de uso de print com operadores aritmeticos
print(soma)
print(multiplicacao)
print(divisao)
print(subtracao)
print(exponenciacao)
print(resto)


# exemplo de uso de operadores relacionais
idade = int(input("Qual sua idade?: "))

# exemplo de uso de print com operadores relacionais
if idade > 18:
    print("Você é maior de idade")
elif idade == 18:
    print("Você tem 18 anos")
else:
    print("Você é menor de idade")
    
# segundo exemplo

salario = float(input("Qual seu salario?: "))

# exemplo de uso de print com operadores relacionais
# exemplo de uso de operadores logicos
if salario >= 1000:
    print("programador junior")
elif salario >= 3000 and salario <= 5000:
    print("programador pleno")
elif salario >= 5000 and salario <= 10000:
    print("programador senior")
else:
    print("gerente de projeto")

#--------------------------------------

# Exemplo de listas
lista_numeros = [1, 2, 3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

# Usando append para adicionar elementos na lista
lista_vazia = []
lista_vazia.append("olá")
lista_vazia.append("mundo")

print(lista_vazia)



# Método      Parâmetros      Resultado       Descrição
# append      item            mutador         Acrescenta um novo item no final da lista
# insert      posição, item   mutador         Insere um novo item na posição dada
# pop         nenhum          híbrido         Remove e retorna o último item
# pop         posição         híbrido         Remove e retorna o item da posição
# sort        nenhum          mutador         Ordena a lista
# reverse     nenhum          mutador         Ordena a lista em ordem reversa
# index       item            retorna idx     Retorna a posição da primeira ocorrência do item
# count       item            retorna ct      Retorna o número de ocorrências do item
# remove      item            mutador         Remove a primeira ocorrência do item
# extend      iterável        mutador         Acrescenta os itens do iterável no final da lista

#--------------------------------------

# Falando sobre repetição

notas = []

 # Exemplo de uso de for - (variavel "x" é um valor que sera alterado a cada repetição)
for x in range(5):
   codigo_aluno = input("Digite o código do aluno: ")
   nota = float(input("Digite a nota do aluno: "))
   resultado = [codigo_aluno, nota]
   notas.append(resultado)  

print("Quantidade de notas: ", len(notas))

# Exemplo de uso de for - (variavel "n" é um valor que sera alterado a cada repetição)
# repetiçao para exibir as notas dentro de outra repetição
for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O aluno", codigo_aluno, "tirou a nota", nota)    
    
# Usando while
    contador = 1
 
    while contador <= 5:
        codigo_aluno = input("Digite o código do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        resultado = [codigo_aluno, nota]
        notas.append(resultado)
# alternativa
        contador += 1
        #ou
        contador = contador + 1
print("Quantidade de notas: ", len(notas))


# dicionario
# Exemplo de dicionario

pessoa = {
    "nome": "Marcos",
    "idade": 21,
    "peso": 54.5
}

print(pessoa["nome"])	
print(pessoa["idade"])
print(pessoa["peso"])

player = {
    "nome": "Marcos",
    "vida": 100,
    "forca": 10,
    "defesa": 5
}

npcs = {
    {"nome": "Gurp", "vida": 100, "forca": 10, "defesa": 5},
    {"nome": "Ilay", "vida": 100, "forca": 10, "defesa": 5},
    {"nome": "Jorn", "vida": 100, "forca": 10, "defesa": 5},
    {"nome": "Klur", "vida": 100, "forca": 10, "defesa": 5},
}