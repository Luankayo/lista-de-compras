import fdb

def conectar():
    con = fdb.connect(
        dsn='localhost:C:/Sistemas/GAFitness/Banco/BANCO.FDB',
        user='SYSDBA',
        password='masterkey',
        charset='UTF8'
    )
    return con
