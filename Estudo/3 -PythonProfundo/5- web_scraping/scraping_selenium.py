'''
WEB SCRAPING COM SELENIUM

Este documento aborda a extração de dados de páginas web dinâmicas, utilizando 
Selenium para interagir com elementos da página.
'''

# 1. INSTALAÇÃO DAS BIBLIOTECAS NECESSÁRIAS
# Selenium requer a instalação do WebDriver correspondente ao navegador utilizado.
# Para instalar o Selenium, execute:

# pip install selenium

# Para baixar o WebDriver do Chrome:
# Acesse https://sites.google.com/chromium.org/driver/ e baixe a versão compatível com seu navegador.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 2. CONFIGURAÇÃO DO SELENIUM E ABERTURA DO SITE
# Aqui iniciamos o WebDriver e acessamos uma página.

# Configurando o WebDriver (ajuste o caminho conforme necessário)
driver = webdriver.Chrome()  # Se precisar especificar o caminho: webdriver.Chrome(executable_path='caminho/do/driver')

driver.get("https://books.toscrape.com/")  # Acessando o site

time.sleep(2)  # Aguardando o carregamento da página

# 3. EXTRAINDO DADOS DA PÁGINA
# Vamos pegar os títulos dos livros disponíveis.

books = driver.find_elements(By.TAG_NAME, "h3")  # Buscando todas as tags <h3>

print("Lista de livros disponíveis:")
for book in books:
    print(f"- {book.text}")  # Extraindo e exibindo os títulos

# 4. NAVEGAÇÃO ENTRE PÁGINAS
# Vamos clicar no botão "next" para ir para a próxima página (se houver).

try:
    next_button = driver.find_element(By.LINK_TEXT, "next")  # Buscando o botão "next"
    next_button.click()  # Clicando no botão
    time.sleep(2)  # Esperando a nova página carregar
    print("Mudança para a próxima página concluída!")
except:
    print("Não há próxima página disponível.")

# 5. FECHANDO O NAVEGADOR
# Sempre finalize o WebDriver após o uso.
driver.quit()

'''
REFERÊNCIAS:
- Documentação oficial do Selenium: https://www.selenium.dev/documentation/
- Site de teste para scraping: https://books.toscrape.com/
'''
