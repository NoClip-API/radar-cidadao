from utils.request_utils import request_api

def get_partidos():
    url = "https://dadosabertos.camara.leg.br/api/v2/partidos?itens=100&ordem=ASC&ordenarPor=sigla"
    return request_api(url, "Erro ao carregar os partidos")
