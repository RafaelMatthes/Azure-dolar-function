import requests
import json
import xmltodict
from datetime import date

class Dolar(object):

    def __init__(self):
        self._url = 'https://www3.bcb.gov.br/bc_moeda/rest/converter/1/1/220/790/'
        self.data_atual = date.today()        

    def get_value(self):
        header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        page = requests.get(f'{self._url}{self.data_atual.year}-{self.data_atual.month}-{self.data_atual.day}', headers=header)
        
        try:
            if page.status_code == 200:
                valor = json.loads(json.dumps(xmltodict.parse(page.content)))

                context = {}
                context['dolar'] = "%.4f" %float(valor['valor-convertido'])

                return context
        except:
            return 'erro'
                

        return {
            'dolar': None, 
        }

   