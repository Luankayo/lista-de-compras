import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from flask import session
import json


load_dotenv()  # carrega o .env local

app = Flask(__name__)

usuarios = {
    'luan': '1234',
    'maria': 'abcd',
    'joao': '4321'
}


# pega secret key do ambiente (Render) ou do .env local
app.secret_key = os.getenv('SECRET_KEY', 'chave_padrao_temporaria')

# pega se deve rodar em modo debug (True/False)
debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 'yes']

compras = {}

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/adicionar', methods=['POST'])
def adicionar():
    produto = request.form['produto'].strip().title()
    quantidade = int(request.form['quantidade'])
    valor = float(request.form['valor'])
    compras[produto] = {'quantidade': quantidade, 'valor': valor}
    return redirect(url_for('index'))

@app.route('/deletar/<produto>')
def deletar(produto):
    produto = produto.title()
    if produto in compras:
        del compras[produto]
    return redirect(url_for('index'))

@app.route('/editar/<produto>')
def editar(produto):
    produto = produto.title()
    item = compras.get(produto, {'quantidade': 0, 'valor': 0})
    return render_template('editar.html', produto=produto, quantidade=item['quantidade'], valor=item['valor'])

@app.route('/atualizar', methods=['POST'])
def atualizar():
    produto_antigo = request.form['produto_antigo'].strip().title()
    produto_novo = request.form['produto'].strip().title()
    quantidade = int(request.form['quantidade'])
    valor = float(request.form['valor'])

    if produto_antigo != produto_novo and produto_antigo in compras:
        del compras[produto_antigo]

    compras[produto_novo] = {'quantidade': quantidade, 'valor': valor}
    return redirect(url_for('index'))

def carregar_historico(usuario):
    try:
        with open('lista_compras.json', 'r') as f:
            dados = json.load(f)
        return dados.get(usuario, [])
    except:
        return []

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Usuário ou senha inválidos.'

    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    usuario = session['username']
    historico = carregar_historico(usuario)
    total = sum(item['quantidade'] * item['valor'] for item in compras.values())
    return render_template('index.html', usuario=usuario, compras=compras, total=total, historico=historico)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=debug_mode, host='0.0.0.0')
