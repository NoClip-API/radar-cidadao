from utils.request_utils import *
import json
import os

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
