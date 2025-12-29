import sqlite3
from config.app import Parametros
from db_lib.base import DatabaseBase


class SQLiteDB(DatabaseBase):

    def conectar(self):
        p = Parametros()
        self._con = sqlite3.connect(p.banco_dados_sqlite)

