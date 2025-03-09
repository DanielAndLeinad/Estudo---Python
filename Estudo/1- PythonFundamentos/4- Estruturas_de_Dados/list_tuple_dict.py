# Estruturas de Dados em Python: Listas, Tuplas e Dicionários

## 1. Listas (list)
# Listas são coleções ordenadas e mutáveis de elementos.
# Podem conter diferentes tipos de dados e permitem modificações.

# Criando uma LISTA

minha_lista = [1, 2, 3, 4, 5]
print("Minha lista: ", minha_lista)

#acessando elemtnos (indexaçao começa em 0)
print("Primeiro elemento: ", minha_lista[0])
print("Ultimo elemento: ", minha_lista[-1])

#modificando elementos da lista
minha_lista[2] = 99
print("Lista apos modificaçao: ", minha_lista)

#adicionando elementos na lista
minha_lista.append(6) #adicionando no final da lista
print("Lista apos o append: ", minha_lista)

minha_lista.insert(2, 42)
print("Lista apos o insert: ", minha_lista)

#removendo elementos
minha_lista.remove(42)
print("Apos a remover o 42: ", minha_lista)

ultimo = minha_lista.pop() #removendo o ultimo elemento da lista
print("Elemento removido: ", ultimo)
print("Lista apos o pop: ", minha_lista)

#iterando sobre lista
for item in minha_lista:
    print("elemento: ", item)
    
#compreensao de listas
quadrado = [x ** 2 for x in range(6)]
print("Lista de quadrados: ", quadrado)

## 2. Tuplas (tuple)
# Tuplas são coleções ordenadas e imutáveis de elementos.

#criando uma tupla
minha_tupla = ( 10, 20, 30, 40 )
print("Tupla: ", minha_tupla)

#acessando elementos 
print("Primeiro elemento: ", minha_tupla[0])

#Desempacotamento de tupla
a, b, c, d = minha_tupla
print("Valores desempacotados: ", a,b,c,d)

#convertendo lista em tupla
tupla_convertida = tuple(minha_lista)
print("Tupla convertida: ", tupla_convertida)

## 3. Dicionários (dict)
# Dicionários são coleções não ordenadas de pares chave-valor.

# Criando um dicionário
meu_dic = {"Nome: ": "Alice", "idade: ": 25, "cidade: ": "Sao Paulo"}
print("Dicionario: ", meu_dic)

#acessando valores
print("Nome: ", meu_dic["Nome: "])

#Modificando valores
meu_dic["idade: "] = 26
print("Dic apos modificaçao: ", meu_dic)

#adicionando novos pares de chave-valor
meu_dic["Profissao: "] = "Engenheiro"
print("Dic apos adiciçao: ", meu_dic)

#removendo elementos
del meu_dic["cidade: "]
print("dic apos remover um elemento: ", meu_dic)

#Iterando sobre dic
for chave, valor in meu_dic.items():
    print(f"chave: {chave}, valor: {valor}")
    
#Compreensao de dicionarios
quadrado_dic = {x: x ** 2 for x in range(6)}
print("Dic de quadrados: ", quadrado_dic)

## 4. Projeto Prático: Catálogo de Produtos
# Criamos um sistema de gerenciamento de produtos usando listas, tuplas e dicionários.

print("------------------------------------------------")


catalogo = {}

def adicionar_produtos(nome, preco, estoque):
    catalogo[nome] = {"preço": preco, "estoque": estoque}  # Correção nas chaves

def exibit_catalogo():
    for produtos, info in catalogo.items():
       print(f"{produtos}: Preço R${info['preço']}, Estoque: {info['estoque']}")  # Agora acessa as chaves corretamente

# Adicionando produtos 
adicionar_produtos("Notebook", 3500.00, 10)
adicionar_produtos("Mouse", 150.00, 50)
adicionar_produtos("Teclado", 200.00, 30)

# Exibindo catálogo
display_catalog = exibit_catalogo()


# Referências:
# https://docs.python.org/pt-br/3/tutorial/datastructures.html


