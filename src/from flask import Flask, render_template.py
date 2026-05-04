from flask import Flask, render_template, request, redirect, url_for
from utils.request_functions import *
from utils.get_votos_deputado import get_votos_deputado

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    res_deputados = get_deputados()
    res_partidos = get_partidos()

    deputados = res_deputados['data'] if res_deputados['success'] and res_deputados['data'] else []
    partidos = res_partidos['data'] if res_partidos['success'] and res_partidos['data'] else []

    nome = request.args.get('nome')
    estado = request.args.get('siglaUf')
    partido = request.args.get('siglaPartido')
    page = request.args.get('page', 1, type=int)

    if nome or estado or partido:
        deputados = [
            d for d in deputados
            if (not nome or nome.lower() in d['nome'].lower())
            and (not estado or d['siglaUf'] == estado)
            and (not partido or d['siglaPartido'] == partido)
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
    res = get_deputado_by_id(id_deputado)
    deputado = res['data'] if res['success'] else res['error']

    votos = get_votos_deputado(id_deputado)

    return render_template('deputado.html', deputado=deputado, votos=votos)

if __name__ == '__main__':
    app.run(debug=True)