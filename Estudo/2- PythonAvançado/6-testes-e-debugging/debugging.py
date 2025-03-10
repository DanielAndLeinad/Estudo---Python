'''
# Debugging e Testes Unitários em Python

## Introdução
Este documento cobre os fundamentos de debugging e testes unitários em Python.
Ele apresenta desde os conceitos básicos até exemplos avançados, com explicações detalhadas e comentadas.

## Seções
1. **Introdução ao Debugging**
2. **Ferramentas de Debugging**
3. **Introdução aos Testes Unitários**
4. **Escrevendo Testes Unitários com unittest**
5. **Projeto Final: Aplicando Debugging e Testes Unitários**

Import	        Função
pdb >>	        Debugging interativo (pausar execução, inspecionar variáveis)
unittest >> 	Criar e rodar testes automatizados


'''
# 1. Introdução ao Debugging
print("Iniciando estudo sobre Debugging e Testes Unitários!")

# Erros comuns em Python
def dividir(a, b):
    return a / b  # Pode gerar erro se b for 0

# Tentando executar a função com um erro
try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(f"Erro encontrado: {e}")

# 2. Ferramentas de Debugging
import pdb  # Importa o módulo de debugging embutido no Python

def soma(a, b):
    pdb.set_trace()  # Pausa a execução para debugging
    return a + b

soma(5, 3)

# 3. Introdução aos Testes Unitários
import unittest

# Função a ser testada
def dobrar(numero):
    return numero * 2

# Criando um teste unitário
class TesteDobrar(unittest.TestCase):
    def test_dobrar(self):
        self.assertEqual(dobrar(2), 4)
        self.assertEqual(dobrar(5), 10)
        self.assertEqual(dobrar(-1), -2)

# Rodando os testes
if __name__ == "__main__":
    unittest.main()

'''
## Projeto Final
Será implementado um sistema de contas bancárias simples, onde aplicaremos debugging e testes unitários.
'''

# Definição da classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError("O valor do depósito deve ser positivo")
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente ou valor inválido")
    
    def consultar_saldo(self):
        return self.saldo

# Criando um teste para ContaBancaria
class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria("João", 1000)
    
    def test_depositar(self):
        self.conta.depositar(500)
        self.assertEqual(self.conta.saldo, 1500)
    
    def test_sacar(self):
        self.conta.sacar(300)
        self.assertEqual(self.conta.saldo, 700)
    
    def test_saldo_insuficiente(self):
        with self.assertRaises(ValueError):
            self.conta.sacar(2000)
    
# Rodando os testes finais
if __name__ == "__main__":
    unittest.main()
