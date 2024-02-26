from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

#
# Estrutura de Rotas /cliente
# /clientes/ - Lista os clientes
# /clientes/ (POST) - Inserir o cliente no servidor
# /clientes/new (GET) - Renderiza formulario para criar um cliente
# /clientes/<id> (GET) - Obtem dados de um cliente
# /clientes/<id>/edit (GET) - Renderiza formulário para editar um cliente
# /clientes/<id>/update (PUT) - Atualiza dados do cliente
# /clientes/<id>/delete (DELETE) - Deleta Registro do cliente
# 

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    # Insere Clientes na Lista
    
    data = request.json
    
    novo_user = {
        "id": len(CLIENTES) +1,
        "nome": data['nome'],
        'email': data['email']
    }

    CLIENTES.append(novo_user)

    return render_template('item_cliente.html', cliente=novo_user)
    

@cliente_route.route('/new')
def form_criacao_cliente():
    # Renderiza formulário para inserir os dados de cliente
    return render_template('form_clientes.html')

@cliente_route.route('/<int:id_cliente>')
def obter_dados_cliente(id_cliente):
    # Carrega dados do cliente

    cliente = list(filter(lambda c: c['id'] == id_cliente, CLIENTES))[0]

    return render_template('informacoes_clientes.html', cliente=cliente)

@cliente_route.route('/<int:id_cliente>/edit')
def form_edicao_cliente(id_cliente):
    # Renderiza formulário para atualizar dados de cliente
    cliente = None

    for c in CLIENTES:
        if c['id'] == id_cliente:
            cliente = c

    return render_template('form_clientes.html', cliente=cliente)

@cliente_route.route('/<int:id_cliente>/update', methods=['PUT'])
def atualiza_dados_cliente(id_cliente):
    # Atualiza dados do cliente
    
    cliente_editado = None

    #Obter dados de form de edicao
    data = request.json

    # Obter user pelo id
    for c in CLIENTES:
        if c['id'] == id_cliente:
            c['nome'] = data['nome']
            c['email'] = data['email']

            cliente_editado = c

    # editar usuário
            
    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:id_cliente>/delete', methods=['DELETE'])
def deleta_registro_cliente(id_cliente):
    # Deleta registro do cliente
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != id_cliente]

    return { 'deleted' : 'ok' }
