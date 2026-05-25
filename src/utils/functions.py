import plotly.graph_objects as go
import plotly.io as pio
from utils.db import *

PESOS_EVENTOS = {
    "Sessão Deliberativa": 1.0,
    "Reunião Deliberativa": 1.0,

    "Audiência Pública e Deliberação": 0.9,
    "Tomada de Depoimento e Deliberação": 0.9,

    "Reunião de Comparecimento de Ministro(a)": 0.85,

    "Reunião de Eleição": 0.8,
    "Reunião de Instalação e Eleição": 0.8,

    "Sessão Preparatória - Eleição": 0.75,
    "Sessão Preparatória - Posse": 0.75,

    "Audiência Pública": 0.7,
    "Tomada de Depoimento": 0.7,
    "Comissão Geral": 0.7,

    "Reunião de Debate": 0.6,
    "Debate": 0.6,

    "Mesa Redonda": 0.55,

    "Painel": 0.5,
    "Reunião": 0.5,

    "Seminário": 0.4,
    "Simpósio": 0.4,
    "Conferência": 0.4,

    "Palestra": 0.35,

    "Evento Técnico": 0.3,
    "Reunião Técnica": 0.3,

    "Diligência": 0.25,

    "Visita Oficial": 0.2,

    "Visita Técnica": 0.15,

    "Homenagem": 0.1,
    "Sessão Não Deliberativa Solene": 0.1,
    "Ato Solene de Instalação": 0.1,
    "Outro Evento": 0.1
}

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
def get_grafico_gasto(deputado_id, tipo=None, mes=None, ano_gasto=None):
    query = """SELECT tipoDespesa, SUM(valorDocumento) as total FROM gastos
    WHERE deputado_id = %s"""
    
    parametros = [deputado_id]
    
    if tipo:
        query += " and tipoDespesa like %s"
        parametros.append(f"%{tipo}%")
    if mes:
        query += " and mes = %s"
        parametros.append(mes)
    if ano_gasto:
        query += " and ano = %s"
        parametros.append(ano_gasto)
    
    query += """ GROUP BY tipoDespesa 
    ORDER BY total ASC""" 

    gastos = fetch_data(query, parametros)
    if not gastos:
        return None

    categorias = [g['tipoDespesa'] for g in gastos]
    valores = [float(g['total']) for g in gastos]

    deputado = get_deputado_by_id(deputado_id)

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

    return pio.to_json(fig)

def get_grafico_presenca(deputado_id, ano_evento=None):
    query = """SELECT e.* FROM eventos e
    inner join presencas p on e.id = p.evento_id
    WHERE p.deputado_id = %s"""

    deputado = get_deputado_by_id(deputado_id)

    parametros = [deputado_id]

    if ano_evento:
        query += " and YEAR(e.dataHoraInicio) = %s"
        parametros.append(ano_evento)

    query += " ORDER BY e.dataHoraInicio DESC"

    presencas = fetch_data(query, parametros)
    if not presencas:
        return None
    
    parametros = [deputado["siglaPartido"]]
    
    query_partido = """
        SELECT d.id, d.nomeEleitoral, SUM(
            CASE
                WHEN e.descricaoTipo IN ('Sessão Deliberativa', 'Reunião Deliberativa') THEN 1
                WHEN e.descricaoTipo IN ('Audiência Pública e Deliberação', 'Tomada de Depoimento e Deliberação') THEN 0.9
                WHEN e.descricaoTipo = 'Reunião de Comparecimento de Ministro(a)' THEN 0.85
                WHEN e.descricaoTipo IN ('Reunião de Eleição', 'Reunião de Instalação e Eleição') THEN 0.8
                WHEN e.descricaoTipo IN ('Sessão Preparatória - Eleição', 'Sessão Preparatória - Posse') THEN 0.75
                WHEN e.descricaoTipo IN ('Audiência Pública', 'Tomada de Depoimento', 'Comissão Geral') THEN 0.7
                WHEN e.descricaoTipo IN ('Reunião de Debate', 'Debate') THEN 0.6
                WHEN e.descricaoTipo = 'Mesa Redonda' THEN 0.55
                WHEN e.descricaoTipo IN ('Painel', 'Reunião') THEN 0.5
                WHEN e.descricaoTipo IN ('Seminário', 'Simpósio', 'Conferência') THEN 0.4
                WHEN e.descricaoTipo = 'Palestra' THEN 0.35
                WHEN e.descricaoTipo IN ('Evento Técnico', 'Reunião Técnica') THEN 0.3
                WHEN e.descricaoTipo = 'Diligência' THEN 0.25
                WHEN e.descricaoTipo = 'Visita Oficial' THEN 0.2
                WHEN e.descricaoTipo = 'Visita Técnica' THEN 0.15
                ELSE 0.1
            END
        ) AS indice FROM deputados d
        INNER JOIN presencas p ON d.id = p.deputado_id
        INNER JOIN eventos e ON e.id = p.evento_id
        WHERE d.siglaPartido = %s
    """

    if ano_evento:
        query_partido += " AND YEAR(e.dataHoraInicio) = %s"
        parametros.append(ano_evento)

    query_partido += " GROUP BY d.id, d.nomeEleitoral ORDER BY indice DESC;"

    indices_deputados_partido = fetch_data(query_partido, parametros)
    indice_deputado = 0
    indice_partido = 0

    for i in indices_deputados_partido:
        indice_partido += i['indice']
    indice_partido /= len(indices_deputados_partido)
    
    for presenca in presencas:
        indice_deputado += PESOS_EVENTOS[presenca['descricaoTipo']]

    fig = go.Figure(data=[
        go.Bar(
            y=[indice_deputado, indice_partido], # Valor do Índice
            x=[deputado["nomeEleitoral"], deputado["siglaPartido"]], # Entidade
            orientation="v",
            marker_color="#0047ab"
        )
    ])

    fig.update_layout(
        title=f"Comparação de presenças - {deputado['nomeEleitoral']} x {deputado['siglaPartido']}",
        yaxis=dict(
            title="Índice",
            dtick=10 if ano_evento else 100,
            tickformat=".2f"
        ),
        height=500,
        width=900
    )

    return pio.to_json(fig)