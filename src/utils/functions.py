import plotly.graph_objects as go
import plotly.io as pio
from utils.functions_db import *
import time

# Funções dos deputados
def get_deputados():
    deputados = fetch_data("SELECT id, nomeEleitoral, urlFoto, siglaPartido, siglaUf FROM deputados")
    return deputados

def get_deputado_by_id(id: int):
    deputado = fetch_data("SELECT id, nomeEleitoral, urlFoto, siglaPartido, siglaUf FROM deputados WHERE id = %s", (id,))
    return deputado[0]

def get_gastos_deputado(deputado_id: int):
    query = "SELECT tipoDespesa, valorDocumento, dataDocumento FROM gastos WHERE deputado_id = %s"

    gastos = fetch_data(query, (deputado_id,))
    return gastos

def get_votos_deputado(deputado_id):
    query = """SELECT tipoVoto, descricao_detalhada, titulo, dataHora, aprovacao FROM votos WHERE deputado_id = %s"""

    votos = fetch_data(query, (deputado_id,))
    return votos

# Funções dos gráficos
def get_grafico_gasto(id_deputado, tipo = None, mes = None, ano = None):
    start = time.time()

    query = """SELECT tipoDespesa, SUM(valorDocumento) as total FROM gastos
    WHERE deputado_id = %s"""
    
    parametros = [id_deputado]
    
    if tipo:
        query += " and tipoDespesa like %s"
        parametros.append(f"%{tipo}%")
    if mes:
        query += " and mes = %s"
        parametros.append(mes)
    if ano:
        query += " and ano = %s"
        parametros.append(ano)
    
    query += """ GROUP BY tipoDespesa 
    ORDER BY total ASC""" 

    gastos = fetch_data(query, parametros)

    print(f"MySQL: {time.time() - start:.2f}s")

    start_plot = time.time()

    if not gastos:
        return None

    categorias = [g['tipoDespesa'] for g in gastos]
    valores = [float(g['total']) for g in gastos]

    deputado = get_deputado_by_id(id_deputado)

    fig = go.Figure(data=[
        go.Bar(
            y=categorias,
            x=valores,
            orientation='h',
            marker_color='#0047ab'
        )
    ])

    fig.update_layout(
        title=f"Resumo de Despesas - {deputado['nomeEleitoral']}",
        xaxis=dict(
            title="Valor (R$)",
            dtick=100000,
            tickformat=".2f"
        ),
        yaxis_title="Tipo de Despesa",
        height=500,
        width=900
    )

    print(f"PlotLy: {time.time() - start_plot:.2f}s")

    return pio.to_json(fig)

def get_deputado_presenca(deputado_id):
    query = """SELECT total_presencas, total_eventos FROM presencas WHERE deputado_id = %s"""

    presencas = fetch_data(query, (deputado_id,))
    return presencas
