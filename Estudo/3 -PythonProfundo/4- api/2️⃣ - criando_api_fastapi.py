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

"""
## 2️⃣ Criando uma API com FastAPI
Crie um novo arquivo chamado `criando_api_fastapi.py` e adicione o seguinte código:


from fastapi import FastAPI

# Criando a aplicação
app = FastAPI()

@app.get("/")
def home():
    
    Rota raiz que retorna uma mensagem de boas-vindas.
    
    return {"mensagem": "Bem-vindo à minha API!"}

@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    
   
    return {"mensagem": f"Olá, {nome}!"}
```



"""