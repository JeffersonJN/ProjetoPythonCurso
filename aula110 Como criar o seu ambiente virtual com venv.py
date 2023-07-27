# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
#antes
#Políticas de execução do PowerShell
# sabendo o que vai ser executado no windons "Set-ExecutionPolicy -ExecutionPolicy Undefined -force"
"""

https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3

Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope LocalMachine
Set-ExecutionPolicy AllSigned -force

"""

# Como criar ambientes virtuais
# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv

# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv
#
# Ativando e desativando meu ambiente virtual
# Windows: .\venv\Scripts\activate
# Linux e Mac: source venv/bin/activate
# Desativar: deactivate
#"""
# gcm python
# 
# 
# """
# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv
#
# Ativando e desativando meu ambiente virtual
# Windows: .\venv\Scripts\activate
# Linux e Mac: source venv/bin/activate
# Desativar: deactivate

# Linux e Mac: source venv/bin/activate
# Desativar: deactivate
#
# pip - instalando pacotes e bibliotecas
# Instalar última versão:
# pip install nome_pacote
# Instalar versão precisa
# (tem outras formas também não mencionadas)
# pip install nome_pacote==0.0.0
# Desinstalar pacote
# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freezepip 


# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
#
# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
# pip install -r requirements.txt