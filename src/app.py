from flask import Flask, render_template, request, redirect, url_for
from utils.request_functions import *

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def home():
    res = get_deputados()
    if res['success'] and res['data'] and not res['error']:
        deputados = res['data']
    else:
        deputados = []

    nome = None
    estado = None
    partido = None

    if request.method == 'POST':
        nome = request.form.get('nome') or None
        estado = request.form.get('siglaUf') or None
        partido = request.form.get('siglaPartido') or None

        if nome or estado or partido:
            deputados = [
                d for d in deputados
                if (not nome or nome.lower() in d['nome'].lower())
                and (not estado or d['siglaUf'] == estado)
                and (not partido or d['siglaPartido'] == partido)
            ]

    page = request.form.get('page', 1, type=int)
    per_page = 24

    inicio = (page - 1) * per_page # Calculo do inicio dos deputados que serão exibidos
    fim = inicio + per_page # Calculo do fim dos deputados que serão exibidos

    total = len(deputados)
    total_pages = (total + per_page - 1) // per_page

    cur_deputados = deputados[inicio:fim]

    return render_template(
        'index.html',
        deputados=cur_deputados,
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

    return render_template('deputado.html', deputado=deputado)

if __name__ == '__main__':
    app.run(debug=True)