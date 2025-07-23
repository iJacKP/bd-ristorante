# 🍔 BD Ristorante - Trabalho Prático - Banco de Dados

## 📖 Descrição
Este projeto é uma API simples para gerenciamento de um restaurante, desenvolvido como Trabalho Prático da disciplina de Banco de Dados. A aplicação permite o gerenciamento de clientes, produtos, categorias e pedidos, realizando operações no banco de dados relacional.

---

## 🛠️ Tecnologias
- **Pytho3.10+**
- **Flask**
- **PostgreSQL 14+**
- **Pipenv ou virtualenv (opcional)**


---

## 📦 Estrutura do Projeto

```bash
bd-ristorante/
├── app.py             # Código principal Flask
├── requirements.txt   # Dependências Python
├── database.sql       # Script DDL do banco
├── mer.png            # Modelo Entidade-Relacionamento
├── integrantes.txt    # Nomes da equipe
└── README.md          # Este arquivo
```

---

## 🚀 Como Executar

### 1️⃣ Clone o repositório:

```bash
git clone <https://github.com/iJacKP/bd-ristorante.git>
cd bd-ristorante
```


### 2️⃣ Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Crie o banco de dados no PostgreSQL

```bash
psql -U postgres
CREATE DATABASE ristorante;
\q
```

### 4️⃣ Importe o script do banco

```bash
psql -U postgres -d ristorante -f database.sql
```

### 5️⃣ Configure o usuário e senha no arquivo app.py

```bash
db_config = {
    "host": "localhost",
    "database": "ristorante",
    "user": "seu_usuario",
    "password": "sua_senha"
}
```

### 6️⃣ Rode a API

```bash
python app.py
```

### A API estará disponível em:
📍 http://127.0.0.1:5000/

### 📖 Endpoints da API

⸻
## Referências da API 

### 🏁 Rota Inicial

```http
GET /
```

| Paramêtro | Tipo | Descrição                | Query |
| :-------- | :----| :---------------------------| ---------------------- |
| _None_    |  Retorna uma mensagem simples. | None – apenas retorna JSON {"mensagem": "API está rodando!"} |

### 🧑‍🍳 Clientes

#### Buscar clientes

```http
GET /clientes
```

| Paramêtro | Tipo | Descrição                | Query |
| :-------- | :----| :---------------------------|---------------------- |
| _None_    |      | Retorna todos os clientes.  | SELECT * FROM clientes |

---

#### Adicionar cliente

```http
POST /clientes
```

| Body | Tipo     | Descrição                  | Query |
| :------------- | :------- | :----------------------------| ---------------------- |
| `nome`         | `string` | **Required**. Nome do cliente| INSERT INTO clientes (nome, email) VALUES (?, ?) |
| `email`        | `string` | **Required**. Email do cliente|

---

#### Atualizar cliente

```http
PUT /clientes/${id}
```

| Paramêtro | Tipo  | Descrição               | Query |
| :-------- | :-----| :-------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID do cliente| UPDATE clientes SET nome = ?, email = ? WHERE id = ? |

| Body | Tipo     | Descrição                  |
| :------------- | :------- | :----------------------------|
| `nome`         | `string` | **Required**. Novo nome       |
| `email`        | `string` | **Required**. Novo email      |

---

#### Deletar cliente

```http
DELETE /clientes/${id}
```

| Paramêtro | Tipo  | Descrição               | Query |
| :-------- | :-----| :-------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID do cliente| DELETE FROM clientes WHERE id = ? |

---

### 🗂️ Categorias

#### Buscar categorias

```http
GET /categorias
```

| Paramêtro | Tipo | Descrição                   | Query |
| :-------- | :----| :-----------------------------| ---------------------- |
| _None_    |      | Retorna todas as categorias.  | SELECT * FROM categorias |

---

#### Adicionar categoria

```http
POST /categorias
```

| Body | Tipo     | Descrição                     | Query |
| :------------- | :------- | :--------------------------------| ---------------------- |
| `nome`         | `string` | **Required**. Nome da categoria. | INSERT INTO categorias (nome) VALUES (?) |

---

#### Atualizar categoria

```http
PUT /categorias/${id}
```

| Paramêtro | Tipo  | Descrição                 |Query |
| :-------- | :-----| :---------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID da categoria| UPDATE categorias SET nome = ? WHERE id = ? |

| Body | Tipo     | Descrição                 |
| :------------- | :------- | :----------------------------|
| `nome`         | `string` | **Required**. Novo nome       |

---

#### Deletar categoria

```http
DELETE /categorias/${id}
```

| Paramêtro | Tipo  | Descrição                 | Query |
| :-------- | :-----| :---------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID da categoria| DELETE FROM categorias WHERE id = ? |

---

### 🍝 Produtos

#### Buscar produtos

```http
GET /produtos
```

| Paramêtro | Tipo | Descrição                | Query |
| :-------- | :----| :---------------------------| ---------------------- |
| _None_    |      | Retorna todos os produtos.  | SELECT * FROM produtos |

---

#### Adicionar produto

```http
POST /produtos
```

| Body | Tipo     | Descrição                     | Query |
| :------------- | :------- | :--------------------------------| ---------------------- |
| `nome`         | `string` | **Required**. Nome do produto    | INSERT INTO produtos (nome, preco, id_categoria) VALUES (?, ?, ?) |
| `preco`        | `float`  | **Required**. Preço do produto   |
| `id_categoria` | `int`    | **Required**. ID da categoria    |

---

#### Atualizar produto

```http
PUT /produtos/${id}
```

| Paramêtro | Tipo  | Descrição                 | Query |
| :-------- | :-----| :---------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID do produto  | UPDATE produtos SET nome = ?, preco = ?, id_categoria = ? WHERE id = ? |

| Body | Tipo     | Descrição                     |
| :------------- | :------- | :--------------------------------|
| `nome`         | `string` | **Required**. Novo nome          |
| `preco`        | `float`  | **Required**. Novo preço         |
| `id_categoria` | `int`    | **Required**. Nova categoria     |

---

#### Deletar produto

```http
DELETE /produtos/${id}
```

| Paramêtro | Tipo  | Descrição                 | Query |
| :-------- | :-----| :---------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID do produto  | DELETE FROM produtos WHERE id = ? |

---

### 📝 Pedidos

#### Buscar pedidos

```http
GET /pedidos
```

| Paramêtro | Tipo | Descrição                | Query |
| :-------- | :----| :---------------------------| ---------------------- |
| _None_    |      | Retorna todos os pedidos.   | SELECT * FROM pedidos |

---

#### Adicionar pedido

```http
POST /pedidos
```

| Body | Tipo     | Descrição                     | Query |
| :------------- | :------- | :--------------------------------| ---------------------- |
| `id_cliente`   | `int`    | **Required**. ID do cliente      | INSERT INTO pedidos (id_cliente) VALUES (?) |

---

#### Atualizar pedido

```http
PUT /pedidos/${id}
```

| Paramêtro | Tipo  | Descrição                | Query |
| :-------- | :-----| :--------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID do pedido  | UPDATE pedidos SET id_cliente = ? WHERE id = ? |

| Body | Tipo     | Descrição                     |
| :------------- | :------- | :--------------------------------|
| `id_cliente`   | `int`    | **Required**. Novo cliente       |

---

#### Deletar pedido

```http
DELETE /pedidos/${id}
```

| Paramêtro | Tipo  | Descrição                | Query |
| :-------- | :-----| :--------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID do pedido  | DELETE FROM pedidos WHERE id = ? |

---

### 🍽️ Itens do Pedido

#### Buscar itens do pedido

```http
GET /itens_pedido
```

| Paramêtro | Tipo | Descrição                      | Query |
| :-------- | :----| :----------------------------------| ---------------------- |
| _None_    |      | Retorna todos os itens dos pedidos| SELECT * FROM itens_pedido |

---

#### Adicionar itens do pedido

```http
POST /itens_pedido
```

| Body | Tipo     | Descrição                          | Query |
| :------------- | :------- | :-------------------------------------| ---------------------- |
| `quantidade`   | `int`    | **Required**. Quantidade do item      | INSERT INTO itens_pedido (quantidade, id_pedido, id_produto) VALUES (?, ?, ?) |
| `id_pedido`    | `int`    | **Required**. ID do pedido            |
| `id_produto`   | `int`    | **Required**. ID do produto           |

---

#### Atualizar itens do pedido

```http
PUT /itens_pedido/${id}
```

| Paramêtro | Tipo  | Descrição                       | Query |
| :-------- | :-----| :-----------------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID do item do pedido | UPDATE itens_pedido SET quantidade = ? WHERE id = ? |

| Body | Tipo     | Descrição                          |
| :------------- | :------- | :-------------------------------------|
| `quantidade`   | `int`    | **Required**. Nova quantidade         |

---

#### Deletar itens do pedido

```http
DELETE /itens_pedido/${id}
```

| Paramêtro | Tipo  | Descrição                       | Query |
| :-------- | :-----| :-----------------------------------| ---------------------- |
| `id`      | `int` | **Required**. ID do item do pedido | DELETE FROM itens_pedido WHERE id = ? |