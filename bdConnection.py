import pymysql as mysql


base = mysql.connect(host = '127.0.0.1', user='root', password='Senh@123', database='ALPR')
# , database='ALPR'


# def criaTable():
#
#     con = base.cursor()
#     con.execute("query")

# criaTable()

def pesquisaProprietario(cpf):

    con = base.cursor()
    con.execute('SELECT * FROM PESSOAS where CPF = %s', (cpf))

    try:
        resultado = con.fetchone()
        print(f"Proprietário -> {resultado[0]} \n                CPF:{resultado[1]} RG:{resultado[2]}")
    except:
        print("deu ruim")

# pesquisaProprietario()


def pesquisaPlaca(placa):

    con = base.cursor()
    con.execute('SELECT * FROM VEICULOS WHERE PLACA = %s', (placa))

    try:
        resultado = con.fetchone()
        print(f'Veiculo ->      {resultado[2]} {resultado[1]} {resultado[3]}\n                Placa: {resultado[0]} ')
        pesquisaProprietario(resultado[5])

    except:
        print('deu ruim2')

# pesquisaPlaca('GJA5809')