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

### Crie o banco de dados no PostgreSQL

psql -U postgres
CREATE DATABASE ristorante;
\q

### Importe o script do banco

psql -U postgres -d ristorante -f database.sql

### Configure o usuário e senha no arquivo app.py

db_config = {
    "host": "localhost",
    "database": "ristorante",
    "user": "seu_usuario",
    "password": "sua_senha"
}

### Rode a API

python app.py

### A API estará disponível em:
📍 http://127.0.0.1:5000/

### 📖 Endpoints da API

⸻

### 🧑‍🍳 Clientes

📥 Listar clientes

[GET] clientes
