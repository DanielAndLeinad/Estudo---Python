# HERENÇA, POLIMORFISMO, ENCAPSULAMENTO E ABSTRAÇÃO

# HERANÇA
# É um mecanismo que permite que uma classe herde atributos e métodos de outra classe.
# A classe que herda é chamada de subclasse e a classe que é herdada é chamada de superclasse.

# POLIMORFISMO
# É a capacidade de um objeto poder ser referenciado de várias formas.
# O polimorfismo permite que um objeto de uma subclasse seja tratado como um objeto de uma superclasse.
# O polimorfismo é uma característica da orientação a objetos que permite que um objeto possa ser referenciado de várias formas.

# ENCAPSULAMENTO
# É o mecanismo que restringe o acesso aos atributos e métodos de uma classe.
# O encapsulamento é uma forma de proteger os atributos e métodos de uma classe, evitando que sejam acessados diretamente.

# ABSTRAÇÃO
# É a capacidade de abstrair um objeto do mundo real.
# A abstração é uma forma de simplificar um objeto do mundo real, tornando-o mais fácil de ser representado em um programa.


# Exemplo de Encapsulamento

# Encapsulamento é o mecanismo que restringe o acesso aos atributos e métodos de uma classe.
# O encapsulamento é uma forma de proteger os atributos e métodos de uma classe, evitando que sejam acessados diretamente.
# Em Python, usamos '_' (protegido) e '__' (privado) para restringir o acesso aos atributos.

'''
 Perguntas Práticas (resolva no código)
1- Encapsulamento: Modifique a classe ContaBancaria e crie um método chamado 
ver_senha() que retorne o valor de __senha. Por que agora conseguimos acessar o atributo privado?

2- Herança: Crie uma nova classe ContaEmpresarial que herda de ContaBancaria, 
mas adiciona um método solicitar_emprestimo(valor), permitindo que o saldo fique negativo até um limite de -5000.

3- Polimorfismo: Adicione um método transferir(valor, destino) em ContaBancaria e 
sobrescreva ele em ContaCorrente, aplicando uma taxa de 2% para transferências.

4- Abstração: Tente criar uma nova classe Pagamento como abstrata, 
com um método realizar_pagamento(), e depois crie duas subclasses Pix e Cartao que implementam esse método de formas diferentes.




'''





class contaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Atributo público
        self._saldo = saldo  # Atributo protegido
        self.__senha = "1234"  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        print(f"Saldo: R$ {self._saldo}")
        
    def ver_senha(self):
        print(f"Senha: {self.__senha}")
    
    def transferirValor(self, valor, destino):
        if valor <= self._saldo:
            self._saldo -= valor
            destino._saldo += valor
            print(f"Transferência de R$ {valor} realizada com sucesso.")


# teste de encapsulamento

conta = contaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
conta.ver_saldo()
# conta.__senha  # Atributo privado não pode ser acessado diretamente

# HERANÇA
# É um mecanismo que permite que uma classe herde atributos e métodos de outra classe.
# A classe que herda é chamada de subclasse e a classe que é herdada é chamada de superclasse.


class contaPoupanca(contaBancaria):
    def __init__(self, titular, saldo, juros):
        super().__init__(titular, saldo)
        self.juros = juros

    def aplicar_juros(self):
        self._saldo += self._saldo * self.juros / 100
        print("Juros aplicados.")
        

class ContaEmpresarial(contaBancaria):
    def solicitar_emprestimo(self, valor):
        if valor <= 5000:  # Permitindo saldo negativo até -5000
            self._saldo += valor
            print(f"Empréstimo de R${valor} aprovado!")
        else:
            print("Empréstimo negado. Limite de R$5000 ultrapassado.")

        


# teste de herança
pouponca = contaPoupanca("Maria", 1000, 0.5)
pouponca.aplicar_juros()
pouponca.ver_saldo()

# POLIMORFISMO
# É a capacidade de um objeto poder ser referenciado de várias formas.
# O polimorfismo permite que um objeto de uma subclasse seja tratado como um objeto de uma superclasse.
# O polimorfismo é uma característica da orientação a objetos que permite que um objeto possa ser referenciado de várias formas.


class contaCorrente(contaBancaria):
    def sacar(self, valor):
        taxa = 5  # taxa de saque
        if valor + taxa <= self._saldo:
            self._saldo -= valor + taxa
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
        
    def transferirValor(self, valor, destino):
        taxa = valor * 0.02 # taxa de transferência
        if valor + taxa <= self._saldo:
            self._saldo -= valor + taxa
            destino._saldo += valor
            print(f"Transferência de R$ {valor} realizada com sucesso.")
        else:
            print("Saldo insuficiente.")
        


# teste de polimorfismo
corrente = contaCorrente("José", 1000)
corrente.sacar(200)
corrente.ver_saldo()


# ABSTRAÇÃO
# É a capacidade de abstrair um objeto do mundo real.
# A abstração é uma forma de simplificar um objeto do mundo real, tornando-o mais fácil de ser representado em um programa.

from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod  # método abstrato
    def sacar(self, valor):
        pass  # Método abstrato, forçando subclasses a implementá-lo.


class NovaContaCorrente(Conta):
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
            
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def realizar_pagamento(self, valor):
        pass  # Esse método precisa ser implementado por qualquer subclasse

class Pix(Pagamento):
    def realizar_pagamento(self, valor):
        print(f"Pagamento de R${valor} via Pix realizado!")

class Cartao(Pagamento):
    def realizar_pagamento(self, valor):
        print(f"Pagamento de R${valor} via Cartão realizado!")

# Isso dá erro: "TypeError: Can't instantiate abstract class Pagamento..."
# pagamento = Pagamento()

pagamento_pix = Pix()
pagamento_pix.realizar_pagamento(100)  # "Pagamento de R$100 via Pix realizado!"

pagamento_cartao = Cartao()
pagamento_cartao.realizar_pagamento(250)  # "Pagamento de R$250 via Cartão realizado!"


    

# teste de abstração

nova_conta = NovaContaCorrente("Ana", 3000)
nova_conta.sacar(500)
nova_conta.sacar(4000)


# Uniao de todos os conceitos

class Banco:
    def __init__(self):
        self.contas = []
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
    def listar_contas(self):
        for conta in self.contas:
            print(f"Titular: {conta.titular}, Saldo: {conta._saldo}")
            
#criando banco e adicionando contas

banco = Banco()
banco.adicionar_conta(pouponca)
banco.adicionar_conta(corrente)
banco.adicionar_conta(nova_conta)

banco.listar_contas()