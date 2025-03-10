"""
# Automação com Python: Conexão com Firebase, MongoDB e MySQL

## Introdução
# Este material ensinará a conectar Python a três bancos de dados distintos:
# Firebase (banco NoSQL na nuvem da Google)
# MongoDB (banco de dados NoSQL orientado a documentos)
# MySQL (banco de dados relacional SQL)
# Cada seção terá uma explicação detalhada, exemplos comentados e um projeto prático ao final.

"""

# Conexão com MySQL usando Python

# Instalando a biblioteca necessária:
# pip install mysql-connector-python


import mysql.connector

# Criar conexão com o MySQL

conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Substitua pelo seu usuário do MySQL
    password="sua_senha",
    database="meu_banco"  # Substitua pelo seu banco de dados    
    
)

cursor = conn.cursor()

# Criar uma tabela (se não existir)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT,
        cidade VARCHAR(255)
    )
""")

# Inserir um usuário na tabela

cursor.execute("INSERT INTO usuarios (nome, idade, cidade) VALUES (%s, %s, %s)", ("Carlos", 28, "Curitiba"))
conn.commit()

# Ler um usuário do banco
cursor.execute("SELECT * FROM usuarios WHERE nome = 'Carlos'")
usuario = cursor.fetchone()
print("Dados do Usuario: ", usuario)

# Fechar conexão
cursor.close()
conn.close()