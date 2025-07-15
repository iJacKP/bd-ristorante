# 🍔 Sistema de Restaurante - Trabalho Final de Banco de Dados

## 📖 Descrição
Este projeto é um sistema simples para gerenciamento de um restaurante, desenvolvido como Trabalho Prático da disciplina de Banco de Dados. A aplicação permite o gerenciamento de clientes, produtos, categorias e pedidos, realizando operações no banco de dados relacional.

---

## 🛠️ Tecnologias
- **Pytho3.10+**
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
pythoapp.py
```

### A API estará disponível em:
📍 http://127.0.0.1:5000/

### 📖 Endpoints da API

⸻
## Referências da API 

### 🧑‍🍳 Clientes

#### Buscar clientes

```http
GET /clientes
```

| Paramêtro | Tipo | Descrição                |
| :-------- | :----| :---------------------------|
| _None_    |      | Retorna todos os clientes.  |

---

#### Adicionar cliente

```http
POST /clientes
```

| Body Paramêtro | Tipo     | Descrição                  |
| :------------- | :------- | :----------------------------|
| `nome`         | `string` | **Required**. Nome do cliente|
| `email`        | `string` | **Required**. Email do cliente|

---

#### Atualizar cliente

```http
PUT /clientes/${id}
```

| Paramêtro | Tipo  | Descrição               |
| :-------- | :-----| :-------------------------|
| `id`      | `int` | **Required**. ID do cliente|

| Body Paramêtro | Tipo     | Descrição                  |
| :------------- | :------- | :----------------------------|
| `nome`         | `string` | **Required**. Novo nome       |
| `email`        | `string` | **Required**. Novo email      |

---

#### Deletar cliente

```http
DELETE /clientes/${id}
```

| Paramêtro | Tipo  | Descrição               |
| :-------- | :-----| :-------------------------|
| `id`      | `int` | **Required**. ID do cliente|

---

### 🗂️ Categorias

#### Buscar categorias

```http
GET /categorias
```

| Paramêtro | Tipo | Descrição                   |
| :-------- | :----| :-----------------------------|
| _None_    |      | Retorna todas as categorias.  |

---

#### Adicionar categoria

```http
POST /categorias
```

| Body Paramêtro | Tipo     | Descrição                     |
| :------------- | :------- | :--------------------------------|
| `nome`         | `string` | **Required**. Nome da categoria. |

---

#### Atualizar categoria

```http
PUT /categorias/${id}
```

| Paramêtro | Tipo  | Descrição                 |
| :-------- | :-----| :---------------------------|
| `id`      | `int` | **Required**. ID da categoria|

| Body Paramêtro | Tipo     | Descrição                 |
| :------------- | :------- | :----------------------------|
| `nome`         | `string` | **Required**. Novo nome       |

---

#### Deletar categoria

```http
DELETE /categorias/${id}
```

| Paramêtro | Tipo  | Descrição                 |
| :-------- | :-----| :---------------------------|
| `id`      | `int` | **Required**. ID da categoria|

---

### 🍝 Produtos

#### Buscar produtos

```http
GET /produtos
```

| Paramêtro | Tipo | Descrição                |
| :-------- | :----| :---------------------------|
| _None_    |      | Retorna todos os produtos.  |

---

#### Adicionar produto

```http
POST /produtos
```

| Body Paramêtro | Tipo     | Descrição                     |
| :------------- | :------- | :--------------------------------|
| `nome`         | `string` | **Required**. Nome do produto    |
| `preco`        | `float`  | **Required**. Preço do produto   |
| `id_categoria` | `int`    | **Required**. ID da categoria    |

---

#### Atualizar produto

```http
PUT /produtos/${id}
```

| Paramêtro | Tipo  | Descrição                 |
| :-------- | :-----| :---------------------------|
| `id`      | `int` | **Required**. ID do produto  |

| Body Paramêtro | Tipo     | Descrição                     |
| :------------- | :------- | :--------------------------------|
| `nome`         | `string` | **Required**. Novo nome          |
| `preco`        | `float`  | **Required**. Novo preço         |
| `id_categoria` | `int`    | **Required**. Nova categoria     |

---

#### Deletar produto

```http
DELETE /produtos/${id}
```

| Paramêtro | Tipo  | Descrição                 |
| :-------- | :-----| :---------------------------|
| `id`      | `int` | **Required**. ID do produto  |

---

### 📝 Pedidos

#### Buscar pedidos

```http
GET /pedidos
```

| Paramêtro | Tipo | Descrição                |
| :-------- | :----| :---------------------------|
| _None_    |      | Retorna todos os pedidos.   |

---

#### Adicionar pedido

```http
POST /pedidos
```

| Body Paramêtro | Tipo     | Descrição                     |
| :------------- | :------- | :--------------------------------|
| `id_cliente`   | `int`    | **Required**. ID do cliente      |

---

#### Atualizar pedido

```http
PUT /pedidos/${id}
```

| Paramêtro | Tipo  | Descrição                |
| :-------- | :-----| :--------------------------|
| `id`      | `int` | **Required**. ID do pedido  |

| Body Paramêtro | Tipo     | Descrição                     |
| :------------- | :------- | :--------------------------------|
| `id_cliente`   | `int`    | **Required**. Novo cliente       |

---

#### Deletar pedido

```http
DELETE /pedidos/${id}
```

| Paramêtro | Tipo  | Descrição                |
| :-------- | :-----| :--------------------------|
| `id`      | `int` | **Required**. ID do pedido  |

---

### 🍽️ Itens do Pedido

#### Buscar itens do pedido

```http
GET /itens_pedido
```

| Paramêtro | Tipo | Descrição                      | Query
| :-------- | :----| :----------------------------------|
| _None_    |      | Retorna todos os itens dos pedidos|

---

#### Adicionar itens do pedido

```http
POST /itens_pedido
```

| Body Paramêtro | Tipo     | Descrição                          |
| :------------- | :------- | :-------------------------------------|
| `quantidade`   | `int`    | **Required**. Quantidade do item      |
| `id_pedido`    | `int`    | **Required**. ID do pedido            |
| `id_produto`   | `int`    | **Required**. ID do produto           |

---

#### Atualizar itens do pedido

```http
PUT /itens_pedido/${id}
```

| Paramêtro | Tipo  | Descrição                       |
| :-------- | :-----| :-----------------------------------|
| `id`      | `int` | **Required**. ID do item do pedido |

| Body Paramêtro | Tipo     | Descrição                          |
| :------------- | :------- | :-------------------------------------|
| `quantidade`   | `int`    | **Required**. Nova quantidade         |

---

#### Deletar itens do pedido

```http
DELETE /itens_pedido/${id}
```

| Paramêtro | Tipo  | Descrição                       |
| :-------- | :-----| :-----------------------------------|
| `id`      | `int` | **Required**. ID do item do pedido |