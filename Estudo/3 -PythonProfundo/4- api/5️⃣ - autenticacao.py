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
## 5️⃣ Implementando Autenticação com Hash de Senhas
Crie um arquivo chamado `autenticacao.py` e adicione o seguinte código:


from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(BaseModel):
    nome: str
    senha: str

usuarios_db = {}

@app.post("/registrar/")
def registrar(usuario: Usuario):
    senha_hash = pwd_context.hash(usuario.senha)
    usuarios_db[usuario.nome] = senha_hash
    return {"mensagem": "Usuário registrado com sucesso!"}

@app.post("/login/")
def login(usuario: Usuario):
    if usuario.nome not in usuarios_db or not pwd_context.verify(usuario.senha, usuarios_db[usuario.nome]):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    return {"mensagem": "Login realizado com sucesso!"}
```



"""