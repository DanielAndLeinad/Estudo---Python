"""
WEB SCRAPING COM REQUESTS E BEAUTIFULSOUP

Este doc. aborda a extração de dados de paginas web de forma estatica, 
utilizando bibliotecas request e beautifulsoup

"""

# 1. Instalação das bibliotecas necessárias
# Primeiro, presicamos instalar as bibliotecas request e beautifulsoup
# Para isso, execute os seguintes comando no CMD/PROMPT

# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# 2. FAZENDO UMA REQUISIÇÃO HTTP
# Vamos fazer uma requisição para um site e obter o conteúdo HTML.

url = "https://books.toscrape.com/"  # Site de exemplo com livros disponíveis para scraping
response = requests.get(url) # Fazendo a requisição GET para a URL

# Verificando se a requisição foi bem-sucedida (código 200)

if response.status_code == 200:
    html_content = response.text # Obtendo o conteúdo HTML da página
    print("Requisição bem-sucedida! HTML obtido.")
else:
    print(f"Erro na requisição: {response.status_code}") 
    
# 3. PARSEANDO O HTML COM BEAUTIFULSOUP
# Agora vamos analisar o HTML e extrair informações específicas.

soup = BeautifulSoup(html_content, "html_parser")  # Criando o objeto BeautifulSoup

# Extraindo o título da página
page_title = soup.title.text  # Obtendo o texto dentro da tag <title>
print(f"Título da página: {page_title}")

# 4. EXTRAINDO DADOS ESPECÍFICOS
# Vamos extrair os títulos dos livros exibidos na página inicial do site.

books = soup.find_all("h3")  # Buscando todas as tags <h3>, que contêm os títulos dos livros

print ("Lista de livros disponiveis: ")
for book in books:
    book_title = book.a["title"] # Extraindo o título do livro da tag <a>
    print(f"- {book_title}")
    
# 5. PROJETO PRÁTICO: EXTRAÇÃO DE TÍTULOS E PREÇOS
# Vamos agora extrair os títulos e preços dos livros e armazená-los em uma lista.

book_data = []  # Lista para armazenar os dados

for book in soup.find_all("article", class_ = "product_pod"):
    title = book.h3.a["title"]  # Obtendo o título do livro
    price = book.find("p", class_="price_color").text  # Obtendo o preço do livro
    book_data.append({"Titulo": title, "Preço": price})

# Exibindo os resultados
print("\nLista de livros e preços:")
for item in book_data:
    print(f"{item['Título']} - {item['Preço']}")



'''
REFERÊNCIAS:
- Documentação oficial do requests: https://docs.python-requests.org/en/latest/
- Documentação oficial do BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Site de teste para scraping: https://books.toscrape.com/
'''
