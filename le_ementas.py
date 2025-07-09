from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
from config import app

meu_app = app.Parametros()

_formato_br = meu_app.date_format_br
_formato_en = meu_app.date_format_en

for projeto_de_lei in meu_app.url_projetos:
    r = requests.get(f'{meu_app.url_site}{projeto_de_lei}')
    soup = BeautifulSoup(r.content, 'html.parser')

    tr = soup.find_all("tr")

    for linha in tr:
        print("-- nova linha --")

        print(linha)
        tds = linha.find_all("td")


        conta = 1
        for td in tds:
            #soup_td = BeautifulSoup(td, 'html.parser')
            print(f"------------- COLUNAS {conta}")
            print(td.get_text())
            conta = conta + 1

        print(" ============================= \n\n")