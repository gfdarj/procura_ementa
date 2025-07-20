from config import app
from bib import le_pagina


def obtem_lista():
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

            pl = le_pagina.obtem_dados_url(url_notes)

            #print(pl)

            if pl:
                pls = pls + pl
                total_por_legislatura += len(pl)

            primeira_vez = False
            inicio = fim + 1
            fim = fim + maximo_contador

    print(f"Total para {projeto_de_lei}: {total_por_legislatura}\n")

    return pls
