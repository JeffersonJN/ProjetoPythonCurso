# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import json
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHA_ARQUIVO = Path(__file__).parent / "aula176d.txt"

locale.setlocale(locale.LC_ALL, '')


def conver_brl(numero: float | int) -> str:
    brl = "R$ " + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2023, 5, 17)

dados = dict(
    nome='Joaão',
    valor=conver_brl(1_234_567),
    data=data.strftime("%d/%m/%Y"),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# print(json.dumps(dados, ensure_ascii=False, indent=2))

texto = """Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. 
Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone 
$telefone.

Atenciosamente,

${empresa}, 
Abraços."""

# template = string.Template(texto)
# print(template.substitute(dados))


class MyTempletes(string.Template):
    delimiter = "%"


with open(CAMINHA_ARQUIVO, 'r')as arquivo:
    texto = arquivo.read()
    template = MyTempletes(texto)
    print(template.substitute(dados,))
