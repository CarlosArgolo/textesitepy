from app import app
from flask import render_template
					
@app.route('/')
@app.route('/index')
def index():
    titulo = 'Home'
    nome = "Carlos"
    arqCss ='style/principal.css'
    return render_template('index.html',nome=nome, titulo=titulo, arqCss=arqCss)

@app.route('/contatos')
def contatos():
    titulo = 'Contatos'
    ms = "Meu Contato com essa ai"
    arqCss ='style/principal.css'
    return render_template('contatos.html',ms=ms, titulo=titulo, arqCss=arqCss)