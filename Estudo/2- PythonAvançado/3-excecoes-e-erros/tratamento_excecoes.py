# Tratamento e exeçoes em Python

# 1. Introdução a try and execept
# Em python, uma execeção de um erro ocorre durante a execução de um programa
# Se uma exceção não for tratada, o programa sera interrompido. 

""" Exemplo de erro sem tratamento

print( 10/0 ) #Isso gera um erro ZeroDivisionError
 
""" 

# 2. Capturando Execeções com try-except
# Para evitar que o programa pare, podemos usar try-except  

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão não permitida.")
    
# 3. Capturando multiplas exceções

try: 
    num = int("ABC") #Erro de valor (valueError)
except ZeroDivisionError:
    print("Error: Divisão por zero")
except ValueError:
    print("Error: Conversão Inválida")
    
# 4. Usando o Bloco "else" (Execurando se não houver error)

try:
    resultado = 10 /2
except ZeroDivisionError:
    print("Erro: Divisão por zero")
else:
    print("O resultado é: ", resultado)
    
# 5. Usando Bloco "finally" (Sempre executado, com ou sem erro)

try: 
    arquivo = open("Exemplo.txt", "w")
    arquivo.write("Escrevendo no arquivo")
except IOError:
    print("Error ao manipular o arquivo...")
finally:
    arquivo.close()
    print("Arquivo Fechado!")
    
# 6. Exceções com "raise"

    """ Sobre "raise" e "exept (variavel) as e"

    raise: O raise em Python é usado para levantar (ou lançar) uma exceção manualmente. 
    Isso significa que você pode interromper a execução normal do programa e gerar um erro quando uma condição específica for atendida.
    
    exept (variavel) as e: Esse bloco é um tratamento de exceção, que entra em ação se um erro do tipo ValueError for levantado.
    
    1. O Python detecta que o raise (variavel) foi acionado e pula para o bloco except.
    2. A parte as e captura a mensagem de erro que foi levantada no raise, armazenando-a na variável e.
    3. O comando print("Erros", e) exibe a mensagem do erro.
    
    Resumo:
    raise: levanta uma exceção manualmente.
    except (varivel) as e: captura o erro levantado e armazena a mensagem na variável e.
    
    Isso permite criar validações personalizadas no código, garantindo que erros sejam identificados e tratados corretamente.
    
    """

try:
    idade = -5
    if idade <=0:
        raise ValueError("Idade não pode ser negativa!")
except ValueError as e:
    print("Erros", e)    
    
    
    
# 7. Criando Exceções personalizadas

class erroPersonalizado(Exception):
    pass

try:
    raise erroPersonalizado("Isso é um erro personalizado!")
except erroPersonalizado as e:
    print("Capturando erro personalizado!", e)
    
# 8. Exemplo completo: Um pequeno sistema que lida com exceções

class Banco:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def sacar(self, valor):
        try:
            if valor > self.saldo:
                raise ValueError("Saldo Insuficiente")
            self.saldo -= valor
            print(f"Saque realizado. Novo saldo: {self.saldo}")
        except ValueError as e:
            print("Erro no saque:", e)
        finally:
            print("Operação Invalida")
            
conta = Banco(100)
conta.sacar(50)
conta.sacar(100)

# Documentação Oficial:
# https://docs.python.org/pt-br/3/tutorial/errors.html

