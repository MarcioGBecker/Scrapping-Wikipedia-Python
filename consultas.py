import json

lista = []

with open('campeoes-br.json', 'r', encoding='utf-8') as f:
    tabelas = json.load(f)

ano = tabelas[1]['vencedor'][1]

print (ano)