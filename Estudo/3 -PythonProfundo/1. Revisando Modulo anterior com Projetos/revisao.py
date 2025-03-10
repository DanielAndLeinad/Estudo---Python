'''
# Revisão de Módulos Estudados em Python

Este documento cobre os principais QUE EU considero como tópicos importantes estudados até agora:
- Estruturas de Dados (listas, tuplas, dicionários)
- Módulos e bibliotecas
- Programação Orientada a Objetos (POO)
- Banco de Dados (SQLite)
- Debugging e Testes Unitários

Cada seção contém explicações detalhadas, exemplos de código comentados e referências à documentação.

No final, há dois projetos práticos para consolidar os conceitos aprendidos.
'''

# 1. Estruturas de Dados

# Listas

lista = [1,2,3,4,5]
lista.append(6)
lista.remove(3)
print(lista)

# Tuplas (imutáveis)
tuplas = (10,20,30)
print(tuplas(1))

# Dicionários (chave-valor)

dicionario = {'nome': 'Alice', 'idade': 25}
print(dicionario['nome'])  # Alice
dicionario['idade'] = 26  # Modificando valor

# 2. Módulos e Bibliotecas

import math
print(math.sqrt(16))

# Criando um módulo próprio (exemplo simplificado)

def saudacao(nome):
    return f"Olá{nome}"

# 3. Programação Orientada a Objetos

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."
    
    
pessoa = pessoa("Carlos", 32)
print(pessoa.apresentar())

# 4. Conexão com SQLite
import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)''')
cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', ("Ana",))
conexao.commit()

# 5. Debugging e Testes Unitários

import unittest

def soma(a,b):
    return a + b

class TestesMatematicos(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2,3),5)
        self.assertEqual(soma(-1,1), 0)
        
if __name__ == '__main__':
    unittest.main()
    
'''
# Projeto 1: Sistema de Gerenciamento de Usuários (Banco de Dados + POO)

Este projeto cria um sistema de cadastro de usuários utilizando SQLite e classes Python.
'''

class usuario:
    def __init__(self, nome):
        self.nome = nome
    
    def salvar(self):
        conexao = sqlite3.connect('banco.db')
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (self.nome,))
        conexao.commit()
        conexao.close()
        
        
usuario = usuario("Joao")
usuario.salvar()
print("Usuário salvo no banco de dados!")

'''
# Projeto 2: Validador de Dados com Testes Unitários

Este projeto implementa uma validação de email e um conjunto de testes unitários para garantir seu funcionamento correto.
'''

import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(padrao, email))

class TesteValidacao(unittest.TestCase):
    def teste_email_valido(self):
        self.assertTrue(validar_email("teste@email.com"))
        
    def teste_email_invalido(self):
        self.assertFalse(validar_email("email@com"))
        
if __name__ == '__main__':
    unittest.main()