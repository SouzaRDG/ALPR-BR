from sinesp_client import SinespClient
import urllib3
urllib3.disable_warnings()


sc = SinespClient()
result = sc.search('PDX6897')

#  Para teste
#
#  Sem roubo ADV4566
#  Roubado PDX6897

print(result)

print(result["status_message"])
