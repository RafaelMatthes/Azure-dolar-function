import logging
import json
import azure.functions as func
from .classes import Dolar

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        dolar = Dolar()
    
        value = dolar.get_value()
    except:
        value = 'None'
            
    if value:
        return func.HttpResponse(
            json.dumps(value)
        )
    else:
        return func.HttpResponse(
            {'error': '400'},
            status_code=100
        )
