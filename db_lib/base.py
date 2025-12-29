from abc import ABC, abstractmethod

#
# COM A AJUDA DO CHATO-GPT ESTOU MONTANDO ESTA CLASSE BASE PARA QUE OUTRAS CLASSES UTILIZEM ELA
# MUDANDO APENAS A CONEXAO COM O BANCO DE DADOS
#

class DatabaseBase(ABC):
    def __init__(self):
        self._con = None

    @abstractmethod
    def conectar(self):
        pass

    def executar(self, sql, params=None, commit=False):
        cursor = self._con.cursor()
        cursor.execute(sql, params or ())
        if commit:
            self._con.commit()
        return cursor

    def fetchone(self, sql, params=None):
        return self.executar(sql, params).fetchone()

    def fetchall(self, sql, params=None):
        return self.executar(sql, params).fetchall()

    def execute_commit(self, sql, params=None):
        self.executar(sql, params, commit=True)

    def close(self):
        if self._con:
            self._con.close()

