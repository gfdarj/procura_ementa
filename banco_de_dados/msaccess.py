import pyodbc
from config.app import Parametros
import os


class conexao_msaccess:

    def __init__(self):
        p = Parametros()

        # connection_string = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=path/to/your/database.mdb'
        self.connection_string = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + str(os.getcwd()) + '/' + p.banco_dados_msaccess

        try:
            self._con = pyodbc.connect(self.connection_string)
            #cursor = cnxn.cursor()
            print("Successfully connected to the database.")

        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '01000':
                print("Error: The specified DSN contains an architecture mismatch between the Driver and Application")
            else:
                print(f"Error connecting to database: {ex}")
            #exit()


    def Insere(self, numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado):
        try:
            cursor = self._con.cursor()
            cursor.execute('INSERT INTO projetos_de_lei (numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado) VALUES (?,?,?,?,?,?,?)', (numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado))
            self._con.commit()
            print(f'(sql) Registro {numero} inserido')

        except Exception as ex:
            print('ERRO: ' + str(ex) + f" (número: {numero})")


    def Atualiza(self, numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado):
        try:
            cursor = self._con.cursor()
            cursor.execute('UPDATE projetos_de_lei SET ementa = ?, data_publicacao = ?, autor = ?, comissoes = ?, tipo = ?, numero_formatado = ? WHERE numero = ?', (ementa, data_publicacao, autor, comissoes, numero, tipo, numero_formatado))
            self._con.commit()
            print(f'(sql) Registro {numero} atualizado')

        except Exception as ex:
            print(str(ex) + f" (numero: {numero})")


    def Seleciona(self, numero):
        cursor = self._con.cursor()
        cursor.execute('SELECT numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado FROM projetos_de_lei WHERE numero = ?', (numero,)) # QUANDO É 1 PARAMETRO TEM QUE COLOCAR ESSA MALDITA VIRGULA !
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

