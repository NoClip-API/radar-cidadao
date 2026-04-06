from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/graficos')
def graficos():
    return render_template('graficos.html')

if __name__ == '__main__':
    app.run(debug=True)