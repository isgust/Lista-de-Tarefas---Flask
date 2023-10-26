from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
listaItens = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        item = data.get('item')

        if item is not None:
            tarefa = {"Item": item, "concluido": False}
            listaItens.append(tarefa)

    # Adicione a enumeração das tarefas no código Python
    listaEnumerada = list(enumerate(listaItens))

    return render_template('index.html', listaEnumerada=listaEnumerada)

@app.route('/marcarConcluida/<int:index>', methods=['POST'])
def marcar_concluida(index):
    if index < len(listaItens):
        listaItens[index]['concluido'] = True
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
