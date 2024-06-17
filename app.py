from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def calcular_pb(N, A):
    pb = (A ** N) / factorial(N) / sum([(A ** n) / factorial(n) for n in range(N + 1)])
    return pb

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def criar_tabela(num_linhas, taxa_chamadas):
    tabela = []
    for n in range(1, num_linhas + 1):
        linha = []
        for a in taxa_chamadas:
            pb = calcular_pb(n, a)
            linha.append(round(pb, 4))
        tabela.append(linha)
    return tabela

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_linhas = int(request.form['num_linhas'])
        inicio_taxa = float(request.form['inicio_taxa'])
        fim_taxa = float(request.form['fim_taxa'])
        passo_taxa = float(request.form['passo_taxa'])
        
        taxa_chamadas = [round(x, 1) for x in list(np.arange(inicio_taxa, fim_taxa + passo_taxa, passo_taxa))]
        tabela = criar_tabela(num_linhas, taxa_chamadas)
        
        return render_template('index.html', tabela=tabela, taxa_chamadas=taxa_chamadas, enumerate=enumerate)
    
    return render_template('index.html', tabela=None, taxa_chamadas=None, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
