# Este é um DOCUMENTO PROGRAMADO criado no dia 03/03/2025,com intuito de estudar POO em Python.
# Autor: Marcos

# Objetivo é simplemeste estudar POO em Python, e ajudar aqueles com algum tipo de dificuldade.
# Este documento é livre para ser copiado,modificado e distribuido,desde que seja mantido o nome do autor e o link de origem.

### INDICE:
"""
1. Introdução à POO
2. Classes e Objetos
3. Encapsulamento
4. Herança
5. Polimorfismo
6. Abstração
7. Projeto Prático Integrando Todos os Conceitos
8. Referências
"""

#  ============================
#  | 1. Introdução à POO      |
#  ============================
""" 

A Programação Orientada a Objetos (POO) ↓
é um paradigma de programação baseado no conceito de "objetos", que possuem atributos (dados) e métodos (funções).
° Os 4 pilares da POO são:
- **Encapsulamento: Restringe o acesso direto aos atributos e permite controle por métodos.
- **Herança: Permite que uma classe herde atributos e métodos de outra.
- **Polimorfismo: Permite que um mesmo método tenha diferentes comportamentos.
- **Abstração: Define um modelo base sem especificar a implementação completa.

--------------------------------------------
Agora, usando na pratica:

"""

# ============================
# 2. Classes e Objetos
# ============================


#Definição de uma classe simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome #atributo público
        self.idade = idade #atributo público
        
    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")
        
# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Marcos", 21)
print(pessoa1.apresentar()) #Olá, eu sou Marcos e tenho 21 anos.

# ============================
# 3. Encapsulamento
# ============================

"""
° Encapsulamento restringe o acesso a determinados atributos de uma classe.

- Atributos públicos: Podem ser acessados de qualquer lugar (`self.nome`)
- Atributos protegidos: Devem ser acessados apenas dentro da classe ou subclasses (`self._saldo`)
- Atributos privados: Não podem ser acessados diretamente (`self.__senha`)
"""

class contaBancaria:
    def __init__(self, titular, senha, saldo):
        self.titular = titular #atributo público
        self._saldo = saldo #atributo protegido
        self.__senha = senha #atributo privado
        
    def ver_saldo(self):
        return f"Saldo atual: R$ {self._saldo}"
    
    def altera_senha(self, nova_senha):
        self.__senha = nova_senha
        return "Senha alterada com sucesso!"
    
# Criando uma conta 
conta1 = contaBancaria("Marcos", 1234, 1000)
print(conta1.ver_saldo()) #Saldo atual: R$ 1000
# print(conta1.__senha)  # ERRO! Não pode acessar diretamente atributos privados.

# ------------------------------
# 4. Herança
# ------------------------------

"""
Herança permite que uma classe (filha) reutilize atributos e métodos de outra (pai).
"""

class contaCorrente(contaBancaria):
    def __init__(self, titular, senha, saldo, limite):
        super().__init__(titular, saldo, senha) # super() chama o construtor da classe pai. Construtor é o método __init__()
        self.limite = limite
        
    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self._saldo -= valor
            return f"Saque de R$ {valor} realizado com sucesso!"
        return "saldo insuficiente"
    
    
# ------------------------------
# 5. Polimorfismo
# ------------------------------

"""
Polimorfismo permite que métodos com o mesmo nome tenham diferentes implementações.
"""

class contaPoupanca(contaBancaria):
    def sacar(self, valor):
        if valor <=self._saldo:
            self._saldo -= valor
            return f"Saque de R$ {valor} realizado da poupança!"
        return "Saldo insuficiente!"
    
# ============================
# 6. Abstração
# ============================

"""
Abstração define uma classe base sem especificar sua implementação completa.
"""

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class pagamentoPix(Pagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor} via Pix realizado!"
    


# ============================
# 7. Projeto Prático
# ============================
"""
Vamos criar um sistema bancário que usa todos os conceitos aprendidos.
"""


class Banco:
    def __init__(self):
        self.contas = []
    
    def adicionar_conta(self, conta):
        return "Conta adicionada ao banco!"
    
    def listar_contas(self):
         return [f"Titular: {conta.titular}, Saldo: R$ {conta._saldo}" for conta in self.contas]
     

# Criando contas e adicionando ao banco

banco = Banco()
conta_cc = contaCorrente("Marcos", 1234, 1000, 500)
conta_cp = contaPoupanca("Daniel", 1234, 5000)

banco.adicionar_conta(conta_cc)
banco.adicionar_conta(conta_cp)
print(banco.listar_contas())

# ============================
# 8. Referências
# ============================
"""
- Documentação oficial: https://docs.python.org/pt-br/3/tutorial/classes.html
- Livro: "Python Orientado a Objetos" - Grégorio Nascimento
- Artigo sobre POO: https://realpython.com/python3-object-oriented-programming/
"""