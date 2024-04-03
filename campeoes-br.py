from pathlib import Path
import scrapy

# Inicialização do Spider
class campeoesSpider(scrapy.Spider):
    name = 'campeoes_BR' # Nome do Spider

    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_campe%C3%B5es_do_Campeonato_Brasileiro_de_Futebol'] # URL que será utilizado o scrapy

    def parse(self, response):
        url = response.request.url
        tabela = response.xpath('//table[contains(@class, "wikitable")]')[1] # Coleta a tabela dos campeões brasileiros
        rows = tabela.xpath('.//tr') # Coleta todas as linhas da tabela
        headers = tabela.xpath('.//th') # Coleta todos os itens na linha
        header_index = 0 # Inicia no header 0
        

        for header in headers:
            header_index += 1

        for row in rows:
            if row.xpath('.//th[2]//text()').get() is not None:
                current_page = row.xpath('.//th/text()').getall() # Define o header da tabela
            ano = row.xpath('.//td[1]//text()').getall() # Coleta todos os anos da tabela
            vencedor = row.xpath('.//td[2]//text()').getall() # Coleta todos os campeões da tabela
            vice = row.xpath('.//td[3]//text()').getall() # Coleta todos os vices da tabela
            bronze = row.xpath('.//td[4]//text()').getall() # Coleta todos os terceiros colocados da tabela

            yield{
                'ano': ano,
                'vencedor': vencedor,
                'vice': vice,
                'bronze': bronze,
            }