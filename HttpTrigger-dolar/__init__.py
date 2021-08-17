import logging
import json
import azure.functions as func
from .classes import Dolar


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        dolar = Dolar()
    
        value = dolar.get_value()#req.params.get('name')
    except:
        value = 'teste'


    if not value:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            value = req_body.get('name')

    if value:
        return func.HttpResponse(
            json.dumps(value)
        )
    else:
        return func.HttpResponse(
            {'error':'500'},
            status_code=200
        )
