from flask import Flask, render_template, request, redirect, url_for
from utils.functions import *

app = Flask(__name__)


@app.route("/")
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
        "UNIÃO",
    ]

    nome = request.args.get("nome")
    estado = request.args.get("siglaUf")
    partido = request.args.get("siglaPartido")
    page = request.args.get("page", 1, type=int)

    if nome or estado or partido:
        deputados = [
            d
            for d in deputados
            if (not nome or nome.lower() in d["nomeEleitoral"].lower())
            and (not estado or d["siglaUf"] == estado)
            and (not partido or d["siglaPartido"] == partido)
        ]

    per_page = 24
    inicio = (page - 1) * per_page
    fim = inicio + per_page

    total = len(deputados)
    total_pages = (total + per_page - 1) // per_page

    cur_deputados = deputados[inicio:fim]

    return render_template(
        "index.html",
        deputados=cur_deputados,
        partidos=partidos,
        page=page,
        total_pages=total_pages,
        nome=nome,
        estado=estado,
        partido=partido,
    )


@app.route("/graficos", methods=["GET", "POST"])
def graficos():
    grafico_1 = None
    grafico_2 = None
    nome1 = None
    nome2 = None

    if request.method == "POST":
        nome1 = request.form.get("nome1")
        nome2 = request.form.get("nome2")

        deputados = get_deputados()

        def find_deputado(nome):
            if not nome:
                return None
            for d in deputados:
                if nome.lower() in d["nomeEleitoral"].lower():
                    return d
            return None

        dep1 = find_deputado(nome1)
        dep2 = find_deputado(nome2)

        if dep1:
            grafico_1 = get_grafico_gasto(dep1["id"])
        if dep2:
            grafico_2 = get_grafico_gasto(dep2["id"])

    return render_template(
        "graficos.html",
        grafico_1=grafico_1,
        grafico_2=grafico_2,
        nome1=nome1,
        nome2=nome2,
    )


@app.route("/deputado/<id_deputado>")
def page_deputado(id_deputado):
    tipo = request.args.get("despesa", default= '').upper()
    mes = request.args.get("mes", type= int)
    ano_gasto = request.args.get("ano_gasto", type= int)
    ano_evento = request.args.get("ano_evento", type=int)
    
    deputado = get_deputado_by_id(id_deputado)
    votos = get_votos_deputado(id_deputado)
    grafico_gastos = get_grafico_gasto(id_deputado, tipo, mes, ano_gasto)
    # print(tipo, mes, ano_gasto)
    grafico_presencas = get_grafico_presenca(id_deputado, ano_evento)

    return render_template("deputado.html", deputado=deputado, votos=votos, grafico_gastos=grafico_gastos, grafico_presencas=grafico_presencas, tipo=tipo, mes=mes, ano_gasto=ano_gasto, ano_evento=ano_evento)

if __name__ == "__main__":
    app.run(debug=True)
