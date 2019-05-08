import pymssql

def conectar ():

    con = pymssql.connect(host = 'localhost', user = 'SA', password = 'Senh@123')
    connect = con.cursor()

conectar()