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

4️⃣ Conectando FastAPI a um Banco de Dados SQLite
Crie um arquivo chamado `api&BD.py` e adicione o seguinte código:

`
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./banco.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Criando um modelo de usuário
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    senha = Column(String)

# Criando o banco de dados
Base.metadata.create_all(bind=engine)
```



"""