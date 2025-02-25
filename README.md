# 🚀 Guia de Estudo: Python para Automação

## 📌 Sobre
Este repositório contém um guia para revisão de estudo detalhado para aprender **Python para Automação** em **2 horas**. Ele abrange desde os fundamentos da linguagem até automação web e consumo de APIs.

---

## 📚 Conteúdo
### 🔹 1. Fundamentos Essenciais do Python (30 minutos)
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

### 🔹 2. Manipulação de Arquivos (30 minutos)
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
📺 [Vídeo recomendado](https://www.youtube.com/watch?v=54r7XrkicJg)  
📜 [Módulo `os`](https://docs.python.org/3/library/os.html)

---

### 🔹 3. Automação Web com Selenium (30 minutos)
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
📺 [Vídeo recomendado](https://www.youtube.com/watch?v=yiD09BpxaTo)  
📜 [Selenium com Python](https://selenium-python.readthedocs.io/)

---

### 🔹 4. Consumo de APIs com `requests` (30 minutos)
✅ Fazer requisições HTTP  
✅ Enviar e receber dados de uma API  

**Exemplo:**
```python
import requests

# Requisição GET
resposta = requests.get("https://api.github.com")
print(resposta.json())
```
📺 [Vídeo recomendado](https://www.youtube.com/watch?v=pmMQLHVDw58)  
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

---

## 🚀 Conclusão
Seguindo esse guia, você terá um conhecimento sólido de Python para automação em apenas 2 horas! 🎯

**📌 Autor:** Marcos Daniel  
**📌 Licença:** MIT

