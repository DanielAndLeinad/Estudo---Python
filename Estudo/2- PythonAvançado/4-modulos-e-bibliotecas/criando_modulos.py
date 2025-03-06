"""
# Módulos e Bibliotecas em Python

## 1. Introdução
Em python, um "Módulo" é um arquivo que contém código em pyhton reutilizavel. Ele pode conter funções, classes
e variáveis.
Uma "Biblioteca" é um conjunto de módulos que oferecem funcionalidades específicas.

## 2. Criando e importando Módulos 
Podemos criar nosso próprio módulo criando um arquivo '.py' e importando em outro código.

"""
import importex

nome_user = "Marcos"
print(importex.saudacao(nome_user))

"""
## 3. Diferentes formas de importação
Podemos importar um módulo inteiro, apenas funções especificas ou renomear módulos para facilitar o uso.

"""

#importando apenas a função saudação de importex.py

from importex import saudacao

print(saudacao("Olá"))


# Importando e renomeando
import importex as iptx
print(iptx.saudacao("Muinto bRABO"))  # Usamos o alias 'iptx'

"""
## 4. Criando um Pacote
Um "Pacote" é uma coleção de modulos organizados de uma pasta . Ele deve contar um arquivo especial ´__init__.py´

```
Estrutura de um pacote:

meu_pacote/
    __init__.py  # Indica que 'meu_pacote' é um pacote
    modulo1.py
    modulo2.py
    
    
Agora podemos importar os módulos dentro do pacote:

python
from meu_pacote import modulo1
```

"""
"""
## 5. Módulos Embutidos no Python
Python já vem com vários módulos embutidos que podemos usar sem instalar nada, como `math`, `random` e `datetime`.

"""

import math
print(math.sqrt(16)) # raiz de 16

import random
print(random.randint(1, 10)) #numero aleatorio entre 1 e 10

"""
## 6. Instalando e Usando Bibliotecas Externas
Podemos instalar bibliotecas externas com o gerenciador de pacotes `pip`.
Exemplo:
```
pip install requests

```
abra o terminal > pip install requests > aceite a criação do ".venv" caso não tenha criado anteriormente.

Depois de instalar, podemos usá-la:
"""

import requests

resposta = requests.get("https://www.google.com")
print(resposta.status_code) #exibe cod. de status HTTP

## 7. Projeto Prático: Criando um Pacote de Utilidades. 
## Vamos criar um pacote chamado `utilidades` contendo dois módulos:
## CONTINUAÇÃO NA PASTA UTILIDADES E NO ARQUIVO MAIN.PY


"""
## 8. Conclusão
Aprendemos sobre:
- Criação e importação de módulos
- Diferentes formas de importação
- Pacotes
- Módulos embutidos
- Bibliotecas externas
- Criamos um projeto prático

Para mais informações, consulte a documentação oficial:
- Módulos: https://docs.python.org/pt-br/3/tutorial/modules.html
- Pacotes: https://docs.python.org/pt-br/3/tutorial/modules.html#packages
"""