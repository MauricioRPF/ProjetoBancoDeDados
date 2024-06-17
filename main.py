from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import base64

app = Flask(__name__)

def b64encode(data):
    return base64.b64encode(data).decode('utf-8')

app.jinja_env.filters['b64encode'] = b64encode

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="Mauricio",  # Substitua pelo seu usuário do MySQL
        password="#Mallzz52",  # Substitua pela sua senha do MySQL
        database="starlink",
        port=3306
    )

def cadastrar_cliente(cpf, nome, email, telefone, endereco):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO identificacao (cpf, nome, e_mail, telefone, endereco) VALUES (%s, %s, %s, %s, %s)"
    valores = (cpf, nome, email, telefone, endereco)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_cliente(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM identificacao WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM identificacao"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def cadastrar_conta(cpf, usuario, senha, nascimento, genero, foto):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO info_conta (cpf, usuario, senha, nascimento, genero, foto) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (cpf, usuario, senha, nascimento, genero, foto)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_conta(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Consulta na tabela info_conta
    sql_conta = "SELECT * FROM info_conta WHERE cpf = %s"
    cursor.execute(sql_conta, (cpf,))
    resultado_conta = cursor.fetchall()
    
    # Consulta na tabela pref_config
    sql_pref_config = "SELECT * FROM pref_config WHERE cpf = %s"
    cursor.execute(sql_pref_config, (cpf,))
    resultado_pref_config = cursor.fetchall()
    
    # Consulta na tabela atv_online
    sql_atv_online = "SELECT * FROM atv_online WHERE cpf = %s"
    cursor.execute(sql_atv_online, (cpf,))
    resultado_atv_online = cursor.fetchall()
    
    # Consulta na tabela dados_localizacao
    sql_dados_localizacao = "SELECT * FROM dados_localizacao WHERE cpf = %s"
    cursor.execute(sql_dados_localizacao, (cpf,))
    resultado_dados_localizacao = cursor.fetchall()
    
    # Consulta na tabela info_sociais
    sql_info_sociais = "SELECT * FROM info_sociais WHERE cpf = %s"
    cursor.execute(sql_info_sociais, (cpf,))
    resultado_info_sociais = cursor.fetchall()
    
    # Consulta na tabela info_pagamento
    sql_info_pagamento = "SELECT * FROM info_pagamento WHERE cpf = %s"
    cursor.execute(sql_info_pagamento, (cpf,))
    resultado_info_pagamento = cursor.fetchall()
    
    # Consulta na tabela info_tecnicas
    sql_info_tecnicas = "SELECT * FROM info_tecnicas WHERE cpf = %s"
    cursor.execute(sql_info_tecnicas, (cpf,))
    resultado_info_tecnicas = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return (resultado_conta, resultado_pref_config, resultado_atv_online, resultado_dados_localizacao, 
            resultado_info_sociais, resultado_info_pagamento, resultado_info_tecnicas)

def deletar_cliente(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Deletar registros nas tabelas que têm referência ao cliente
    sql_delete_info_conta = "DELETE FROM info_conta WHERE cpf = %s"
    sql_delete_pref_config = "DELETE FROM pref_config WHERE cpf = %s"
    sql_delete_atv_online = "DELETE FROM atv_online WHERE cpf = %s"
    sql_delete_dados_localizacao = "DELETE FROM dados_localizacao WHERE cpf = %s"
    sql_delete_info_sociais = "DELETE FROM info_sociais WHERE cpf = %s"
    sql_delete_info_pagamento = "DELETE FROM info_pagamento WHERE cpf = %s"
    sql_delete_info_tecnicas = "DELETE FROM info_tecnicas WHERE cpf = %s"
    sql_delete_identificacao = "DELETE FROM identificacao WHERE cpf = %s"

    # Executar as queries de deleção
    cursor.execute(sql_delete_info_conta, (cpf,))
    cursor.execute(sql_delete_pref_config, (cpf,))
    cursor.execute(sql_delete_atv_online, (cpf,))
    cursor.execute(sql_delete_dados_localizacao, (cpf,))
    cursor.execute(sql_delete_info_sociais, (cpf,))
    cursor.execute(sql_delete_info_pagamento, (cpf,))
    cursor.execute(sql_delete_info_tecnicas, (cpf,))
    cursor.execute(sql_delete_identificacao, (cpf,))

    conexao.commit()
    cursor.close()
    conexao.close()

def listar_contas():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM info_conta"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def cadastrar_atividade_online(cpf, historico, preferencias, compras, duracao_sessoes, click_ad):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO atv_online (cpf, historico, preferencias, compras, duracao_sessoes, click_ad) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (cpf, historico, preferencias, compras, duracao_sessoes, click_ad)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_atividade_online(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM atv_online WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_atividades_online():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM atv_online"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def cadastrar_dados_localizacao(cpf, loc_geografica, locais_visitados):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO dados_localizacao (cpf, loc_geografica, locais_visitados) VALUES (%s, %s, %s)"
    valores = (cpf, loc_geografica, locais_visitados)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_dados_localizacao(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM dados_localizacao WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_dados_localizacao():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM dados_localizacao"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def cadastrar_info_sociais(cpf, interacoes, amigos):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO info_sociais (cpf, interacoes, amigos) VALUES (%s, %s, %s)"
    valores = (cpf, interacoes, amigos)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_info_sociais(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM info_sociais WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_info_sociais():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM info_sociais"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def cadastrar_info_pagamento(cpf, cartao, historico_transacoes):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO info_pagamento (cpf, cartao, historico_transacoes) VALUES (%s, %s, %s)"
    valores = (cpf, cartao, historico_transacoes)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_info_pagamento(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM info_pagamento WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_info_pagamento():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM info_pagamento"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def cadastrar_pref_config(cpf, idioma_pref, config_privacidade, pref_notificacao):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO pref_config (cpf, idioma_pref, config_privacidade, pref_notificacao) VALUES (%s, %s, %s, %s)"
    valores = (cpf, idioma_pref, config_privacidade, pref_notificacao)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_pref_config(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM pref_config WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_pref_config():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM pref_config"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def cadastrar_info_tecnicas(cpf, tipo_dispositivo, so, nav_web, ende_ip):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO info_tecnicas (cpf, tipo_dispositivo, so, nav_web, ende_ip) VALUES (%s, %s, %s, %s, %s)"
    valores = (cpf, tipo_dispositivo, so, nav_web, ende_ip)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_info_tecnicas(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM info_tecnicas WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_info_tecnicas():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM info_tecnicas"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        cpf = request.form['cpf']
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        cadastrar_cliente(cpf, nome, email, telefone, endereco)
        return redirect(url_for('index'))
    return render_template('cadastrar.html')

@app.route('/deletar_cliente', methods=['POST'])
def deletar_cliente_view():
    if request.method == 'POST':
        cpf = request.form['cpf']
        deletar_cliente(cpf)
        return redirect(url_for('index'))

@app.route('/consultar', methods=['GET', 'POST'])
def consultar():
    cliente = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        cliente = consultar_cliente(cpf)
    return render_template('consultar.html', cliente=cliente)

@app.route('/relatorio')
def relatorio():
    clientes = listar_clientes()
    return render_template('relatorio.html', clientes=clientes)

@app.route('/cadastrar_conta', methods=['GET', 'POST'])
def cadastrar_conta_view():
    if request.method == 'POST':
        cpf = request.form['cpf']
        usuario = request.form['usuario']
        senha = request.form['senha']
        nascimento = request.form['nascimento']
        genero = request.form['genero']
        foto = request.files['foto'].read()  # Assuming the file is sent as binary
        cadastrar_conta(cpf, usuario, senha, nascimento, genero, foto)
        return redirect(url_for('index'))
    return render_template('cadastrar_conta.html')

@app.route('/consultar_conta', methods=['GET', 'POST'])
def consultar_conta_view():
    conta = None
    pref_config = None
    atv_online = None
    dados_localizacao = None
    info_sociais = None
    info_pagamento = None
    info_tecnicas = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        (conta, pref_config, atv_online, dados_localizacao, 
         info_sociais, info_pagamento, info_tecnicas) = consultar_conta(cpf)
    return render_template('consultar_conta.html', conta=conta, pref_config=pref_config, atv_online=atv_online,
                           dados_localizacao=dados_localizacao, info_sociais=info_sociais, 
                           info_pagamento=info_pagamento, info_tecnicas=info_tecnicas)

@app.route('/relatorio_contas')
def relatorio_contas():
    contas = listar_contas()
    return render_template('relatorio_contas.html', contas=contas)

@app.route('/cadastrar_atividade_online', methods=['GET', 'POST'])
def cadastrar_atividade_online_view():
    if request.method == 'POST':
        cpf = request.form['cpf']
        historico = request.form['historico']
        preferencias = request.form['preferencias']
        compras = request.form['compras']
        duracao_sessoes = request.form['duracao_sessoes']
        click_ad = request.form['click_ad']
        cadastrar_atividade_online(cpf, historico, preferencias, compras, duracao_sessoes, click_ad)
        return redirect(url_for('index'))
    return render_template('cadastrar_atividade_online.html')

@app.route('/consultar_atividade_online', methods=['GET', 'POST'])
def consultar_atividade_online_view():
    atividade = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        atividade = consultar_atividade_online(cpf)
    return render_template('consultar_atividade_online.html', atividade=atividade)

@app.route('/relatorio_atividades_online')
def relatorio_atividades_online():
    atividades = listar_atividades_online()
    return render_template('relatorio_atividades_online.html', atividades=atividades)

@app.route('/cadastrar_dados_localizacao', methods=['GET', 'POST'])
def cadastrar_dados_localizacao_view():
    if request.method == 'POST':
        cpf = request.form['cpf']
        loc_geografica = request.form['loc_geografica']
        locais_visitados = request.form['locais_visitados']
        cadastrar_dados_localizacao(cpf, loc_geografica, locais_visitados)
        return redirect(url_for('index'))
    return render_template('cadastrar_dados_localizacao.html')

@app.route('/consultar_dados_localizacao', methods=['GET', 'POST'])
def consultar_dados_localizacao_view():
    dados = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        dados = consultar_dados_localizacao(cpf)
    return render_template('consultar_dados_localizacao.html', dados=dados)

@app.route('/relatorio_dados_localizacao')
def relatorio_dados_localizacao():
    dados = listar_dados_localizacao()
    return render_template('relatorio_dados_localizacao.html', dados=dados)

@app.route('/cadastrar_info_sociais', methods=['GET', 'POST'])
def cadastrar_info_sociais_view():
    if request.method == 'POST':
        cpf = request.form['cpf']
        interacoes = request.form['interacoes']
        amigos = request.form['amigos']
        cadastrar_info_sociais(cpf, interacoes, amigos)
        return redirect(url_for('index'))
    return render_template('cadastrar_info_sociais.html')

@app.route('/consultar_info_sociais', methods=['GET', 'POST'])
def consultar_info_sociais_view():
    info = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        info = consultar_info_sociais(cpf)
    return render_template('consultar_info_sociais.html', info=info)

@app.route('/relatorio_info_sociais')
def relatorio_info_sociais():
    infos = listar_info_sociais()
    return render_template('relatorio_info_sociais.html', infos=infos)

@app.route('/cadastrar_info_pagamento', methods=['GET', 'POST'])
def cadastrar_info_pagamento_view():
    if request.method == 'POST':
        cpf = request.form['cpf']
        cartao = request.form['cartao']
        historico_transacoes = request.form['historico_transacoes']
        cadastrar_info_pagamento(cpf, cartao, historico_transacoes)
        return redirect(url_for('index'))
    return render_template('cadastrar_info_pagamento.html')

@app.route('/consultar_info_pagamento', methods=['GET', 'POST'])
def consultar_info_pagamento_view():
    info = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        info = consultar_info_pagamento(cpf)
    return render_template('consultar_info_pagamento.html', info=info)

@app.route('/relatorio_info_pagamento')
def relatorio_info_pagamento():
    infos = listar_info_pagamento()
    return render_template('relatorio_info_pagamento.html', infos=infos)

@app.route('/cadastrar_pref_config', methods=['GET', 'POST'])
def cadastrar_pref_config_view():
    if request.method == 'POST':
        cpf = request.form['cpf']
        idioma_pref = request.form['idioma_pref']
        config_privacidade = request.form['config_privacidade']
        pref_notificacao = request.form['pref_notificacao']
        cadastrar_pref_config(cpf, idioma_pref, config_privacidade, pref_notificacao)
        return redirect(url_for('index'))
    return render_template('cadastrar_pref_config.html')

@app.route('/consultar_pref_config', methods=['GET', 'POST'])
def consultar_pref_config_view():
    config = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        config = consultar_pref_config(cpf)
    return render_template('consultar_pref_config.html', config=config)

@app.route('/relatorio_pref_config')
def relatorio_pref_config():
    configs = listar_pref_config()
    return render_template('relatorio_pref_config.html', configs=configs)

@app.route('/cadastrar_info_tecnicas', methods=['GET', 'POST'])
def cadastrar_info_tecnicas_view():
    if request.method == 'POST':
        cpf = request.form['cpf']
        tipo_dispositivo = request.form['tipo_dispositivo']
        so = request.form['so']
        nav_web = request.form['nav_web']
        ende_ip = request.form['ende_ip']
        cadastrar_info_tecnicas(cpf, tipo_dispositivo, so, nav_web, ende_ip)
        return redirect(url_for('index'))
    return render_template('cadastrar_info_tecnicas.html')

@app.route('/consultar_info_tecnicas', methods=['GET', 'POST'])
def consultar_info_tecnicas_view():
    info = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        info = consultar_info_tecnicas(cpf)
    return render_template('consultar_info_tecnicas.html', info=info)

@app.route('/relatorio_info_tecnicas')
def relatorio_info_tecnicas():
    infos = listar_info_tecnicas()
    return render_template('relatorio_info_tecnicas.html', infos=infos)

if __name__ == '__main__':
    app.run(debug=True)
