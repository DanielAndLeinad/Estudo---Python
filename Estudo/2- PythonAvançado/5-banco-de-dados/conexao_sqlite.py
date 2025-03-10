import sqlite3

# Passo 1: Criando e conectando ao banco de dados
# Se o arquivo 'meu_banco.db' não existir, ele será criado automaticamente

conexao = sqlite3.connect("meu_banco.db")

# Criando um cursor para executar comandos SQL

cursor = conexao.cursor()

# Passo 2: Criando uma tabela

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Salvando as mudanças
conexao.commit()


# Passo 4: Consultando os dados

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
print("Lista de usuarios")
for usuario in usuarios:
    print(usuario)
    
# Passo 5: Atualizando dados

cursor.execute("DELETE FROM usuarios WHERE nome = 'bob'") 
conexao.commit()

# Passo 7: Fechando a conexão
conexao.close()

   