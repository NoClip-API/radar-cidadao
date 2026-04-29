import json

def get_votos_deputado(deputado_id):
    with open(f'src/static/votos_deputados/votos_deputado_{deputado_id}.json', 'r', encoding='utf-8') as f:
        votos_deputados = json.load(f)
    
    return votos_deputados
