from bs4 import BeautifulSoup
#from bs4.dammit import EncodingDetector
import requests
from classes.projeto_de_lei import projeto_de_lei
from bib import tipo_projeto_de_lei

###################################################################################
# Retorna o conjunto de PL´s lidos na URL
###################################################################################
def obtem_dados_url(url_projeto_de_lei):
    pls = []

    try:
        #print("try")
        r = requests.get(f'{url_projeto_de_lei}')
        #print(f'{url_projeto_de_lei}')
        soup = BeautifulSoup(r.content, 'html.parser')

        tr = soup.find_all("tr")
        #print(f'TR: {len(tr)}')

        linha = 1
        for linha in tr:
            tds = linha.find_all("td")

            pl = projeto_de_lei()
            col = 1

            for td in tds:
                if col == 1:
                    pl.numero = td.get_text()
                    pl.tipo = tipo_projeto_de_lei.mostra(pl.numero)
                    pl.numero_formatado = str(int(pl.numero[6:11])) + "/" + pl.numero[0:4]
                # coluna 2 - vazio
                if col == 3:
                    pl.ementa = td.get_text()
                    sp = pl.ementa.strip().split(f"=>{pl.numero} =>")

                    # Tem bancos que está com espaço depois do "=>"
                    if sp[0].strip() != sp[-1].strip():
                        pl.ementa = sp[0].strip()
                        pl.comissoes = sp[-1].strip()
                    else:
                        sp = pl.ementa.strip().split(f"=> {pl.numero} =>")
                        pl.ementa = sp[0].strip()
                        pl.comissoes = sp[-1].strip()


                if col == 4:
                    pl.data_publicacao = td.get_text()
                if col == 5:
                    pl.autor = td.get_text()

                col = col + 1

            if len(pl.numero) == 11:
                pls.append(pl)

    finally:
        return pls
