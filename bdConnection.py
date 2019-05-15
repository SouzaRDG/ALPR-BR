import pymysql as mysql


base = mysql.connect(host = '127.0.0.1', user='root', password='Senh@123')
# , database='ALPR'

q = 'DROP DATABASE TESTEDBBB'


def criaTable():

    con = base.cursor()
    con.execute(q)


criaTable()