from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

compras = {}

@app.route('/')
def index():
    total = sum(item['quantidade'] * item['valor'] for item in compras.values())
    return render_template('index.html', compras=compras, total=total)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
