from flask import Flask, render_template, request, redirect, url_for
from utils.functions import *

app = Flask(__name__)

@app.route('/')
def home():
    deputados = get_deputados()
    partidos = [
        "AVANTE",
        "CIDADANIA",
        "MISSÃO",
        "NOVO",
        "PCdoB",
        "PDT",
        "PL",
        "PODE",
        "PP",
        "PRD",
        "PSB",
        "PSD",
        "PSDB",
        "PSOL",
        "PT",
        "PV",
        "REDE",
        "REPUBLICANOS",
        "SOLIDARIEDADE",
        "UNIÃO"
    ]

    nome = request.args.get('nome')
    estado = request.args.get('siglaUf')
    partido = request.args.get('siglaPartido')
    page = request.args.get('page', 1, type=int)

    if nome or estado or partido:
        deputados = [
            d for d in deputados
            if (not nome or nome.lower() in d['ultimoStatus']['nome'].lower())
            and (not estado or d['ultimoStatus']['siglaUf'] == estado)
            and (not partido or d['ultimoStatus']['siglaPartido'] == partido)
        ]

    per_page = 24
    inicio = (page - 1) * per_page
    fim = inicio + per_page

    total = len(deputados)
    total_pages = (total + per_page - 1) // per_page

    cur_deputados = deputados[inicio:fim]

    return render_template(
        'index.html',
        deputados=cur_deputados,
        partidos=partidos,
        page=page,
        total_pages=total_pages,
        nome=nome,
        estado=estado,
        partido=partido
)
@app.route('/graficos')
def graficos():
    return render_template('graficos.html')

@app.route('/deputado/<id_deputado>')
def page_deputado(id_deputado):
    deputado = get_deputado_by_id(id_deputado)
    votos = get_votos_deputado(id_deputado)
    grafico_gastos = get_grafico(id_deputado)
    presenca, eventos = get_deputado_presenca(id_deputado)

    return render_template('deputado.html', deputado=deputado, votos=votos, grafico_gastos=grafico_gastos, presenca=presenca, eventos=eventos)

if __name__ == '__main__':
    app.run(debug=True)
