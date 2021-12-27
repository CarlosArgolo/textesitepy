from app import app
from flask import render_template
					
@app.route('/')
@app.route('/index')
def index():
    titulo = 'Contatos'
    nome = "Carlos"
    return render_template('index.html',nome=nome, titulo=titulo)

@app.route('/contatos')
def contatos():
    titulo = 'Contatos'
    ms = "Meu Contato com essa ai"
    return render_template('contatos.html',ms=ms, titulo=titulo)