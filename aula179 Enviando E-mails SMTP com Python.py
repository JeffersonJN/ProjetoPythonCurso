# Enviando E-mails SMTP com Python
import os
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib


from dotenv import load_dotenv

load_dotenv()

# caminho arquivo html

CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula179a.html'
# Dados do remetente e destinatario

remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configuração do servidor SMTP

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagemde texto

with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Jefferson')

# trasforma nossa mensagem em MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este e o assundo do e-mail. '

corpo_do_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_do_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print("E-mail enviado")
# # import os
# # import pathlib
# # import smtplib

# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # from string import Template

# # from dotenv import load_dotenv

# # load_dotenv()

# # # caminho HTML

# # CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula179a.html'

# # # Dados do remetente e destinatário

# # remetente = os.getenv('FROM_EMAIL', '')
# # destinatario = remetente


# # # Configurações SMTP

# # smtp_server = 'stmp.gmail.com'
# # smtp_port = 587
# # smtp_username = os.getenv('FROM_EMAIL', '')
# # smtp_password = os.getenv('EMAIL_PASSWORD', '')

# # # mensagem de texto

# # with open(CAMINHO_HTML, 'r') as arquivo:
# #     texto_arquivo = arquivo.read()
# #     template = Template(texto_arquivo)
# #     texto_email = template.substitute(nome='Helena')

# # # Transformar nossa mensagem em MIMEMultipart

# # mime_multipart = MIMEMultipart()
# # mime_multipart['from'] = remetente
# # mime_multipart['to'] = destinatario
# # mime_multipart['subject'] = "este a o assumto do email."

# # corpo_email = MIMEText(texto_email, 'html', 'utf-8')
# # mime_multipart.attach(corpo_email)


# # # enviando email
# # with smtplib.SMTP(smtp_server, smtp_port) as server:
# #     server.ehlo()
# #     server.starttls()
# #     server.login(smtp_username, smtp_password)
# #     server.send_message(mime_multipart)
# #     print('E-mail enviado com  sucesso!')


# # Enviando E-mails SMTP com Python


# # load_dotenv()

# # Caminho arquivo HTML
# # CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula179a.html'

# # Dados do remetente e destinatário
# # remetente = os.getenv('FROM_EMAIL', '')
# # destinatario = remetente

# # Configurações SMTP
# # smtp_server = 'smtp.gmail.com'
# # smtp_port = 587
# # smtp_username = os.getenv('FROM_EMAIL', '')
# # smtp_password = os.getenv('EMAIL_PASSWORD', '')

# # Mensagem de texto
# # with open(CAMINHO_HTML, 'r') as arquivo:
# #     texto_arquivo = arquivo.read()
# #     template = Template(texto_arquivo)
# #     texto_email = template.substitute(nome='Helena')

# # Transformar nossa mensagem em MIMEMultipart
# # mime_multipart = MIMEMultipart()
# # mime_multipart['from'] = remetente
# # mime_multipart['to'] = destinatario
# # mime_multipart['subject'] = 'Este é o assunto do e-mail'

# # corpo_email = MIMEText(texto_email, 'html', 'utf-8')
# # mime_multipart.attach(corpo_email)

# # Envia o e-mail
# # with smtplib.SMTP(smtp_server, smtp_port) as server:
# #     server.ehlo()
# #     server.starttls()
# #     server.login(smtp_username, smtp_password)
# #     server.send_message(mime_multipart)
# #     print('E-mail enviado com  sucesso!')
