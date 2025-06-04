import csv
from flask import Flask, render_template, url_for, request, redirect
import google.generativeai as genai
import requests



gemini_api_key = "api_key"
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre-equipe')
def sobre_equipe():
    return render_template('sobre.html')

@app.route('/10anos')
def kids():
    return render_template('10anos.html')

@app.route('/iniciante')
def iniciante():
    return render_template('iniciante.html')

@app.route('/intermediario')
def intermediario():
    return render_template('intermediario.html')

@app.route('/programador')
def programador():
    return render_template('programador.html')

@app.route('/basico')
def basico():
    return render_template('basico.html')
@app.route('/selecao')
def selecao():
    return render_template('selecao.html')
@app.route('/vetmat')
def vetmat():
    return render_template('vetomatriz.html')
@app.route('/repeticao')
def repeticao():
    return render_template('repeticao.html')
@app.route('/funepro')
def funcepro():
    return render_template('funceproc.html')
@app.route('/traexc')
def traexc():
    return render_template('trateexce.html')
@app.route('/bibliotecas')
def bibliotecas():
    return render_template('bibliotecas.html')
@app.route('/datanalise')
def datanalise():
    return render_template('dataanalise.html')

@app.route('/conta', methods=['GET', 'POST'])
def conta():
    texto_usuario = None

    if request.method == 'POST':
        texto_usuario = request.form.get('escreva')
        if texto_usuario and texto_usuario.strip() != "":
            with open('bd_sobre_mim.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow([texto_usuario])

    return render_template('conta.html', texto_usuario=texto_usuario)


rotas_validas = {
    "home": "/",
    "glossario": "/glossario",
    "sobre": "/sobre-equipe",
    "10anos": "/10anos",
    "iniciante": "/iniciante",
    "intermediario": "/intermediario",
    "programador": "/programador",
    "basico": "/basico",
    "selecao": "/selecao",
    "repeticao": "/repeticao",
    "vetmat": "/vetmat",
    "funepro": "/funepro",
    "traexc": "/traexc",
    "bibliotecas": "/bibliotecas",
    "datanalise": "/datanalise",
    "conta": "/conta",
    "ia": "/ia"
}

@app.route('/buscar_glossario')
def buscar_glossario():
    termo = request.args.get('q', '').lower().strip()
    glossariodetermos = []

    with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for linha in reader:
            if len(linha) >= 1:
                glossariodetermos.append(linha[0].lower().strip())
    if termo in glossariodetermos:
        return render_template('glossario.html', termo_encontrado=termo)
    else:
        return render_template('404.html')

@app.route('/buscar')
def buscar():
    termo = request.args.get('q', '').lower().strip()

    if termo in rotas_validas:
        return redirect(rotas_validas[termo])
    else:
        return render_template('notfound.html'), 404

@app.route('/glossario')
def glossario():

    glossariodetermos = []
    with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for t in reader:
            glossariodetermos.append(t)

    return render_template('glossario.html', glossario=glossariodetermos)

@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')

@app.route('/excluir_termo')
def excluir_termo():
    return render_template('excluir_termo.html')

@app.route('/alterar_termo')
def alterar_termo():
    return render_template('alterar_termo.html')

@app.route('/criar_termo', methods = ['POST'])
def criar_termo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

@app.route('/remover_termo', methods = ['POST'])
def remover_termo():

    termos = request.form['termo']
    termos_restantes = []
    termo_encontrado = False

    with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i in reader:
            if i[0].lower().strip() != termos.lower().strip():
                termos_restantes.append(i)
            else:
                termo_encontrado = True
    if not termo_encontrado:
        return render_template('404.html')

    with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(termos_restantes)

    return redirect(url_for('glossario'))

@app.route('/trocar_termo', methods = ['POST'])
def trocar_termo():
    termo = request.form['termo']
    novo_termo = request.form['novo_termo']
    nova_definicao = request.form['nova_definicao']
    termos = []


    with open('bd_glossario.csv', 'r+', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i in reader:
            if i[0] == termo:
                termos.append([novo_termo, nova_definicao])
            else:
                termos.append(i)

    with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(termos)

    return redirect(url_for('glossario'))

def gerar_resposta_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

@app.route('/ia', methods=['GET', 'POST'])
def ia():
    resposta = ""
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        if pergunta:
            resposta = gerar_resposta_gemini(pergunta)
    return render_template('ia.html', resposta=resposta)

app.run(debug=True)
