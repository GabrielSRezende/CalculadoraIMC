from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para armazenar histórico de IMCs
historico = []


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    elif 30 <= imc < 34.9:
        categoria = "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        categoria = "Obesidade grau 2"
    else:
        categoria = "Obesidade grau 3"
    return round(imc, 2), categoria


@app.route('/')
def index():
    return render_template('index.html', historico=historico)


@app.route('/calcular', methods=['POST'])
def calcular():
    nome = request.form['nome']
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    imc, categoria = calcular_imc(peso, altura)

    # Adiciona ao histórico
    historico.append({"nome": nome, "peso": peso, "altura": altura, "imc": imc, "categoria": categoria})

    return render_template('index.html', historico=historico)


if __name__ == '__main__':
    app.run(debug=True)
