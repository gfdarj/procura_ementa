import pyodbc
from config.app import Parametros
from db_lib.base import DatabaseBase

class AccessDB(DatabaseBase):

    def conectar(self):
        p = Parametros()
        conn_str = (
            'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            f'DBQ={p.banco_dados_msaccess}'
        )
        self._con = pyodbc.connect(conn_str)
