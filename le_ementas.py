#from bs4 import BeautifulSoup
#from bs4.dammit import EncodingDetector
#import requests

from banco_de_dados.sqlite import projeto_de_lei_bd
from config import app
from bib import le_pagina

meu_app = app.Parametros()

pls = []

for projeto_de_lei in meu_app.url_projetos:

    pl = []
    total_por_legislatura = 0
    inicio = 1
    fim = 999
    maximo_contador = 999
    primeira_vez = True

    while (pl != []) or (primeira_vez):
        url_notes = f'{meu_app.url_site}{projeto_de_lei}&Start={inicio}&Count={fim}'
        print(url_notes)

        pl = le_pagina.le_projeto_de_lei(url_notes)

        if pl:
            pls = pls + pl
            total_por_legislatura += len(pl)

        primeira_vez = False
        inicio = fim + 1
        fim = fim + maximo_contador

    print(f"Total para {projeto_de_lei}: {total_por_legislatura}\n")


#print(" *********************************************************************** ")
bd = projeto_de_lei_bd()
bd.ApagaTudo()

for a in pls:
    #print(f"{a.numero}\n{a.ementa}\n{a.comissoes}\n{a.autor}\n{a.data_publicacao}\n")
    bd.Insere(a.numero, a.ementa, a.data_publicacao, a.autor, a.comissoes)
    #print("")

print(f"Total: {len(pls)}")
print("* FIM *")

