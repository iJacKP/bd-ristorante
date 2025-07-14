from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
db_config = {
    "host": "localhost",
    "database": "ristorante",
    "user": "jack", 
    "password": ""
}

# Função para conectar ao banco
def conectar_db():
    return psycopg2.connect(**db_config)


# CLIENTES - SELECT - Listar clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cliente")
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultados)

# CLIENTES - INSERT - Adicionar cliente
@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO cliente (nome, email) VALUES (%s, %s)", (nome, email))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Cliente cadastrado com sucesso!"}), 201

# CLIENTES - UPDATE - Atualizar cliente
@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("UPDATE cliente SET nome=%s, email=%s WHERE id_cliente=%s", (nome, email, id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Cliente atualizado com sucesso!"})

# CLIENTES - DELETE - Remover cliente
@app.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM cliente WHERE id_cliente=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Cliente removido com sucesso!"})

# CATEGORIAS - SELECT - Listar categorias
@app.route('/categorias', methods=['GET'])
def listar_categorias():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM categoria")
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultados)

# CATEGORIAS - INSERT - Adicionar categoria
@app.route('/categorias', methods=['POST'])
def adicionar_categoria():
    dados = request.get_json()
    nome = dados['nome']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO categoria (nome) VALUES (%s)", (nome,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Categoria cadastrada com sucesso!"}), 201

# CATEGORIAS - UPDATE - Atualizar categoria
@app.route('/categorias/<int:id>', methods=['PUT'])
def atualizar_categoria(id):
    dados = request.get_json()
    nome = dados['nome']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("UPDATE categoria SET nome=%s WHERE id_categoria=%s", (nome, id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Categoria atualizada com sucesso!"})

# CATEGORIAS - DELETE - Remover categoria
@app.route('/categorias/<int:id>', methods=['DELETE'])
def deletar_categoria(id):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM categoria WHERE id_categoria=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Categoria removida com sucesso!"})

# PRODUTOS - 

# PRODUTOS - SELECT - Listar produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM produto")
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultados)

# PRODUTOS - INSERT - Adicionar produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    dados = request.get_json()
    nome = dados['nome']
    preco = dados['preco']
    id_categoria = dados['id_categoria']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO produto (nome, preco, id_categoria) VALUES (%s, %s, %s)", (nome, preco, id_categoria))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Produto cadastrado com sucesso!"}), 201

# PRODUTOS - UPDATE - Atualizar produto
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    nome = dados['nome']
    preco = dados['preco']
    id_categoria = dados['id_categoria']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("UPDATE produto SET nome=%s, preco=%s, id_categoria=%s WHERE id_produto=%s", (nome, preco, id_categoria, id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Produto atualizado com sucesso!"})

# PRODUTOS - DELETE - Remover produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM produto WHERE id_produto=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Produto removido com sucesso!"})

# PEDIDOS - SELECT - Listar pedidos
@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pedido")
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultados)

# PEDIDOS - INSERT - Adicionar pedido
@app.route('/pedidos', methods=['POST'])
def adicionar_pedido():
    dados = request.get_json()
    id_cliente = dados['id_cliente']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO pedido (id_cliente) VALUES (%s)", (id_cliente,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Pedido cadastrado com sucesso!"}), 201

# PEDIDOS - UPDATE - Atualizar pedido
@app.route('/pedidos/<int:id>', methods=['PUT'])
def atualizar_pedido(id):
    dados = request.get_json()
    id_cliente = dados['id_cliente']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("UPDATE pedido SET id_cliente=%s WHERE id_pedido=%s", (id_cliente, id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Pedido atualizado com sucesso!"})

# PEDIDOS - DELETE - Remover pedido
@app.route('/pedidos/<int:id>', methods=['DELETE'])
def deletar_pedido(id):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM pedido WHERE id_pedido=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Pedido removido com sucesso!"})

# ITENS DO PEDIDO - SELECT - Listar itens do pedido
@app.route('/itens_pedido', methods=['GET'])
def listar_itens_pedido():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM item_pedido")
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultados)

# ITENS DO PEDIDO -INSERT - Adicionar item ao pedido
@app.route('/itens_pedido', methods=['POST'])
def adicionar_item_pedido():
    dados = request.get_json()
    quantidade = dados['quantidade']
    id_pedido = dados['id_pedido']
    id_produto = dados['id_produto']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO item_pedido (quantidade, id_pedido, id_produto) VALUES (%s, %s, %s)", (quantidade, id_pedido, id_produto))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Item adicionado ao pedido com sucesso!"}), 201

# ITENS DO PEDIDO - UPDATE - Atualizar item do pedido
@app.route('/itens_pedido/<int:id>', methods=['PUT'])
def atualizar_item_pedido(id):
    dados = request.get_json()
    quantidade = dados['quantidade']
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("UPDATE item_pedido SET quantidade=%s WHERE id_item=%s", (quantidade, id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Item do pedido atualizado com sucesso!"})

# ITENS DO PEDIDO - DELETE - Remover item do pedido
@app.route('/itens_pedido/<int:id>', methods=['DELETE'])
def deletar_item_pedido(id):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM item_pedido WHERE id_item=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensagem": "Item do pedido removido com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)