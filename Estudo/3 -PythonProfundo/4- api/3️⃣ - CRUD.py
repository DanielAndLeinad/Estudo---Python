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
## 3️⃣ Criando um CRUD com FastAPI
Crie um arquivo chamado `CRUD.py` e adicione o seguinte código:

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de dados
class Item(BaseModel):
    id: int
    nome: str
    descricao: str

# Banco de dados fictício
banco_dados = []

@app.post("/items/", response_model=Item)
def criar_item(item: Item):
    banco_dados.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def listar_items():
    return banco_dados
```



"""