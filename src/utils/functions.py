import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'static', 'data')

# Funções dos deputados
def get_deputados():
  deputados = []

  for arquivo in os.listdir(f'{DATA_PATH}/dados_deputados'):
    if arquivo.startswith('deputado_') and arquivo.endswith('.json'):
      with open(f'{DATA_PATH}/dados_deputados/{arquivo}', 'r', encoding='utf-8') as f:
        deputado = json.load(f)
        deputados.append(deputado)

  return deputados

def get_deputado_by_id(id: int):
  with open(f'{DATA_PATH}/dados_deputados/deputado_{id}.json', 'r', encoding='utf-8') as f:
    deputado = json.load(f)
    
    return deputado

def get_gastos_deputado(deputado_id: int):
  with open(f'{DATA_PATH}/gastos_deputados/gastos_deputado_{deputado_id}.json', 'r', encoding='utf-8') as f:
    gastos_deputados = json.load(f)
    
    return gastos_deputados

def get_votos_deputado(deputado_id):
    with open(f'{DATA_PATH}/votos_deputados/votos_deputado_{deputado_id}.json', 'r', encoding='utf-8') as f:
        votos_deputados = json.load(f)
    
    return votos_deputados
