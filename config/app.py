import json
import os

class Parametros:
    def __init__(self):
        with open(os.getcwd() + '/configuracao.json', encoding='utf-8') as configuracao_json:
            arquivo_conf = json.load(configuracao_json)

        self._date_format_en = arquivo_conf['date_format_en']
        self._date_format_br = arquivo_conf['date_format_br']
        self._url_site = arquivo_conf['url_site']
        self._url_projetos = arquivo_conf['url_projetos']
        self._banco_dados_msacess = arquivo_conf['banco_dados_msacess']
        self._banco_dados_sqlite = arquivo_conf['banco_dados_sqlite']


    @property
    def date_format_en(self):
        return str(self._date_format_en)

    @property
    def date_format_br(self):
        return str(self._date_format_br)

    @property
    def url_site(self):
        return str(self._url_site)

    @property
    def url_projetos(self):
        return self._url_projetos

    @property
    def banco_dados_sqlite(self):
        return str(self._banco_dados_sqlite)

    @property
    def banco_dados_msacess(self):
        return str(self._banco_dados_msacess)

