"""
    Vamos separar sobre em 4 arquivos. 
Cada arquivo vai falar sobre um processo que faz parte do uso de uma API

'''
# 📌 Introdução às APIs e FastAPI com Python

Este material cobre desde o consumo de APIs até a criação de APIs completas usando FastAPI.

## 🔹 O que é uma API?
API (Application Programming Interface) é um conjunto de regras que permite que sistemas diferentes se comuniquem.

## 🔹 Instalando as dependências necessárias
Antes de começar, precisamos instalar algumas bibliotecas essenciais.

Abra o terminal e execute:
```
bash
pip install fastapi uvicorn requests sqlalchemy sqlite3 passlib[bcrypt]

```

---
"""

## 1️⃣ Consumindo APIs com requests
# Crie um arquivo chamado `consumindo_api.py` e adicione o seguinte código:
"""python
import requests

def consumir_api():
    
    Faz uma requisição GET para uma API pública e exibe os dados.
    
    url = "https://jsonplaceholder.typicode.com/posts/1"  # URL da API
    resposta = requests.get(url)  # Envia uma requisição GET
    
    if resposta.status_code == 200:
        dados = resposta.json()  # Converte a resposta para JSON
        print("Título:", dados["title"])
        print("Corpo:", dados["body"])
    else:
        print("Erro ao consumir API", resposta.status_code)

# Chamando a função para testar
consumir_api()

"""