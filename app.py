from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dados = None
    if request.method == 'POST':
        username = request.form['username']
        url = f'https://api.github.com/users/{username}'
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
        else:
            dados = {'erro': 'Usuário não encontrado.'}
    return render_template('index.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
