import pymysql as mysql
import sinesp


base = mysql.connect(host = '127.0.0.1', user='root', password='Senh@123', database='ALPR')

# def criaTable():
#
#     con = base.cursor()
#     con.execute("query")

# criaTable()

def pesquisaProprietario(cpf, placa):

    con = base.cursor()
    con.execute('SELECT * FROM PESSOAS where CPF = %s', (cpf))

    try:
        resultado = con.fetchone()
        print(f"Proprietario -> {resultado[0]} \n                CPF:{resultado[1]} RG:{resultado[2]}\n")
    except:
        print("\nNão possivel encontrar o proprietario, apesar do veiculo estar cadastrado\n"
              "chame o suporte para verificar possíveis erros no banco de dados...\n"
              "Verificando a placa no servidor da SINESP...")

        sinesp.pesquisaSituacao(placa)

# pesquisaProprietario()


def pesquisaPlaca(placa):

    con = base.cursor()
    con.execute('SELECT * FROM VEICULOS WHERE PLACA = %s', (placa))

    try:
        resultado = con.fetchone()
        print(f'\nVeiculo ->      {resultado[2]} {resultado[1]} {resultado[3]}\n'
              f'                Placa: {resultado[0]} ')
        pesquisaProprietario(resultado[5], resultado[0])

        # pesquisaProprietario(resultado[5], resultado[0])
        # abre cancela

    except:
        print(f'\nA placa {placa} do veículo não foi encontrada no banco de dados.\n'
              'Verificando a placa no servidor da SINESP...')

        sinesp.pesquisaSituacao(placa)

# pesquisaPlaca('GJA5809')