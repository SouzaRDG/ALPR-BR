from sinesp_client import SinespClient
import urllib3
urllib3.disable_warnings()

# # Teste
#
# sc = SinespClient()
# result = sc.search('PDX6897')
#
# #  Para teste
# #
# #  Sem roubo ADV4566
# #  Roubado PDX6897
#
# print(result)
#
# print(result["status_message"])



##############                TESTAR (SINESP ESTA FORA DO AR NO MOMENTO)

def pesquisaSituacao(placa):

    try:

        sc = SinespClient()
        resultado = sc.search(placa)
        print(resultado['status_message'])
        print(resultado)

        if(resultado['return_code'] == 1):
            print('Placa inválida')
        elif(resultado['status_code'] == 1):
            print('*-* ATENÇÃO *-*\n\n'
                'O veículo está marcado como roubado/furtado segundo o SINESP\n'
                'Fique atento e chame as autoridades competentes')
        else:
            print('Veículo regularizado segundo o SINESP\n'
                  'Fique atento as características do veículo\n'
                  'DADODADODADODADO AAAAAAAAAADICIONAR DPS CARACTERISTICAS DO VEICULO do servidor SINESP')

    except:

        print('Não foi possível realizar a pesquisa da situação do veículo junto ao SINESP\n'
              'Possíveis Erros:\n'
              'Verifique sua conexão com a internet\n'
              'Confira se não há uma atualização na API\n'
              'O aplicativo da SINESP pode estar fora do ar no momento')

pesquisaSituacao('pdx6897')