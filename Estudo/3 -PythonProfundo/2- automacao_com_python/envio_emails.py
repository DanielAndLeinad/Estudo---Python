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
Envio de E-mails com Python

Explicação:
O envio de e-mails pode ser feito usando o módulo smtplib para SMTP e email.mime para formatar as mensagens.

Pré-requisitos:
- Uma conta de e-mail (ex: Gmail)
- Ativar a autenticação para aplicativos menos seguros (caso necessário)
- Instalar a biblioteca smtplib (já incluída no Python)
'''

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do e-mail

EMAIL_REMETENTE = "seuemail@gmail.com"
senha = "suasenha"
EMAIL_DESTINATARIO = "destino@gmail.com"

# Criando a mensagem

msg = MIMEMultipart()
msg["from"] = EMAIL_REMETENTE
msg["to"] = EMAIL_DESTINATARIO
msg["subject"] = "Teste automação"

# Corpo do e-mail
corpo = "Este é um email de teste"
msg.attach(MIMEText(corpo, "plain"))

# Enviando o e-mail

try:
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(EMAIL_REMETENTE, senha)
    servidor.sendmail(EMAIL_REMETENTE, EMAIL_DESTINATARIO, msg.as_string())
    servidor.quit()
    print("E-mail enviado com sucesso")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
