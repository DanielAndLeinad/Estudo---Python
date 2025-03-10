"""
# Automação com Python: Conexão com Firebase, MongoDB e MySQL

## Introdução
# Este material ensinará a conectar Python a três bancos de dados distintos:
# Firebase (banco NoSQL na nuvem da Google)
# MongoDB (banco de dados NoSQL orientado a documentos)
# MySQL (banco de dados relacional SQL)
# Cada seção terá uma explicação detalhada, exemplos comentados e um projeto prático ao final.

"""

# Conexão com Firebase usando Python

# Instalando a biblioteca necessária:
# pip install firebase-admin

import firebase_admin

from firebase_admin import credentials, firestore

# Carregar credenciais do Firebase

cred = credentials.Certificate("caminho/para/arquivo.json") # Substitua pelo caminho correto do arquivo JSON
firebase_admin.initialize_app(cred)

# Criar uma conexão com o Firestore
db = firestore.client()

# Criar um novo documento no Firestore
dados = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
db.collection("usuarios").document("usuario1").set(dados)

# Ler um documento do Firestore
doc = db.collection("usuarios").document("usuario1").get()
if doc.exists:
    print("Dados do usuário:", doc.to_dict())
