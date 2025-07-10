from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
from config import app
from banco_de_dados import sqlite

meu_app = app.Parametros()

pls = []

for projeto_de_lei in meu_app.url_projetos:
    r = requests.get(f'{meu_app.url_site}{projeto_de_lei}')
    soup = BeautifulSoup(r.content, 'html.parser')

    tr = soup.find_all("tr")

    for linha in tr:
        tds = linha.find_all("td")

        pl = sqlite.projeto_de_lei()
        col = 1

        for td in tds:
            if col == 1:
                pl.numero = td.get_text()
            # coluna 2 - vazio
            if col == 3:
                pl.ementa = td.get_text()
            if col == 4:
                pl.data_publicacao = td.get_text()
            if col == 5:
                pl.autor = td.get_text()

            col = col + 1

        #print(" ============================= \n\n")
        pls.append(pl)

print(" *********************************************************************** ")
print(" *********************************************************************** ")
for a in pls:
    print(f"{a.numero}\n{a.ementa}\n{a.autor}\n{a.data_publicacao}\n")
