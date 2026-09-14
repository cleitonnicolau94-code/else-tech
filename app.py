from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/clientes")
def clientes():
    arquivo = open("clientes.txt", "r")

    lista = arquivo.readlines()

    arquivo.close()

    clientes = []

    for linha in lista:
        dados = linha.strip().split("|")
        clientes.append(dados)

    tabela = """
    <table border="1" cellpadding="10">
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Telefone</th>
            <th>Equipamento</th>
            <th>Ações</th>
        </tr>
    """

    for cliente in clientes:
        tabela += """
        <tr>
            <td>""" + cliente[0] + """</td>
            <td>""" + cliente[1] + """</td>
            <td>""" + cliente[2] + """</td>
            <td>""" + cliente[3] + """</td>
            <td><a href="/editar/""" + cliente[0] + """">✏️ Editar</a></td>
        </tr>
        """

    tabela += "</table>"

    return """
    <h1>GERENCIAMENTO DE CLIENTES</h1>
    <p>Clientes cadastrados: """ + str(len(lista)) + """</p>

    """ + tabela + """

    <br>
    <a href="/">← Voltar ao menu</a>
    """


@app.route("/editar/<id_cliente>")
def editar(id_cliente):
    return """
    <h1>EDITAR CLIENTE</h1>

    <p>ID do cliente: """ + id_cliente + """</p>

    <p>Em breve vamos colocar aqui os dados para edição.</p>

    <a href="/clientes">← Voltar para clientes</a>
    """


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        equipamento = request.form["equipamento"]

        arquivo_leitura = open("clientes.txt", "r")
        linhas = arquivo_leitura.readlines()
        arquivo_leitura.close()

        id_cliente = len(linhas) + 1

        arquivo = open("clientes.txt", "a")
        arquivo.write(
            str(id_cliente)
            + "|"
            + nome
            + "|"
            + telefone
            + "|"
            + equipamento
            + "\n"
        )
        arquivo.close()

        return redirect("/clientes")

    return """
    <h1>CADASTRAR CLIENTE</h1>

    <form method="POST">
        <p>Nome:</p>
        <input type="text" name="nome">

        <p>Telefone:</p>
        <input type="text" name="telefone">

        <p>Equipamento:</p>
        <input type="text" name="equipamento">

        <br><br>
        <button>Cadastrar</button>
    </form>

    <br>
    <a href="/clientes">← Voltar para clientes</a>
    """


app.run()