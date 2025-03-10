# 🚀 Guia de Estudo: Python para Automação

## 📌 Sobre
Este repositório contém um guia para revisão de estudo detalhado para aprender **Python para Automação** em até **2 horas** caso você tenha uma base anterior, do contrario pode demorar um pouco mais. Ele abrange desde os fundamentos da linguagem até automação web e consumo de APIs.
### Obs: É recomendado estudar junto com a documentação do Python.
---

## 📚 Conteúdo
### 🔹 1. Fundamentos Essenciais do Python 
✅ Sintaxe básica e estrutura do Python  
✅ Controle de fluxo (`if`, `for`, `while`)  
✅ Estruturas de dados (`list`, `tuple`, `dict`)  
✅ Funções  

**Exemplo:**
```python
# Função simples
 def saudacao(nome):
     return f"Olá, {nome}!"
print(saudacao("Marcos"))
```
📜 [Documentação do Python](https://docs.python.org/pt-br/3/)

---

### 🔹 2. Manipulação de Arquivos 
✅ Criar, ler e escrever arquivos  
✅ Manipular pastas com `os` e `shutil`  

**Exemplo:**
```python
import os
# Criar um arquivo e escrever nele
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Conteúdo do arquivo.")
print("Arquivo criado com sucesso!")
```
📜 [Módulo `os`](https://docs.python.org/3/library/os.html)

---

### 🔹 3. Automação Web com Selenium 
✅ Acessar páginas automaticamente  
✅ Preencher formulários e buscar elementos  

**Exemplo:**
```python
from selenium import webdriver

# Abrir o navegador e acessar o Google
driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)
driver.quit()
```
📜 [Selenium com Python](https://selenium-python.readthedocs.io/)

---

### 🔹 4. Consumo de APIs com `requests` 
✅ Fazer requisições HTTP  
✅ Enviar e receber dados de uma API  

**Exemplo:**
```python
import requests

# Requisição GET
resposta = requests.get("https://api.github.com")
print(resposta.json())
```
📜 [Requests - HTTP para humanos](https://requests.readthedocs.io/en/latest/)

---

## 📌 Como Usar este Repositório
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/python-automation-guide.git
```
2. Instale as dependências:
```bash
pip install selenium requests
```
3. Pratique os exemplos e edite os scripts conforme necessário.

---

## 🔎 Pesquisas Recomendadas
- "Python os module"
- "Python Selenium Web Scraping"
- "Python API requests examples"
- 📜 [Python Selenium Tutorial - Automate Websites and Create Botss](https://www.youtube.com/watch?v=NB8OceGZGjA&pp=ygUQd2ViZHJpdmVyIHB5dGhvbg%3D%3D)
- 📜 [Selenium - Automatize Qualquer Tarefa na Internet com Python](https://www.youtube.com/watch?v=71ECrViH_Ng&ab_channel=HashtagPrograma%C3%A7%C3%A3o)
---

## 🚀 Conclusão
Seguindo esse guia, você terá um conhecimento sólido de Python para automação em apenas 2 horas! 🎯

**📌 Autor:** Marcos Daniel  
**📌 Licença:** MIT

