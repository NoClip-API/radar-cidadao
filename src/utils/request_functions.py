from utils.request_utils import *
from concurrent.futures import ThreadPoolExecutor, as_completed

cache_votos = {}

# Funções dos deputados
def get_deputados():
  return request_api(f"{api_url}/deputados", "Erro ao carregar os dados")

def get_deputado_by_id(id: int):
  url = f"{api_url}/deputados/{id}"

  return request_api(url, "Deputado inexistente")

def get_despesas_by_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/despesas"

  return request_api(url, "Deputado inexistente ou sem histórico de despesas")

def get_discursos_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/discursos"

  return request_api(url, "Deputado inexistente ou sem histórico de discursos")

def get_eventos_by_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/eventos"

  return request_api(url, "Deputado inexistente ou sem histórico de eventos")

def get_partidos():
  url = f"{api_url}/partidos?itens=100&ordem=ASC&ordenarPor=sigla"
  
  return request_api(url, "Erro ao carregar os partidos")
  
def get_frentes_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/frentes"

  return request_api(url, "Deputado inexistente ou sem frentes adotadas")

def get_historico_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/historico"

  return request_api(url, "Deputado inexistente ou sem histórico de legislaturas")

def get_mandatos_externos_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/mandatosExternos"

  return request_api(url, "Deputado inexistente ou sem mandatos externos")

def get_ocupacoes_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/ocupacoes"

  return request_api(url, "Deputado inexistente ou sem histórico de ocupações passadas")

def get_orgaos_by_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/orgaos"

  return request_api(url, "Deputado inexistente ou não integrado a nenhum órgão")

def get_profissoes_deputado(deputadoId: int):
  url = f"{api_url}/deputados/{deputadoId}/profissoes"

  return request_api(url, "Deputado inexistente ou sem histórico de profissões")

def get_votos_votacao(v):
  url = f"{api_url}/votacoes/{v['id']}/votos"
  votos = request_api(url, "Votação inexistente ou sem histórico de votos")

  return v, votos

def get_votos_por_deputado(deputado_id):
  deputado_id = int(deputado_id)

  if deputado_id in cache_votos:
    return cache_votos[deputado_id]

  url = f"{api_url}/votacoes?dataInicio=2024-01-01"
  votacoes = request_api(url, "Erro")
  votos_deputado = []

  if votacoes['success']:
    with ThreadPoolExecutor(max_workers=50) as executor:
      futures = [
        executor.submit(get_votos_votacao, v)
        for v in votacoes['data']
      ]

      for future in as_completed(futures):
        v, votos = future.result()
        if votos['success']:
          for data_voto in votos['data']:
            if data_voto['deputado_']['id'] == deputado_id:
              votos_deputado.append({
                'dados_voto': data_voto,
                'informacoes': {
                  'descricao': v['descricao'],
                  'dataHora': v['dataHoraRegistro'],
                  'aprovacao': v['aprovacao']
                }
              })
  cache_votos[deputado_id] = votos_deputado
  return votos_deputado