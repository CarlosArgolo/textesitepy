from app import app
from flask import render_template
					
@app.route('/')
@app.route('/index')
def index():
    nome = "Carlos"
    return render_template('index.html',nome=nome)

@app.route('/contatos')
def index():
    ms = "Meu Contato com essa ai"
    return render_template('contatos.html',ms=ms)