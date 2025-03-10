'''
Automação com Python - Material Didático

Este documento abrange três áreas principais de automação com Python:
1. Envio de e-mails
2. Manipulação de arquivos
3. Automação Web

Cada seção contém uma explicação teórica detalhada, exemplos de código bem comentados e links para a documentação oficial.
No final, há um projeto prático que une todos os conceitos.
'''

'''
Automação Web com Python (Selenium)

Explicação:
O Selenium é uma biblioteca que permite interagir com páginas da web automaticamente.
É necessário instalar o Selenium e um driver do navegador (ex: ChromeDriver para Google Chrome).
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializando o navegador (certifique-se de que o ChromeDriver está instalado e no PATH)
navegador = webdriver.Chrome()
navegador.get("https://www.google.com")

# Encontrando o campo de pesquisa e buscando algo
campo_pesquisa = navegador.find_element("name", "q")
campo_pesquisa.send_keys("Automação com Python")
campo_pesquisa.send_keys(Keys.RETURN)

time.sleep(5)  # Espera para ver os resultados

# Fechando o navegador
navegador.quit()

print("Pesquisa realizada com sucesso!")