import json
import plotly.graph_objects as go
import plotly.io as pio
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

  deputados.sort(key=lambda x: x['ultimoStatus']['nome'].lower())

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

# Funções dos gráficos
def get_grafico_gasto(id_deputado):
  gastos = get_gastos_deputado(id_deputado)
  resumo = gastos.get('resumo_despesas', {})

  sorted_resumo = sorted(resumo.items(), key=lambda x: x[1], reverse=False)
  # print(sorted_resumo)
  categorias = [x[0] for x in sorted_resumo]
  valores = [x[1] for x in sorted_resumo]

  fig = go.Figure(data=[
      go.Bar(
          y=categorias,
          x=valores,
          orientation='h',
          marker_color='#0047ab'
      )
  ])

  fig.update_layout(
      title=f"Resumo de Despesas - {gastos['nome']}",
      xaxis=dict(
          title="Valor (R$)",
          dtick=100000,
          tickformat=".2f"
      ),
      yaxis_title="Tipo de Despesa",
      height=500,
      width=900
  )

  return pio.to_json(fig)


def get_deputado_presenca(id_deputado):
    try:
        with open(f'{DATA_PATH}/presenca_deputados/deputado_{id_deputado}.json', 'r', encoding='utf-8') as p:
            presenca = json.load(p)

        presencas, eventos =  presenca.get('total_presencas', 0), presenca.get('total_eventos', 0)
        return presencas, eventos

    except FileNotFoundError:
        return 0, 0
