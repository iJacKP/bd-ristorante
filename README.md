# 🍔 Sistema de Restaurante - Trabalho Final de Banco de Dados

## 📖 Descrição
Este projeto é um sistema simples para gerenciamento de um restaurante, desenvolvido como Trabalho Prático da disciplina de Banco de Dados. A aplicação permite o gerenciamento de clientes, produtos, categorias e pedidos, realizando operações no banco de dados relacional.

---

## 🛠️ Tecnologias
- **Python 3.10+**
- **Flask**
- **PostgreSQL 14+**
- **Pipenv ou virtualenv (opcional)**


---

## 📦 Estrutura do Projeto

restaurante/
├── app.py             # Código principal Flask
├── requirements.txt   # Dependências Python
├── database.sql       # Script DDL do banco
├── mer.png            # Modelo Entidade-Relacionamento
├── integrantes.txt    # Nomes da equipe
└── README.md          # Este arquivo

---

## 🚀 Como Executar

### 1️⃣ Clone o repositório:

git clone <https://github.com/iJacKP/bd-ristorante.git>
cd bd-ristorante

### 2️⃣ Crie e ative um ambiente virtual:

python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows


### 2️⃣ Instale as dependências

pip install -r requirements.txt

### 3️⃣ Crie o banco de dados no PostgreSQL

psql -U postgres
CREATE DATABASE ristorante;
\q

### 4️⃣ Importe o script do banco

psql -U postgres -d ristorante -f database.sql

### 5️⃣ Configure o usuário e senha no arquivo app.py

db_config = {
    "host": "localhost",
    "database": "ristorante",
    "user": "seu_usuario",
    "password": "sua_senha"
}

### 6️⃣ Rode a API

python app.py

### A API estará disponível em:
📍 http://127.0.0.1:5000/

### 📖 Endpoints da API

⸻

### 🧑‍🍳 Clientes

📥 Listar clientes

================================
📖 Endpoints da API
===============================

🧑‍🍳 CLIENTES
-------------------------------

📥 Listar clientes
GET /clientes
Query SQL:
SELECT * FROM cliente;

📥 Adicionar cliente
POST /clientes
Query SQL:
INSERT INTO cliente (nome, email) VALUES (%s, %s);

📥 Atualizar cliente
PUT /clientes/<id>
Query SQL:
UPDATE cliente SET nome=%s, email=%s WHERE id_cliente=%s;

📥 Deletar cliente
DELETE /clientes/<id>
Query SQL:
DELETE FROM cliente WHERE id_cliente=%s;


🗂️ CATEGORIAS
-------------------------------

📥 Listar categorias
GET /categorias
Query SQL:
SELECT * FROM categoria;

📥 Adicionar categoria
POST /categorias
Query SQL:
INSERT INTO categoria (nome) VALUES (%s);

📥 Atualizar categoria
PUT /categorias/<id>
Query SQL:
UPDATE categoria SET nome=%s WHERE id_categoria=%s;

📥 Deletar categoria
DELETE /categorias/<id>
Query SQL:
DELETE FROM categoria WHERE id_categoria=%s;


🍝 PRODUTOS
-------------------------------

📥 Listar produtos
GET /produtos
Query SQL:
SELECT * FROM produto;

📥 Adicionar produto
POST /produtos
Query SQL:
INSERT INTO produto (nome, preco, id_categoria) VALUES (%s, %s, %s);

📥 Atualizar produto
PUT /produtos/<id>
Query SQL:
UPDATE produto SET nome=%s, preco=%s, id_categoria=%s WHERE id_produto=%s;

📥 Deletar produto
DELETE /produtos/<id>
Query SQL:
DELETE FROM produto WHERE id_produto=%s;


📝 PEDIDOS
-------------------------------

📥 Listar pedidos
GET /pedidos
Query SQL:
SELECT * FROM pedido;

📥 Adicionar pedido
POST /pedidos
Query SQL:
INSERT INTO pedido (id_cliente) VALUES (%s);

📥 Atualizar pedido
PUT /pedidos/<id>
Query SQL:
UPDATE pedido SET id_cliente=%s WHERE id_pedido=%s;

📥 Deletar pedido
DELETE /pedidos/<id>
Query SQL:
DELETE FROM pedido WHERE id_pedido=%s;


🍽️ ITENS DO PEDIDO
-------------------------------

📥 Listar itens do pedido
GET /itens_pedido
Query SQL:
SELECT * FROM item_pedido;

📥 Adicionar item ao pedido
POST /itens_pedido
Query SQL:
INSERT INTO item_pedido (quantidade, id_pedido, id_produto) VALUES (%s, %s, %s);

📥 Atualizar item do pedido
PUT /itens_pedido/<id>
Query SQL:
UPDATE item_pedido SET quantidade=%s WHERE id_item=%s;

📥 Deletar item do pedido
DELETE /itens_pedido/<id>
Query SQL:
DELETE FROM item_pedido WHERE id_item=%s;

===============================