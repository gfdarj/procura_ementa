import sqlite3
import os
from config import app
from config.app import Parametros


class conexao_sqlite:
    def __init__(self):
        try:
            p = Parametros()
            self._con = sqlite3.connect(p.banco_dados_sqlite)
            #self._con = sqlite3.connect(os.getcwd() + '/' + p.banco_dados_sqlite)
        except sqlite3.Error as ex:
            print(f'ERRO: {ex}')


    def Insere(self, numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link):
        try:
            cursor = self._con.cursor()
            cursor.execute('INSERT INTO projetos_de_lei (numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link) VALUES (?,?,?,?,?,?,?,?)', (numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link))
            self._con.commit()
            print(f'(sql) Registro {numero} inserido')

        except Exception as ex:
            print('ERRO: ' + str(ex) + f" (número: {numero})")


    def Atualiza(self, numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link):
        try:
            cursor = self._con.cursor()
            cursor.execute('UPDATE projetos_de_lei SET ementa = ?, data_publicacao = ?, autor = ?, comissoes = ?, tipo = ?, numero_formatado = ?, link = ? WHERE numero = ?', (ementa, data_publicacao, autor, comissoes, numero, tipo, numero_formatado, link))
            self._con.commit()
            print(f'(sql) Registro {numero} atualizado')

        except Exception as ex:
            print(str(ex) + f" (numero: {numero})")


    def Seleciona(self, numero):
        cursor = self._con.cursor()
        cursor.execute('SELECT numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link FROM projetos_de_lei WHERE numero = ?', (numero,)) # QUANDO É 1 PARAMETRO TEM QUE COLOCAR ESSA MALDITA VIRGULA !
        return cursor.fetchone()


    def Apaga(self, numero):
        cursor = self._con.cursor()
        cursor.execute('DELETE FROM projetos_de_lei WHERE numero = ?', (numero,)) # QUANDO É 1 PARAMETRO TEM QUE COLOCAR ESSA MALDITA VIRGULA !
        print(f'(sql) Registro {numero} excluído')
        return cursor.fetchone()


    def ApagaTudo(self):
        try:
            cursor = self._con.cursor()
            cursor.execute('DELETE FROM projetos_de_lei')
            self._con.commit()
            print('(sql) Todos os registros apagados')

        except Exception as ex:
            print('ERRO: ' + str(ex))

