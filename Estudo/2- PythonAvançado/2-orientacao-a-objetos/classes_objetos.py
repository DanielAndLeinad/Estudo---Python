# ==========================
# CLASSE CARRO (Classe → Modelo para criar objetos)
# ==========================
class Carro:  # CLASSE: Define o modelo de um carro
    """Classe que representa um carro."""
    def __init__(self, marca, modelo, ano):  # MÉTODO: Construtor da classe
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao_carro(self):  # MÉTODO: Função que pertence à classe Carro
        """Retorna uma descrição do carro."""
        return f"{self.ano} {self.marca} {self.modelo}"

# OBJETO: Criando um carro a partir da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022)

# MÉTODO SENDO CHAMADO: Usando o método descricao_carro() do objeto
print(meu_carro.descricao_carro())  # Exibe a descrição do carro

# ==========================
# CLASSE PESSOA (Classe → Modelo para criar objetos)
# ==========================
class Pessoa:  # CLASSE: Define o modelo de uma pessoa
    """Classe que representa uma pessoa."""
    def __init__(self, nome, idade):  # MÉTODO: Construtor da classe
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):  # MÉTODO: Função que pertence à classe Pessoa
        """Retorna uma saudação da pessoa."""
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# OBJETO: Criando uma pessoa a partir da classe Pessoa
pessoa1 = Pessoa("Marcos", 21)

# MÉTODO SENDO CHAMADO: Usando o método cumprimentar() do objeto
print(pessoa1.cumprimentar())  # Exibe a saudação

# ==========================
# CLASSE CACHORRO (Classe → Modelo para criar objetos)
# ==========================
class Cachorro:  # CLASSE: Define o modelo de um cachorro
    """Classe que representa um cachorro."""
    def __init__(self, nome, raca, idade):  # MÉTODO: Construtor da classe
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):  # MÉTODO: Função que pertence à classe Cachorro
        """Simula um latido do cachorro."""
        return f"{self.nome} ({self.raca}) está latindo: Au Au!"

# OBJETO: Criando um cachorro a partir da classe Cachorro
meu_cachorro = Cachorro("Thor", "Labrador", 3)

# MÉTODO SENDO CHAMADO: Usando o método latir() do objeto
print(meu_cachorro.latir())  # Exibe a ação do cachorro

# ==========================
# FUNÇÃO FORA DAS CLASSES (Função → Bloco de código independente)
# ==========================
def criar_carro(marca, modelo, ano):  # FUNÇÃO: Código que cria e retorna um objeto Carro
    """Cria um objeto Carro e o retorna"""
    carro = Carro(marca, modelo, ano)  # OBJETO: Criando um novo carro
    return carro  # Retorna o carro criado

# OBJETO: Criando um carro através da função
meu_novo_carro = criar_carro("Chevrolet", "Cruze", 2019)

# MÉTODO SENDO CHAMADO: Usando o método descricao_carro() do objeto criado pela função
print(meu_novo_carro.descricao_carro())
