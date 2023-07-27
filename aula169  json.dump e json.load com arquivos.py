# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula169_b.json'

CAMINHO_ABSOLUTO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)
filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}
# print(filme)

with open(CAMINHO_ABSOLUTO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO, 'r') as arquivo:
    filme_json = json.load(arquivo)
    print(filme_json)

# print(os.path.dirname(__file__), NOME_ARQUIVO)
