from utils.request_utils import *

# Funções dos deputados
def get_deputados():
  return request_api(api_url, "Erro ao carregar os dados")

def get_deputado_by_id(id: int):
  url = f"{api_url}/{id}"

  return request_api(url, "Deputado inexistente")

def get_despesas_by_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/despesas"

  return request_api(url, "Deputado inexistente ou sem histórico de despesas")

def get_discursos_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/discursos"

  return request_api(url, "Deputado inexistente ou sem histórico de discursos")

def get_eventos_by_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/eventos"

  return request_api(url, "Deputado inexistente ou sem histórico de eventos")

def get_frentes_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/frentes"

  return request_api(url, "Deputado inexistente ou sem frentes adotadas")

def get_historico_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/historico"

  return request_api(url, "Deputado inexistente ou sem histórico de legislaturas")

def get_mandatos_externos_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/mandatosExternos"

  return request_api(url, "Deputado inexistente ou sem mandatos externos")

def get_ocupacoes_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/ocupacoes"

  return request_api(url, "Deputado inexistente ou sem histórico de ocupações passadas")

def get_orgaos_by_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/orgaos"

  return request_api(url, "Deputado inexistente ou não integrado a nenhum órgão")

def get_profissoes_deputado(deputadoId: int):
  url = f"{api_url}/{deputadoId}/profissoes"

  return request_api(url, "Deputado inexistente ou sem histórico de profissões")