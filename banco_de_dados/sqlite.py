import sqlite3
import os


class projeto_de_lei_bd:
    def __init__(self):
        self._con = sqlite3.connect(os.getcwd() + '/projetos_de_lei.db')


    def Insere(self, numero, ementa, data_publicacao, autor, comissoes, tipo):
        try:
            cursor = self._con.cursor()
            cursor.execute('INSERT INTO projetos_de_lei (numero, ementa, data_publicacao, autor, comissoes, tipo) VALUES (?,?,?,?,?,?)', (numero, ementa, data_publicacao, autor, comissoes, tipo))
            self._con.commit()
            print(f'(sql) Registro {numero} inserido')

        except Exception as ex:
            print('ERRO: ' + str(ex) + f" (número: {numero})")


    def Atualiza(self, numero, ementa, data_publicacao, autor, comissoes, tipo):
        try:
            cursor = self._con.cursor()
            cursor.execute('UPDATE projetos_de_lei SET ementa = ?, data_publicacao = ?, autor = ?, comissoes = ?, tipo = ? WHERE numero = ?', (ementa, data_publicacao, autor, comissoes, numero, tipo))
            self._con.commit()
            print(f'(sql) Registro {numero} atualizado')

        except Exception as ex:
            print(str(ex) + f" (numero: {numero})")


    def Seleciona(self, numero):
        cursor = self._con.cursor()
        cursor.execute('SELECT numero, ementa, data_publicacao, autor, comissoes, tipo FROM projetos_de_lei WHERE numero = ?', (numero,)) # QUANDO É 1 PARAMETRO TEM QUE COLOCAR ESSA MALDITA VIRGULA !
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

