import requests

api_url = "https://dadosabertos.camara.leg.br/api/v2"

def response_success(data):
  return {
      "success": True,
      "data": data,
      "error": None
  }

def response_error(message):
  return {
      "success": False,
      "data": None,
      "error": message
  }

def is_empty_data(dados):
    if not dados:
        return True

    if not isinstance(dados, list):
      return False

    for item in dados:
        if not isinstance(item, dict):
          return False

        for value in item.values():
          if value is not None:
            return False

    return True

def request_api(url, message_empty):
  try:
    response = requests.get(url)

    if response.status_code == 404:
      return response_error("Deputado não encontrado")

    data = response.json()
    dados = data.get('dados')

    if isinstance(dados, str):
      return response_error(dados)

    if is_empty_data(dados):
      return response_error(message_empty)

    return response_success(dados)

  except Exception as e:
    return response_error(f"Erro ao carregar os dados: {e}")
