import json
from datetime import date

with open('campeoes-br.json', 'r', encoding='utf-8') as f:
    tabelas = json.load(f)

today = date.today()
consulta = int(input('Informe o ano que deseja consultar:(YYYY) '))


while consulta >= today.year:
    print ("O campeonato não foi concluído ou realizado!")
    print (f"No momento temos o campeonato até o ano de {today.year - 1}.")
    consulta = int(input('Informe o ano que deseja consultar:(YYYY) '))

for ano in tabelas:
    
    if str(consulta) == ano['ano']:
        print (
            f"1° colocado: {ano['vencedor']}\n"
            f"2° colocado: {ano['vice']}\n"
            f"3° colocado: {ano['bronze']}"
            )