from sinesp_client import SinespClient
import urllib3

urllib3.disable_warnings()


# Teste rápido para verificar se esta funcionando

# sc = SinespClient()
# result = sc.search('PLA0000')
#
# #  Para teste
# #
# #  Sem roubo ADV4566
# #  Roubado PDX6897
#
# print(result)  # retorna todos os dados
#
# print(result["status_message"])   # retorna apenas o status de roubo


def pesquisaSituacao(placa):
    try:

        sc = SinespClient()
        resultado = sc.search(placa)

        # print(placa)
        # print(resultado['status_message'])
        # print(resultado)

        if resultado.get('return_code') == '1' or resultado.get('return_code') == '3':
            print(f'\nATENÇÃO *-* Placa {placa} inválida *-* \n Possíveis motivos:\n'
                  '1 - Essa placa não se encontra no servidor da SINESP \n*-* ATENÇÃO *-*'
                  'ESSA PLACA PODE SER FALSA!\n'
                  '2 - A placa não foi identificada corretamente\n')

        elif (resultado.get('status_code') == '1'):
            print('\n*-* ATENÇÃO *-*\n'
                  f'O veículo placa {placa} está marcado como roubado/furtado segundo o SINESP\n'
                  f'{resultado.get("model")} {resultado.get("color")} {resultado.get("model_year")}\n'
                  f'{resultado.get("plate")} - {resultado.get("city")} - {resultado.get("state")}\n'
                  'Fique atento e chame as autoridades competentes\n'
                  'EM HIPOTESE NENHUMA TENTE AGIR POR CONTA PRÓPRIA!\n')

        else:
            print(f'\nVeículo placa {placa} regularizado segundo o SINESP\n'
                  'Fique atento as características do veículo cadastradas no SINESP:\n'
                  f'{resultado.get("model")} {resultado.get("color")} {resultado.get("model_year")}\n'
                  f'{resultado.get("plate")} - {resultado.get("city")} - {resultado.get("state")}\n')

    except:
        print('\n Não foi possível realizar a pesquisa da situação do veículo junto ao SINESP\n'
              'Possíveis Erros:\n'
              '1 - Verifique sua conexão com a internet\n'
              '2 - Confira se não há uma atualização na API\n'
              '3 - O aplicativo da SINESP pode estar fora do ar no momento\n'
              '4 - O servidor bloqueou seu acesso devido a muitos acessos seguidos.\n'
              'Nesse caso, o acesso pode se normalizar após algumas horas \n'
              '(talvez seja necessario limpar o cache)\n')


# pesquisaSituacao('PDX6897')
