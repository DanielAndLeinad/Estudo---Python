"""
# Automação com Python: Conexão com Firebase, MongoDB e MySQL

## Introdução
# Este material ensinará a conectar Python a três bancos de dados distintos:
# Firebase (banco NoSQL na nuvem da Google)
# MongoDB (banco de dados NoSQL orientado a documentos)
# MySQL (banco de dados relacional SQL)
# Cada seção terá uma explicação detalhada, exemplos comentados e um projeto prático ao final.

"""
# Conexão com MongoDB usando Python

# Instalando a biblioteca necessária:
# pip install pymongo

from pymongo import MongoClient

# Conectar ao servidor MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Substitua pelo endereço do seu MongoDB

# Criar banco e coleção
db = client["meu_banco"]
colecao = db["usuarios"]

# Inserir um documento no MongoDB
dados = {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"}
colecao.insert_one(dados)

# Ler um documento do MongoD
usuario = colecao.find_one({"nome": "Maris"})
print("Dados dos usuarios", usuario)