from flask import Flask, request, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Formulários
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/formulario_completo')
def formulario_completo():
    return render_template('formulario_completo.html')

@app.route('/formulario_criativo')
def formulario_criativo():
    return render_template('formulario_criativo.html')


def corrigir_url(url):
    url = url.strip()
    if url and not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url
    return url

# Currículo Simples (recebe dados via JSON)
@app.route('/gerar_curriculo', methods=['POST'])
def gerar_curriculo():
    dados = request.get_json()

    nome = dados.get("nome", "Nome não informado")
    email = dados.get("email", "Email não informado")
    telefone = dados.get("telefone", "Telefone não informado")
    resumo = dados.get("resumo", "Resumo não informado").replace('\n', '<br>')
    formacao = dados.get("formacao", "Formação não informada").replace('\n', '<br>')
    experiencia = dados.get("experiencia", "Experiência não informada").replace('\n', '<br>')
    habilidades = dados.get("habilidades", "Habilidades não informadas").replace('\n', '<br>')

    idiomas = dados.get("idiomas", "").replace('\n', '<br>')

    linkedin = corrigir_url(dados.get("linkedin", ""))
    portfolio = corrigir_url(dados.get("portfolio", ""))

    return render_template(
        'curriculo_simples.html',
        nome=nome,
        email=email,
        telefone=telefone,
        resumo=resumo,
        formacao=formacao,
        experiencia=experiencia,
        habilidades=habilidades,
        idiomas=idiomas,
        linkedin=linkedin,
        portfolio=portfolio
    )


# Currículo Criativo (via JSON)
@app.route('/gerar_curriculo_criativo', methods=['POST'])
def gerar_curriculo_criativo():
    dados = request.get_json()

    nome = dados.get("nome", "Nome não informado")
    email = dados.get("email", "Email não informado")
    telefone = dados.get("telefone", "Telefone não informado")
    resumo = dados.get("resumo", "Resumo não informado").replace('\n', '<br>')
    formacao = dados.get("formacao", "Formação não informada").replace('\n', '<br>')
    experiencia = dados.get("experiencia", "Experiência não informada").replace('\n', '<br>')
    habilidades = dados.get("habilidades", "Habilidades não informadas").replace('\n', '<br>')
    perfil = dados.get("perfil", "Perfil pessoal não informado").replace('\n', '<br>')

    idiomas = dados.get("idiomas", "").replace('\n', '<br>')

    linkedin = corrigir_url(dados.get("linkedin", ""))
    portfolio = corrigir_url(dados.get("portfolio", ""))

    return render_template(
        'curriculo_criativo.html',
        nome=nome,
        email=email,
        telefone=telefone,
        resumo=resumo,
        formacao=formacao,
        experiencia=experiencia,
        habilidades=habilidades,
        perfil=perfil,
        idiomas=idiomas,
        linkedin=linkedin,
        portfolio=portfolio
    )


# Currículo Completo (via JSON)
@app.route('/gerar_curriculo_completo', methods=['POST'])
def gerar_curriculo_completo():
    dados = request.get_json()

    nome = dados.get("nome", "Nome não informado")
    email = dados.get("email", "Email não informado")
    telefone = dados.get("telefone", "Telefone não informado")
    resumo = dados.get("resumo", "Resumo não informado").replace('\n', '<br>')
    formacao = dados.get("formacao", "Formação não informada").replace('\n', '<br>')
    experiencia = dados.get("experiencia", "Experiência não informada").replace('\n', '<br>')
    habilidades = dados.get("habilidades", "Habilidades não informadas").replace('\n', '<br>')
    nome_completo = dados.get("nome_completo", "Nome completo não informado").replace('\n', '<br>')
    data_nasc = dados.get("data_nasc", "Data de nascimento não informada").replace('\n', '<br>')
    naturalidade = dados.get("naturalidade", "Naturalidade não informada").replace('\n', '<br>')
    disp = dados.get("disp", "Disponibilidade não informada").replace('\n', '<br>')

    linkedin = corrigir_url(dados.get("linkedin", ""))
    portfolio = corrigir_url(dados.get("portfolio", ""))

    return render_template(
        'curriculo_completo.html',
        nome=nome,
        email=email,
        telefone=telefone,
        resumo=resumo,
        formacao=formacao,
        experiencia=experiencia,
        habilidades=habilidades,
        nome_completo=nome_completo,
        data_nasc=data_nasc,
        naturalidade=naturalidade,
        disp=disp,
        linkedin=linkedin,
        portfolio=portfolio
    )


# Executar o app
if __name__ == '__main__':
    app.run(debug=True)
